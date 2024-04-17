import asyncio
import logging
from asyncio.tasks import Task
from dataclasses import dataclass
from typing import AsyncIterator, Awaitable, Callable, Dict, List, Optional
from uuid import UUID

from . import _exceptions as exceptions
from . import _message as message
from . import _model
from ._message import DateTime, DownstreamChunk, DownstreamMetadata
from ._sequence import Sequence
from ._ticker import Ticker
from ._utils import drain, enqueue

__all__ = [
    "Downstream",
    "_DownstreamChunkIterator",
    "DownstreamMetadata",
    "_DownstreamMetadataIterator",
    "DownstreamClosedEventHandler",
    "DownstreamClosedEvent",
]

logger = logging.getLogger(__name__)


@dataclass
class DownstreamClosedEvent:
    """
    ダウンストリームをクローズした時のイベントです。

    Attributes:
        state(iscp.DownstreamState): クローズしたときのダウンストリームの状態
        error(Optional[iscp.ISCPException]): 内部エラーが発生した場合の例外
    """

    state: _model.DownstreamState
    error: Optional[exceptions.ISCPException] = None


DownstreamClosedEventHandler = Callable[[DownstreamClosedEvent], None]
DownstreamChunkCallback = Callable[[_model.DownstreamChunk], None]
DownstreamMetadataCallback = Callable[[_model.DownstreamMetadata], None]
_DownstreamChunkIterator = AsyncIterator[_model.DownstreamChunk]
_DownstreamMetadataIterator = AsyncIterator[_model.DownstreamMetadata]


