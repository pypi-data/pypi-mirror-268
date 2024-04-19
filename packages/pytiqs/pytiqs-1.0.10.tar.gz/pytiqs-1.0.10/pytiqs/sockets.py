from typing import Optional, Any, Dict, List, Callable, Union

import six
import sys
import time
import json
import logging
import threading

from autobahn.websocket import ConnectionResponse
from twisted.internet import reactor, ssl
from twisted.internet.interfaces import IConnector
from twisted.python import log as twisted_log
from twisted.internet.protocol import ReconnectingClientFactory
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory, connectWS
from twisted.python.failure import Failure

from .__version__ import __version__, __title__

log = logging.getLogger(__name__)


class TiqsClientProtocol(WebSocketClientProtocol):
    PING_INTERVAL = 2.5
    KEEPALIVE_INTERVAL = 5

    _next_ping = None
    _next_pong_check = None
    _last_pong_time = None
    _last_ping_time = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(TiqsClientProtocol, self).__init__(*args, **kwargs)

    def onConnect(self, response: ConnectionResponse) -> None:
        self.factory.ws = self
        if self.factory.on_connect:
            self.factory.on_connect(self, response)
        self.factory.resetDelay()
        # pass

    def onOpen(self) -> None:
        self._loop_ping()
        self._loop_pong_check()
        if self.factory.on_open:
            self.factory.on_open(self)

    def onMessage(self, payload: bytes, is_binary: bool) -> None:
        if self.factory.on_message:
            self.factory.on_message(self, payload, is_binary)

    def onClose(self, was_clean: bool, code: int, reason: str) -> None:
        if not was_clean:
            if self.factory.on_error:
                self.factory.on_error(self, code, reason)

        if self.factory.on_close:
            self.factory.on_close(self, code, reason)
        self._last_ping_time = None
        self._last_pong_time = None
        if self._next_ping:
            self._next_ping.cancel()
        if self._next_pong_check:
            self._next_pong_check.cancel()

    def onPong(self, response: str) -> None:
        if self._last_pong_time and self.factory.debug:
            log.debug("last pong was {} seconds back.".format(time.time() - self._last_pong_time))
        self._last_pong_time = time.time()
        if self.factory.debug:
            log.debug("pong => {}".format(response))

    def _loop_ping(self) -> None:
        if self.factory.debug:
            if self._last_ping_time:
                log.debug("last ping was {} seconds back.".format(time.time() - self._last_ping_time))
        self._last_ping_time = time.time()
        self._next_ping = self.factory.reactor.callLater(self.PING_INTERVAL, self._loop_ping)

    def _loop_pong_check(self) -> None:
        if self._last_pong_time:
            last_pong_diff = time.time() - self._last_pong_time
            if last_pong_diff > (2 * self.PING_INTERVAL):
                if self.factory.debug:
                    log.debug("Last pong was {} seconds ago. So dropping connection to reconnect.".format(
                        last_pong_diff))
                self.dropConnection(abort=True)
        self._next_pong_check = self.factory.reactor.callLater(self.PING_INTERVAL, self._loop_pong_check)


class TiqsClientFactory(WebSocketClientFactory, ReconnectingClientFactory):  # type: ignore
    protocol = TiqsClientProtocol
    maxDelay = 5
    maxRetries = 10  # type: Any
    _last_connection_time = None

    def __init__(self, *args: Any, **kwargs: Any):
        self.debug = False
        self.ws = None
        self.on_open = None  # type: Optional[Callable[[websocket.WebSocket], None]]
        self.on_error = None  # type: Optional[Callable[[websocket.WebSocket, int, str], None]]
        self.on_close = None  # type: Optional[Callable[[websocket.WebSocket, int, str], None]]
        self.on_message = None  # type: Optional[Callable[[websocket.WebSocket, bytes, bool], None]]
        self.on_connect = None  # type: Optional[Callable[[websocket.WebSocket, ConnectionResponse], None]]
        self.on_reconnect = None  # type: Optional[Callable[[int], None]]
        self.on_noreconnect = None  # type: Optional[Callable[[], None]]
        super(TiqsClientFactory, self).__init__(*args, **kwargs)

    def startedConnecting(self, connector: IConnector) -> None:
        if not self._last_connection_time and self.debug:
            log.debug("Start WebSocket connection.")
        self._last_connection_time = time.time()

    def clientConnectionFailed(self, connector: IConnector, reason: Failure) -> None:
        if self.retries > 0:
            log.error(
                "Retrying connection. Retry attempt count: {}. Next retry in around: {} seconds".format(self.retries,
                                                                                                        int(round(
                                                                                                            self.delay))))
            if self.on_reconnect:
                self.on_reconnect(self.retries)
        self.retry(connector)  # type: ignore
        self.send_noreconnect()

    def clientConnectionLost(self, connector: IConnector, reason: Failure) -> None:
        if self.retries > 0:
            if self.on_reconnect:
                self.on_reconnect(self.retries)
        self.retry(connector)  # type: ignore
        self.send_noreconnect()

    def send_noreconnect(self) -> None:
        if self.maxRetries is not None and (self.retries > self.maxRetries):
            if self.debug:
                log.debug("Maximum retries ({}) exhausted.".format(self.maxRetries))
                self.stop()
            if self.on_noreconnect:
                self.on_noreconnect()


