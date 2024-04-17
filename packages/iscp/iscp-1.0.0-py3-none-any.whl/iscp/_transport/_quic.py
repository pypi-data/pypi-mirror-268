import asyncio
import collections
import functools
import ssl
from dataclasses import dataclass
from datetime import datetime, timedelta
from io import BytesIO
from typing import Dict, List, Optional, Tuple, cast

from aioquic.asyncio.client import connect
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.quic import events
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import QuicEvent

from .. import _exceptions as exceptions
from .._sequence import Sequence
from ._negotiation_params import NegotiationParams
from ._transport import Connector, Reader, Transport, TransportName, Unreliable, Writer

__all__ = ["Quic", "QuicConnector", "_MAX_PAYLOAD_SIZE", "_MAX_PAYLOAD_SIZE"]

_MAX_DATAGRAM_FRAME_SIZE = 1170
_MAX_PAYLOAD_SIZE = _MAX_DATAGRAM_FRAME_SIZE - 8
_READ_BUFFER_EXPIRY = 1.0

_ReadWriteMessage = collections.namedtuple("ReceivedMessage", ["seq_num", "seg_idx", "max_idx", "payload"])


@dataclass
class _ReadBuffer(object):
    segment_count: int
    message_size: int
    max_idx: int
    message_payloads: List[bytes]
    expired_at: datetime

    def add(self, segment_idx: int, payload: bytes):
        if segment_idx >= len(self.message_payloads):
            raise exceptions.ISCPMalformedMessageError()

        self.segment_count += 1
        self.message_size += len(payload)
        self.message_payloads[segment_idx] = payload

    def is_complete(self) -> bool:
        return self.segment_count == (self.max_idx + 1)

    def build(self) -> bytes:
        wr = BytesIO(bytes(self.message_size))
        for v in self.message_payloads:
            wr.write(v)
        return wr.getvalue()


