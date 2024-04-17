import asyncio
from asyncio.exceptions import CancelledError
from contextlib import suppress
from urllib.parse import urljoin, urlparse

import websockets
from websockets.exceptions import ConnectionClosed

from .._exceptions import ISCPTransportClosedError
from ._negotiation_params import NegotiationParams
from ._transport import Connector, Transport, TransportName

__all__ = ["WebSocket", "WebSocketConnector"]


_KEEP_ALIVE_INTERVAL: float = 10


class WebSocket(Transport):
    """Websocketトランスポートです。"""

    def __init__(
        self,
        url: str,
        negotiation_params=NegotiationParams(),
    ):

        self._url = url
        self._keep_alive_interval = _KEEP_ALIVE_INTERVAL
        self._called_close_event = asyncio.Event()
        self._done_keep_alive_event = asyncio.Event()
        self._negotiation_params = negotiation_params

    async def open(self):
        self._wsconn = await websockets.connect(f"{self._url}?{self._negotiation_params.encode_to_url_values()}")
        self._keep_alive_task = asyncio.create_task(self._keep_alive(self._keep_alive_interval))
        self._called_close_event.clear()

    @property
    def address(self) -> str:
        url = urlparse(self._url)
        return url.netloc

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def write(self, msg: bytes):
        try:
            await self._wsconn.send(msg)
        except ConnectionClosed as e:
            raise ISCPTransportClosedError from e

    async def read(self) -> bytes:
        try:
            return await self._wsconn.recv()
        except ConnectionClosed as e:
            raise ISCPTransportClosedError from e

    async def _keep_alive(self, interval: float):
        while not self._called_close_event.is_set() and not self._wsconn.closed:
            pong_waiter = await self._wsconn.ping()
            await pong_waiter
            await asyncio.sleep(interval)

    async def close(self):

        if self._called_close_event.is_set():
            return None

        self._called_close_event.set()

        await self._wsconn.close()
        await self._wsconn.wait_closed()
        self._keep_alive_task.cancel()
        with suppress(CancelledError):
            await self._keep_alive_task

    def negotiation_params(self):
        return self._negotiation_params

    @property
    def name(self) -> TransportName:
        return TransportName.WEBSOCKET


class WebSocketConnector(Connector):
    """
    WebSocketのiSCPコネクターです。

    Args:
        enable_tls(bool): TLS有効化フラグ。Trueの場合は ``wss://${address}/${path}`` ,Falseの場合は ``ws://${address}/${path}`` でアクセスを試みます。
        path(str): 接続先のaddressに続くパス
    """

    def __init__(self, *, keep_alive_interval: float = 10, enable_tls=True, path="api/iscp/connect"):
        self._keep_alive_interval = keep_alive_interval
        self._scheme = "wss" if enable_tls else "ws"
        self._path = path

    async def connect(self, address: str, negotiation_params: NegotiationParams) -> WebSocket:
        ws = WebSocket(
            url=urljoin(f"{self._scheme}://{address}", self._path),
            negotiation_params=negotiation_params,
        )
        await ws.open()
        return ws