class TiqsSocket(object):
    CONNECT_TIMEOUT = 30
    RECONNECT_MAX_DELAY = 60
    RECONNECT_MAX_TRIES = 50
    ROOT_URI = "wss://wss.tiqs.trading"

    # Available streaming modes.
    MODE_LTPC = "ltpc"
    MODE_QUOTE = "quote"
    MODE_LTP = "ltp"
    MODE_FULL = "full"

    _is_first_connect = True

    _message_code = 11
    _message_subscribe = "sub"
    _message_unsubscribe = "unsub"
    _message_setmode = "mode"

    _minimum_reconnect_max_delay = 5
    _maximum_reconnect_max_tries = 300

    def __init__(self, app_id: str, token: str, debug: bool = False, root: Optional[str] = None,
                 reconnect: bool = True, reconnect_max_tries: int = RECONNECT_MAX_TRIES,
                 reconnect_max_delay: int = RECONNECT_MAX_DELAY,
                 connect_timeout: int = CONNECT_TIMEOUT) -> None:
        self.root = root or self.ROOT_URI
        if reconnect_max_tries > self._maximum_reconnect_max_tries:
            log.warning(
                "`reconnect_max_tries` can not be more than {val}. Setting to highest possible value - {val}.".format(
                    val=self._maximum_reconnect_max_tries))
            self.reconnect_max_tries = self._maximum_reconnect_max_tries
        else:
            self.reconnect_max_tries = reconnect_max_tries
        if reconnect_max_delay < self._minimum_reconnect_max_delay:
            log.warning(
                "`reconnect_max_delay` can not be less than {val}. Setting to lowest possible value - {val}.".format(
                    val=self._minimum_reconnect_max_delay))
            self.reconnect_max_delay = self._minimum_reconnect_max_delay
        else:
            self.reconnect_max_delay = reconnect_max_delay
        self.connect_timeout = connect_timeout
        self.socket_url = "{root}?appId={app_id}&token={token}".format(
            root=self.root,
            app_id=app_id,
            token=token
        )
        self.debug = debug
        self.ws = None

        self.on_ticks = None  # type: Optional[Callable[[Any, Any], None]]
        self.on_open = None  # type: Optional[Callable[[Any], None]]
        self.on_close = None  # type: Optional[Callable[[Any, int, str], None]]
        self.on_error = None  # type: Optional[Callable[[Any, int, str], None]]
        self.on_connect = None  # type: Optional[Callable[[Any, Any], None]]
        self.on_message = None  # type: Optional[Callable[[Any, bytes, bool], None]]
        self.on_reconnect = None  # type: Optional[Callable[[Any, int], None]]
        self.on_noreconnect = None  # type: Optional[Callable[[Any], None]]
        self.on_order_update = None  # type: Optional[Callable[[Any, Dict[str, Any]], None]]
        self.subscribed_tokens = {}  # type: Dict[int, str]

    def _create_connection(self, url: str, **kwargs: Any) -> None:
        self.factory = TiqsClientFactory(url, **kwargs)
        self.ws = self.factory.ws
        self.factory.debug = self.debug

        # Register private callbacks
        self.factory.on_open = self._on_open
        self.factory.on_error = self._on_error
        self.factory.on_close = self._on_close
        self.factory.on_message = self._on_message
        self.factory.on_connect = self._on_connect
        self.factory.on_reconnect = self._on_reconnect
        self.factory.on_noreconnect = self._on_noreconnect

        self.factory.maxDelay = self.reconnect_max_delay
        self.factory.maxRetries = self.reconnect_max_tries

    def _user_agent(self) -> str:
        return (__title__ + "-python/").capitalize() + __version__

    def connect(self, threaded: bool = False, disable_ssl_verification: bool = False, proxy: Any = None) -> None:
        if self.debug:
            log.debug("Connecting to {}".format(self.socket_url))
        self._create_connection(self.socket_url,
                                useragent=self._user_agent(),
                                proxy=proxy)
        context_factory = None
        if self.factory.isSecure and not disable_ssl_verification:
            context_factory = ssl.ClientContextFactory()
        connectWS(self.factory, contextFactory=context_factory, timeout=self.connect_timeout)
        if self.debug:
            twisted_log.startLogging(sys.stdout)
        opts = {}
        if not reactor.running:
            if threaded:
                opts["installSignalHandlers"] = False
                self.websocket_thread = threading.Thread(target=reactor.run, kwargs=opts)
                self.websocket_thread.daemon = True
                self.websocket_thread.start()
            else:
                reactor.run(**opts)

    def is_connected(self) -> bool:
        if self.ws and self.ws.state and self.ws.state == self.ws.STATE_OPEN:
            return True
        else:
            return False

    def _close(self, code: Optional[int] = None, reason: Optional[str] = None) -> None:
        if self.ws:
            self.ws.sendClose(code, reason)

    def close(self, code: Optional[int] = None, reason: Optional[str] = None) -> None:
        self.stop_retry()
        self._close(code, reason)

    def stop(self) -> None:
        reactor.stop()  # type: ignore

    def stop_retry(self) -> None:
        if self.factory:
            self.factory.stopTrying()

    def subscribe(self, instrument_tokens: List[int]) -> None:
        try:
            self.ws.sendMessage(
                # six.b(json.dumps({"a": self._message_subscribe, "v": instrument_tokens}))
                six.b(json.dumps({
                    "code": self._message_subscribe,
                    "mode": self.MODE_QUOTE,
                    self.MODE_QUOTE: instrument_tokens
                }))
            )

            for token in instrument_tokens:
                self.subscribed_tokens[token] = self.MODE_QUOTE

            return True
        except Exception as e:
            self._close(reason="Error while subscribe: {}".format(str(e)))
            raise

    def unsubscribe(self, instrument_tokens: List[int]) -> None:
        try:
            unsubscribe_dict = {}
            for token in instrument_tokens:
                if token in unsubscribe_dict:
                    unsubscribe_dict[self.subscribed_tokens[token]].append(token)
                else:
                    unsubscribe_dict[self.subscribed_tokens[token]] = [token]

            for mode, tokenList in unsubscribe_dict.items():
                self.ws.sendMessage(
                    six.b(json.dumps({
                        "code": self._message_unsubscribe,
                        "mode": mode,
                        mode: tokenList
                    }))
                )

            for token in instrument_tokens:
                try:
                    del (self.subscribed_tokens[token])
                except KeyError:
                    pass

            return True
        except Exception as e:
            self._close(reason="Error while unsubscribe: {}".format(str(e)))
            raise

    def set_mode(self, mode: str, instrument_tokens: List[int]) -> None:
        try:
            # subscribed_instruments = [int(key) for key in self.subscribed_tokens.keys()]
            # self.unsubscribe(subscribed_instruments)
            req = {
                    "code": self._message_subscribe,
                    "mode": mode,
                    mode: instrument_tokens
                }
            if self.debug:
                log.debug("set_mode payload {}".format(json.dumps(req)))
            self.ws.sendMessage(
                six.b(json.dumps(req))
            )

            # Update modes
            for token in instrument_tokens:
                self.subscribed_tokens[token] = mode

            return True
        except Exception as e:
            self._close(reason="Error while setting mode: {}".format(str(e)))
            raise

    def resubscribe(self) -> None:
        modes = {} # type: Dict[str, List[int]]

        for token in self.subscribed_tokens:
            m = self.subscribed_tokens[token]

            if not modes.get(m):
                modes[m] = []

            modes[m].append(token)

        for mode in modes:
            if self.debug:
                log.debug("Resubscribe and set mode: {} - {}".format(mode, modes[mode]))

            self.subscribe(modes[mode])
            self.set_mode(mode, modes[mode])

    def _on_connect(self, ws, response: ConnectionResponse) -> None:
        self.ws = ws
        if self.on_connect:
            self.on_connect(self, response)

    def _on_close(self, ws, code, reason):
        log.error("Connection closed: {} - {}".format(code, str(reason)))

        if self.on_close:
            self.on_close(self, code, reason)

    def _on_error(self, ws, code: int, reason: str) -> None:
        log.error("Connection error: {} - {}".format(code, str(reason)))

        if self.on_error:
            self.on_error(self, code, reason)

    def _on_message(self, ws, payload: bytes, is_binary: bool) -> None:
        if self.on_message:
            self.on_message(self, payload, is_binary)

        # If the message is binary, parse it and send it to the callback.
        if self.on_ticks and is_binary and len(payload) > 4:
            self.on_ticks(self, self._parse_binary(payload))

        # Parse text messages
        if not is_binary:
            self._parse_message(ws, payload)

    def _on_open(self, ws) -> None:
        if not self._is_first_connect:
            self.resubscribe()
        self._is_first_connect = False

        if self.on_open:
            return self.on_open(self)

    def _on_reconnect(self, attempts_count: int) -> None:
        if self.on_reconnect:
            return self.on_reconnect(self, attempts_count)

    def _on_noreconnect(self) -> None:
        if self.on_noreconnect:
            return self.on_noreconnect(self)

    def _parse_message(self, ws, payload: Union[str, bytes]) -> None:
        if type(payload) == bytes:
            payload = payload.decode("utf-8")
        try:
            data = json.loads(payload)
        except ValueError:
            return
        if self.on_order_update and data.get("type") == "orderUpdate":
            self.on_order_update(self, data)

    def _parse_binary(self, data: bytes) -> Dict[str, Any]:
        tick = {}  # type: Dict[str, Any]
        if self.debug:
            log.debug("Parsing binary, len: {}".format(len(data)))
        if len(data) >= 13:
            tick['token'] = int.from_bytes(data[0:4])
            tick['ltp'] = int.from_bytes(data[4:8])
            tick['mode'] = self.MODE_LTP
        if len(data) == 17:
            tick['close'] = int.from_bytes(data[13:17])
            tick['netChange'] = round(((tick['ltp'] - tick['close']) / tick['close']) * 100 + 1e-9, 2) or 0.00
            if tick['ltp'] > tick['close']:
                tick['changeFlag'] = 43  # ascii code for '+'
            elif tick['ltp'] < tick['close']:
                tick['changeFlag'] = 45  # ascii code for '-'
            else:
                tick['changeFlag'] = 32  # no change
            tick['mode'] = self.MODE_LTPC
        if len(data) >= 69:
            tick['ltq'] = int.from_bytes(data[13:17])
            tick['avgPrice'] = int.from_bytes(data[17:21])
            tick['totalBuyQuantity'] = int.from_bytes(data[21:25])
            tick['totalSellQuantity'] = int.from_bytes(data[25:29])
            tick['open'] = int.from_bytes(data[29:33])
            tick['high'] = int.from_bytes(data[33:37])
            tick['close'] = int.from_bytes(data[37:41])
            tick['low'] = int.from_bytes(data[41:45])
            tick['volume'] = int.from_bytes(data[45:49])
            tick['time'] = int.from_bytes(data[53:57])
            tick['oi'] = int.from_bytes(data[57:61])
            tick['oiDayHigh'] = int.from_bytes(data[61:65])
            tick['oiDayLow'] = int.from_bytes(data[65:69])
            tick['netChange'] = round(((tick['ltp'] - tick['close']) / tick['close']) * 100 + 1e-9, 2) or int(0)
            if tick['ltp'] > tick['close']:
                tick['changeFlag'] = 43  # ascii code for '+'
            elif tick['ltp'] < tick['close']:
                tick['changeFlag'] = 45  # ascii code for '-'
            else:
                tick['changeFlag'] = 32  # no change
            tick['mode'] = self.MODE_QUOTE
        if len(data) >= 197:
            tick['ltt'] = int.from_bytes(data[49:53])
            tick['lowerLimit'] = int.from_bytes(data[69:73])
            tick['upperLimit'] = int.from_bytes(data[73:77])
            bids = []
            asks = []
            for i in range(10):
                quantity = int.from_bytes(data[77 + i * 12:81 + i * 12])
                price = int.from_bytes(data[81 + i * 12:85 + i * 12])
                orders = int.from_bytes(data[85 + i * 12:89 + i * 12])
                if i >= 5:
                    asks.append({'price': price, 'quantity': quantity, 'orders': orders})
                else:
                    bids.append({'price': price, 'quantity': quantity, 'orders': orders})
            tick['bids'] = bids
            tick['asks'] = asks
            tick['mode'] = self.MODE_FULL
        if tick.get('close', 0) == 0:
            tick['netChange'] = 0
        return tick