class _ClientProtocol(QuicConnectionProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_datagram_queue: asyncio.Queue[Optional[bytes]] = asyncio.Queue()
        self._read_stream_queue: asyncio.Queue[Optional[bytes]] = asyncio.Queue()
        self._negotiated = asyncio.Event()
        self._sequence = Sequence(initial=0, max_value=2 ^ 32, delta=1)
        self._read_buffers: Dict[int, _ReadBuffer] = {}

    async def read(self) -> bytes:
        res = await self._read_stream_queue.get()
        if res:
            self._read_stream_queue.task_done()
            rd = BytesIO(res)
            msg_size = int.from_bytes(rd.read(4), "big", signed=False)
            return rd.read(msg_size)
        raise exceptions.ISCPTransportClosedError()

    async def read_unreliable(self) -> bytes:
        while True:
            res = await self._read_datagram_queue.get()
            if res:
                self._read_datagram_queue.task_done()
                rd = BytesIO(res)
                msg = self._read_unreliable_from(rd)
                read_buffer = self._read_buffers.get(
                    msg.seq_num,
                    _ReadBuffer(
                        segment_count=0,
                        message_size=0,
                        max_idx=msg.max_idx,
                        message_payloads=[b""] * (msg.max_idx + 1),
                        expired_at=datetime.utcnow() + timedelta(seconds=_READ_BUFFER_EXPIRY),
                    ),
                )
                self._read_buffers[msg.seq_num] = read_buffer
                read_buffer.add(msg.seg_idx, msg.payload)
                if read_buffer.is_complete():
                    del self._read_buffers[msg.seq_num]
                    return read_buffer.build()
                continue
            raise exceptions.ISCPTransportClosedError()

    async def write(self, msg: bytes):
        wr = BytesIO()
        msg_size = len(msg)
        wr.write(msg_size.to_bytes(4, "big", signed=False))
        wr.write(msg)
        self._quic.send_stream_data(self._send_stream_id, wr.getvalue())
        self.transmit()

    async def write_unreliable(self, msg: bytes):
        seq_num = self._sequence()
        seg_idx = 0
        max_idx = int(len(msg) / _MAX_PAYLOAD_SIZE)
        rd = BytesIO(msg)
        while True:
            payload = rd.read(_MAX_PAYLOAD_SIZE)
            wr = BytesIO()
            self._write_unreliable_to(wr, _ReadWriteMessage(seq_num=seq_num, seg_idx=seg_idx, max_idx=max_idx, payload=payload))
            self._quic.send_datagram_frame(wr.getvalue())
            self.transmit()
            if len(payload) < _MAX_PAYLOAD_SIZE:
                return
            seg_idx += 1

    def _write_unreliable_to(self, wr: BytesIO, msg: _ReadWriteMessage):
        wr.write(msg.seq_num.to_bytes(4, "big", signed=False))
        wr.write(msg.max_idx.to_bytes(2, "big", signed=False))
        wr.write(msg.seg_idx.to_bytes(2, "big", signed=False))
        wr.write(msg.payload)

    def _read_unreliable_from(self, rd: BytesIO) -> _ReadWriteMessage:
        return _ReadWriteMessage(
            seq_num=int.from_bytes(rd.read(4), "big", signed=False),
            max_idx=int.from_bytes(rd.read(2), "big", signed=False),
            seg_idx=int.from_bytes(rd.read(2), "big", signed=False),
            payload=rd.read(),
        )

    async def _negotiate(self, negotiation_params: NegotiationParams):
        negotiation_stream_id = self._quic.get_next_available_stream_id(is_unidirectional=True)
        self._quic.send_stream_data(negotiation_stream_id, negotiation_params.encode_to_binary(), end_stream=True)

        self._send_stream_id = self._quic.get_next_available_stream_id(is_unidirectional=True)

    def quic_event_received(self, event: QuicEvent):
        if isinstance(event, events.ConnectionTerminated):
            self._read_stream_queue.put_nowait(None)
            self._read_datagram_queue.put_nowait(None)
        if isinstance(event, events.StreamDataReceived):
            self._read_stream_queue.put_nowait(event.data)
        elif isinstance(event, events.DatagramFrameReceived):
            self._read_datagram_queue.put_nowait(event.data)


class Quic(Transport, Unreliable):
    """QUICトランスポートです。"""

    def __init__(
        self,
        address: str,
        negotiation_params=NegotiationParams(),
        insecure: bool = False,
    ):
        self._address = address
        self._negotiation_params = negotiation_params
        self._insecure = insecure

        # Event
        self._connected = asyncio.Event()
        self._called_close_event = asyncio.Event()
        self._disconnected = asyncio.Event()
        self._opened = asyncio.Event()

    async def open(self):
        if self._opened.is_set():
            return self
        self._opened.set()

        task = asyncio.create_task(self._connect())

        def cb(_, done):
            done.set()

        task.add_done_callback(functools.partial(cb, done=self._disconnected))
        await self._connected.wait()
        return self

    @property
    def address(self) -> str:
        return self._address

    @property
    def name(self) -> TransportName:
        return TransportName.QUIC

    async def _connect(self):
        configuration = QuicConfiguration(
            alpn_protocols=["iscp"],
            is_client=True,
            verify_mode=ssl.CERT_NONE if self._insecure else None,
            max_datagram_frame_size=65536,
        )
        sp = self._address.split(":")
        assert len(sp) == 2

        async with connect(
            sp[0], int(sp[1]), create_protocol=_ClientProtocol, configuration=configuration, wait_connected=True
        ) as conn:
            self._protocol = cast(_ClientProtocol, conn)
            await self._protocol._negotiate(self._negotiation_params)
            self._connected.set()
            await self._called_close_event.wait()

    async def __aenter__(self):
        return await self.open()

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def read(self) -> bytes:
        return await self._protocol.read()

    async def write(self, msg: bytes):
        await self._protocol.write(msg)

    async def close(self):
        self._called_close_event.set()
        await self._disconnected.wait()

    def negotiation_params(self):
        return self._negotiation_params

    def get_unreliable(self) -> Tuple[Writer, Reader]:
        readWriter = QuicDatagram(protocol=self._protocol)
        return (readWriter, readWriter)


class QuicDatagram(Writer, Reader):
    """QUIC DatagramのReader/Writerです。"""

    def __init__(
        self,
        protocol: _ClientProtocol,
    ):
        self._protocol = protocol

    async def read(self) -> bytes:
        return await self._protocol.read_unreliable()

    async def write(self, msg: bytes):
        await self._protocol.write_unreliable(msg)


class QuicConnector(Connector):
    """
    QUICのiSCPコネクターです。

    Args:
        insecure(bool): Trueの場合、SSL証明書の検証を行いません。
    """

    def __init__(self, insecure: bool = False):
        self._insecure = insecure

    async def connect(self, address: str, negotiation_params: NegotiationParams = NegotiationParams()) -> Quic:
        quic = Quic(address=address, negotiation_params=negotiation_params, insecure=self._insecure)
        return await quic.open()