class Downstream(object):
    """
    ダウンストリームを表すクラスです。

    .. attention::

       このクラスのオブジェクトは、必ず iscp.Conn の `open_downstream()` を使用して生成してください。

       .. code-block:: python

           async with await Conn.connect(...) as conn:
             async with await conn.open_downstream(...) as downstream:
               pass

       このコードは以下のコードと等価です。

       .. code-block:: python

           async with await Conn.connect(...) as conn:
             downstream = await conn.open_downstream(...)
             try:
                 pass
             finally:
                 await downstream.close()

    """

    def __init__(
        self,
        id: UUID,
        id_alias: int,
        server_time: DateTime,
        qos: message.QoS,
        expiry_interval: float,
        filters: List[message.DownstreamFilter],
        requester: Callable[[message.RequestMessage], Awaitable[message.RequestMessage]],
        request_message_sender: Callable[[message.RequestMessage], Awaitable[None]],
        stream_message_sender: Callable[[message.StreamMessage], Awaitable[None]],
        data_id_aliases: Dict[int, message.DataID],
        data_id_alias_sequence: Optional[Sequence] = None,
        # TODO: implement
        # cb: Optional[DownstreamChunkCallback] = None,
        # metadata_cb: Optional[DownstreamChunkCallback] = None,
        ack_interval: float = 1,
        closed_event_handler: Optional[DownstreamClosedEventHandler] = None,
    ):

        # Config
        self._ack_interval = ack_interval

        # From DownstreamOpenRequest
        self._stream_id_alias = id_alias
        self._qos = qos
        self._expiry_interval = expiry_interval
        self._filters = filters

        # From DownstreamOpenResponse
        self._id = id
        self._server_time = server_time

        # State
        self._total_data_points = 0
        self._final_sequence_number = 0
        self._data_id_aliases = data_id_aliases
        self._rev_data_id_aliases = {v: k for k, v in data_id_aliases.items()}

        self._upstream_info_aliases: Dict[int, message.UpstreamInfo] = {}
        self._rev_upstream_info_aliases: Dict[message.UpstreamInfo, int] = {}

        self._requester = requester

        self._stream_message_sender = stream_message_sender
        self._request_message_sender = request_message_sender

        # Queue
        self._queue: asyncio.Queue[Optional[DownstreamChunk]] = asyncio.Queue(maxsize=262144)
        self._generator_call_once = asyncio.Event()

        self._metadata_queue: asyncio.Queue[Optional[DownstreamMetadata]] = asyncio.Queue(maxsize=256)
        self._metadata_generator_call_once = asyncio.Event()

        # Buffer
        self._ack_chunk_result_buffer: List[message.DownstreamChunkResult] = []
        self._ack_data_id_aliases_buffer: Dict[int, message.DataID] = {}
        self._ack_upstream_info_buffer: Dict[int, message.UpstreamInfo] = {}

        # Sequences
        self._ack_id_sequence = Sequence.for_ack_id()
        self._data_id_alias_sequence = data_id_alias_sequence if data_id_alias_sequence else Sequence.for_data_id_alias()
        self._upstream_info_alias_sequence = Sequence.for_data_id_alias()

        self._loop_tasks: List[Task] = []

        # TODO: implement callback
        # self._cb = cb
        # self._metadata_cb = metadata_cb
        # status
        self._is_closed = asyncio.Event()
        self._is_draining = asyncio.Event()
        self._closed_event_handler = closed_event_handler

        self._internal_error: Optional[exceptions.ISCPException] = None

    @property
    def state(self):
        """
        ストリームの状態を取得します。

        Returns:
            DownstreamState: ダウンストリームの状態
        """
        return _model.DownstreamState(
            id=self._id,
            data_id_aliases=self._data_id_aliases,
            last_issued_data_id_alias=self._data_id_alias_sequence._current,
            upstream_infos=self._upstream_info_aliases,
            last_issued_upstream_info_alias=self._upstream_info_alias_sequence._current,
            last_issued_ack_id=self._ack_id_sequence._current,
            server_time=self._server_time,
        )

    @property
    def id(self):
        """
        ストリームIDを取得します。

        Returns:
            UUID: ストリームID
        """
        return self._id

    @property
    def server_time(self):
        """
        DownstreamResponseで返却されたサーバー時刻を取得します。

        Returns:
            iscp.DateTime: DownstreamResponseで返却されたサーバー時刻
        """
        return self._server_time

    @property
    def expiry_interval(self):
        """
        有効期限を取得します。

        Returns:
            float: ストリームの有効期限（秒）
        """
        return self._expiry_interval

    @property
    def qos(self):
        """
        QoSを取得します。

        Returns:
            iscp.QoS: QoS
        """
        return self._qos

    @property
    def ack_interval(self):
        """
        Ack返却間隔（秒）を取得します。

        Returns:
            float: Ack返却間隔（秒）
        """
        return self._ack_interval

    @property
    def filters(self):
        """
        ダウンストリームフィルターを取得します。

        Returns:
            List[iscp.DownstreamFilter]: ダウンストリームフィルターのリスト
        """
        return self._filters

    async def _start(self):
        self._loop_tasks.append(asyncio.create_task(self._flush_ack_loop()))
        asyncio.create_task(self._wait_closed_for_event_handler())
        return self

    async def _wait_closed_for_event_handler(self):
        await self._is_closed.wait()
        if self._closed_event_handler:
            self._closed_event_handler(DownstreamClosedEvent(state=self.state, error=self._internal_error))

    async def _handle_chunk_ack_complete(self, msg: message.DownstreamChunkAckComplete):
        if msg.result_code == message.ResultCode.SUCCEEDED:
            return
        logger.warn(f"code[{msg.result_code!r}],message,[{msg.result_string!r}]")

    async def _handle_chunk(self, msg: DownstreamChunk):
        enqueue(self._queue, msg)

    async def _handle_metadata(self, msg: DownstreamMetadata):
        enqueue(self._metadata_queue, msg)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def _flush_ack_loop(self):
        async with Ticker.of(delay=self._ack_interval) as tick:
            async for _ in tick():
                if not self._ack_chunk_result_buffer:
                    continue
                await self._stream_message_sender(
                    message.DownstreamChunkAck(
                        ack_id=self._ack_id_sequence(),
                        stream_id_alias=self._stream_id_alias,
                        results=self._ack_chunk_result_buffer,
                        upstream_aliases=self._ack_upstream_info_buffer,
                        data_id_aliases=self._data_id_aliases,
                        extension_fields=message.DownstreamChunkAckExtensionFields(),
                    )
                )
                self._ack_upstream_info_buffer = {}
                self._ack_data_id_aliases_buffer = {}
                self._ack_chunk_result_buffer = []

    async def chunks(self, *, timeout: Optional[float] = None) -> _DownstreamChunkIterator:
        """

        ダウンストリームチャンクを受信します。

        Args:
            timeout (Optional[float]): 読み込みタイムアウト（秒）。指定しない場合はタイムアウトしません。
        Yields:
            iscp.DownstreamChunk: ダウンストリームチャンク
        Examples:
            >>> with conn.open_downstream(...) as downstream:
                  async for msg in downstream.chunks():
                      print(msg)

        """
        # assert not self._cb, ""
        assert not self._generator_call_once.is_set(), "already called generator"
        self._generator_call_once.set()

        while True:
            msg = await asyncio.wait_for(self._queue.get(), timeout=timeout)
            if not msg:
                return
            self._queue.task_done()
            if (
                isinstance(msg.upstream_or_alias, message.UpstreamInfo)
                and msg.upstream_or_alias not in self._rev_upstream_info_aliases
            ):
                alias = self._push_upstream_info(msg.upstream_or_alias)
                self._ack_upstream_info_buffer[alias] = msg.upstream_or_alias

            self._ack_chunk_result_buffer.append(
                message.DownstreamChunkResult(
                    result_code=message.ResultCode.SUCCEEDED,
                    result_string="OK",
                    sequence_number_in_upstream=msg.stream_chunk.sequence_number,
                    stream_id_of_upstream=msg.upstream_or_alias.stream_id
                    if isinstance(msg.upstream_or_alias, message.UpstreamInfo)
                    else self._upstream_info_aliases[msg.upstream_or_alias].stream_id,
                    extension_fields=message.DownstreamChunkResultExtensionFields(),
                )
            )

            def update_data_id_alias(v: message.DataPointGroup) -> _model.DataPointGroup:
                if isinstance(v.data_id_or_alias, message.DataID) and v.data_id_or_alias not in self._rev_data_id_aliases:
                    alias = self._push_data_id_alias(v.data_id_or_alias)
                    self._ack_data_id_aliases_buffer[alias] = v.data_id_or_alias
                return _model.DataPointGroup(
                    data_id=v.data_id_or_alias
                    if isinstance(v.data_id_or_alias, message.DataID)
                    else self._data_id_aliases[v.data_id_or_alias],
                    data_points=v.data_points,
                )

            yield _model.DownstreamChunk(
                upstream_info=msg.upstream_or_alias
                if isinstance(msg.upstream_or_alias, message.UpstreamInfo)
                else self._upstream_info_aliases[msg.upstream_or_alias],
                sequence_number=msg.stream_chunk.sequence_number,
                data_point_groups=[update_data_id_alias(v) for v in msg.stream_chunk.data_point_groups],
            )

    def _push_data_id_alias(self, msg: message.DataID) -> int:
        """
        Returns:
            データIDエイリアス
        """
        alias = self._data_id_alias_sequence()
        self._data_id_aliases[alias] = msg
        self._rev_data_id_aliases[msg] = alias
        return alias

    def _push_upstream_info(self, msg: message.UpstreamInfo) -> int:
        """
        Returns:
            アップストリームエイリアス
        """
        alias = self._upstream_info_alias_sequence()
        self._upstream_info_aliases[alias] = msg
        self._rev_upstream_info_aliases[msg] = alias
        return alias

    async def metadatas(self, *, timeout: Optional[float] = None) -> _DownstreamMetadataIterator:
        """

        タイムアウトを指定して、ダウンストリームメタデータを受信します。

        Args:
            timeout (Optional[float]): 読み込みタイムアウト（秒）。指定しない場合はタイムアウトしません。
        Yields:
            iscp.DownstreamMetadata: ダウンストリームメタデータ
        Examples:
            >>> with conn.open_downstream(...) as downstream:
                  async for msg in downstream.metadatas():
                      print(msg)
        """
        # assert not self._metadata_cb, ""
        assert not self._metadata_generator_call_once.is_set(), "already called metadata_generator"
        self._metadata_generator_call_once.set()

        while True:
            msg = await asyncio.wait_for(self._metadata_queue.get(), timeout=timeout)
            if not msg:
                return
            self._metadata_queue.task_done()
            await self._request_message_sender(
                message.DownstreamMetadataAck(
                    request_id=msg.request_id,
                    result_code=message.ResultCode.SUCCEEDED,
                    result_string="OK",
                    extension_fields=message.DownstreamMetadataAckExtensionFields(),
                )
            )
            yield _model.DownstreamMetadata(
                source_node_id=msg.source_node_id,
                metadata=msg.metadata,
            )

    async def close(self):

        """
        ダウンストリームを閉じます。
        """

        if self._is_closed.is_set():
            return

        if self._is_draining.is_set():
            raise exceptions.ISCPException(message="already draining")

        self._is_draining.set()

        try:
            for t in self._loop_tasks:
                t.cancel()

            await asyncio.wait(self._loop_tasks)

            drain(self._metadata_queue)
            # send done
            self._metadata_queue.put_nowait(None)

            drain(self._queue)
            # send done
            self._queue.put_nowait(None)

            resp = await self._requester(
                message.DownstreamCloseRequest(
                    request_id=0,
                    stream_id=self._id,
                    extension_fields=message.DownstreamCloseRequestExtensionFields(),
                )
            )
            if isinstance(resp, message.DownstreamCloseResponse):
                if resp.result_code is message.ResultCode.SUCCEEDED:
                    return
                logger.error(
                    f"failed to close a downstream. stream_id \
                            [{self._id}] code=[{resp.result_code}] msg=[{resp.result_string}]",
                )
                return

            raise exceptions.ISCPFailedMessageError(received_message=resp)
        except Exception as e:
            raise e
        finally:
            self._is_closed.set()
