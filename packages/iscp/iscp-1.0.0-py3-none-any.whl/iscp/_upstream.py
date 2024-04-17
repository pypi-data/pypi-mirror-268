import asyncio
import contextlib
import copy
import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Awaitable, Callable, Coroutine, Dict, List, Optional, Set
from uuid import UUID

from . import _exceptions as exceptions
from . import _message as message
from . import _model
from ._flush_policy import FlushPolicy
from ._sequence import Sequence

__all__ = [
    "Upstream",
    "AfterReceiveAckCallback",
    "BeforeSendDataPointsCallback",
    "UpstreamClosedEventHandler",
    "UpstreamClosedEvent",
]

logger = logging.getLogger(__name__)

maxUint64 = 18446744073709551615
maxUint32 = 4294967295


@dataclass
class UpstreamClosedEvent:
    """
    アップストリームをクローズした時のイベントです。

    Attributes:
        state(iscp.UpstreamState): クローズした時のアップストリームの状態
        error(Optional[iscp.ISCPException]): 内部エラーが発生した場合の例外
    """

    state: _model.UpstreamState
    error: Optional[exceptions.ISCPException] = None


UpstreamClosedEventHandler = Callable[[UpstreamClosedEvent], None]

Requester = Callable[[message.RequestMessage], Awaitable[message.RequestMessage]]
Sender = Callable[[message.UpstreamChunk], Awaitable[None]]

BeforeSendDataPointsCallback = Callable[[UUID, _model.UpstreamChunk], None]
AfterReceiveAckCallback = Callable[[UUID, _model.UpstreamChunkAck], None]


class Upstream(object):
    """
    アップストリームを表すクラスです。

    .. attention::

       このクラスのオブジェクトは、必ず iscp.Conn の `open_upstream()` を使用して生成してください。

       .. code-block:: python

           async with await Conn.connect(...) as conn:
             async with await conn.open_upstream(...) as upstream:
               pass

       このコードは以下のコードと等価です。

       .. code-block:: python

           async with await Conn.connect(...) as conn:
             upstream = await conn.open_upstream(...)
             try:
                 pass
             finally:
                 await upstream.close()

    """

    def __init__(
        self,
        id: UUID,
        id_alias: int,
        session_id: str,
        data_id_aliases: Dict[int, message.DataID],
        server_time: message.DateTime,
        requester: Requester,
        sender: Sender,
        close_timeout: float,
        ack_interval: float,
        expiry_interval: float,
        qos: message.QoS,
        flush_policy: FlushPolicy,
        persist: bool,
        receive_ack_callback: Optional[AfterReceiveAckCallback] = None,
        send_data_point_callback: Optional[BeforeSendDataPointsCallback] = None,
        closed_event_handler: Optional[UpstreamClosedEventHandler] = None,
        close_session: bool = False,
    ):
        self._flush_policy = flush_policy
        self._close_timeout = close_timeout
        self._persist = persist
        self._close_session = close_session

        # From Upstream Open Request
        self._session_id = session_id
        self._ack_interval = ack_interval
        self._expiry_interval = expiry_interval
        self._qos = qos

        # From Upstream Open Response
        self._id = id
        self._id_alias = id_alias
        self._data_id_aliases = data_id_aliases
        self._rev_data_id_aliases = {v: k for k, v in self._data_id_aliases.items()}
        self._server_time = server_time

        # State
        self._total_data_points = 0
        self._final_sequence_number = 0
        self._waiting_sequence_numbers: Set[int] = set()

        # Function
        self._requester = requester
        self._sender = sender
        self._sequence_number_sequence = Sequence.for_sequence_number()

        # Callback
        self._send_data_point_callback = send_data_point_callback if send_data_point_callback is not None else lambda a, b: None
        self._receive_ack_callback = receive_ack_callback if receive_ack_callback is not None else lambda a, b: None

        # Internal Event
        self._started_draining = asyncio.Event()
        self._received_all_ack = asyncio.Event()
        self._closed = asyncio.Event()
        self._finished_flush_buffer_size_loop = asyncio.Event()
        self._finished_flush_interval_loop = asyncio.Event()
        self._closed_event_handler = closed_event_handler

        # Internal Queue
        self._ack_queue: asyncio.Queue[message.UpstreamChunkAck] = asyncio.Queue()
        self._receive_ack_callback_queue: asyncio.Queue[_model.UpstreamChunkAck] = asyncio.Queue()
        self._send_data_point_callback_queue: asyncio.Queue[_model.UpstreamChunk] = asyncio.Queue()

        # Others
        self._send_buffer_condition = asyncio.Condition()
        self._send_buffer: Dict[message.DataID, List[message.DataPoint]] = defaultdict(lambda: [])
        self._send_buffer_size: int = 0
        self._all_loops: List[asyncio.Task] = []
        self._internal_error: Optional[exceptions.ISCPException] = None

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
        UpstreamResponseで返却されたサーバー時刻を取得します。

        Returns:
            iscp.DateTime: UpstreamResponseで返却されたサーバー時刻
        """
        return self._server_time

    @property
    def state(self):
        """
        ストリームの状態を取得します。

        Returns:
            UpstreamState: アップストリームの状態
        """
        return _model.UpstreamState(
            data_points_buffer=[
                _model.DataPointGroup(
                    data_id=copy.deepcopy(k),
                    data_points=copy.deepcopy(v),
                )
                for k, v in self._send_buffer.items()
            ],
            data_id_aliases=self._data_id_aliases.copy(),
            total_data_points=self._total_data_points,
            last_issued_sequence_number=self._sequence_number_sequence._current,
        )

    @property
    def session_id(self):
        """
        セッションIDを取得します。

        Returns:
            str: セッションID
        """
        return self._session_id

    @property
    def ack_interval(self):
        """
        Ackの返却間隔を取得します。

        Returns:
            float: Ackの返却間隔（秒）
        """
        return self._ack_interval

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
    def persist(self):
        """
        永続化フラグを取得します。

        Returns:
            Bool: 永続化フラグ
        """
        return self._persist

    @property
    def flush_policy(self):
        """
        フラッシュポリシーを取得します。

        Returns:
            iscp.FlushPolicy: フラッシュポリシー
        """
        return self._flush_policy

    @property
    def close_timeout(self):
        """
        クローズタイムアウト（秒）を取得します。

        Returns:
            float: クローズタイムアウト（秒）
        """
        return self._close_timeout

    @property
    def close_session(self):
        """
        クローズ時にセッションをクローズするかどうかを取得します。

        Returns:
            bool: クローズ時にセッションをクローズするかどうか
        """
        return self._close_session

    async def _start(self):
        self._all_loops.append(asyncio.create_task(self._ack_loop()))
        self._all_loops.append(asyncio.create_task(self._flush_interval_loop()))
        self._all_loops.append(asyncio.create_task(self._flush_buffer_size_loop()))
        self._all_loops.append(asyncio.create_task(self._receive_ack_hook_loop()))
        self._all_loops.append(asyncio.create_task(self._send_data_point_hook_loop()))
        asyncio.create_task(self._wait_closed_for_event_handler())
        return self

    async def _wait_closed_for_event_handler(self):
        await self._closed.wait()
        if self._closed_event_handler:
            self._closed_event_handler(
                UpstreamClosedEvent(
                    state=self.state,
                    error=self._internal_error,
                )
            )

    async def _receive_ack_hook_loop(self):
        logger.debug("start receive_ack_hook_loop")
        while True:
            msg = await self._receive_ack_callback_queue.get()
            self._receive_ack_callback(self._id, msg)
            self._receive_ack_callback_queue.task_done()

    async def _send_data_point_hook_loop(self):
        logger.debug("start send_data_point_hook_loop")
        while not self._started_draining.is_set():
            msg = await self._send_data_point_callback_queue.get()
            self._send_data_point_callback(self._id, msg)
            self._send_data_point_callback_queue.task_done()

    async def _ack_loop(self):
        try:
            while True:
                async with _event_or_coro(self._ack_queue.get(), self._closed) as (done, pending):
                    for result in done:
                        ack = await result
                        if isinstance(ack, message.UpstreamChunkAck):
                            self._data_id_aliases.update(ack.data_id_aliases)
                            await self._receive_ack_callback_queue.put(
                                _model.UpstreamChunkAck(
                                    results=[
                                        _model.UpstreamChunkResult(
                                            sequence_number=v.sequence_number,
                                            result_code=v.result_code,
                                            result_string=v.result_string,
                                        )
                                        for v in ack.results
                                    ]
                                )
                            )
                            self._update_data_id_alias(ack.data_id_aliases)
                            for n in [n.sequence_number for n in ack.results]:
                                self._waiting_sequence_numbers.remove(n)
                            self._ack_queue.task_done()
                            if self._finished_flush_buffer_size_loop.is_set() and self._finished_flush_interval_loop.is_set():
                                if len(self._waiting_sequence_numbers) == 0:
                                    self._received_all_ack.set()
                                    return
                        else:
                            return

        except Exception as e:
            logger.error(e)

    def _update_data_id_alias(self, arg: Dict[int, message.DataID]):
        self._data_id_aliases.update(arg)
        self._rev_data_id_aliases = {v: k for k, v in self._data_id_aliases.items()}

    async def _flush_buffer_size_loop(self):
        try:
            while True:
                async with self._send_buffer_condition:
                    if self._closed.is_set():
                        return
                    if self._started_draining.is_set() or self._flush_policy.IsFlush(self._send_buffer_size):
                        await self._flush()
                    if self._started_draining.is_set():
                        return
                    await self._send_buffer_condition.wait()
        finally:
            self._finished_flush_buffer_size_loop.set()

    async def _flush_interval_loop(self):
        try:
            tick = self._flush_policy.Ticker()
            if not tick:
                return
            async for _ in tick():
                async with self._send_buffer_condition:
                    if self._started_draining.is_set() and not self._send_buffer:
                        return
                    await self._flush()
                    if self._started_draining.is_set():
                        return
                    await self._send_buffer_condition.wait()
        finally:
            if tick:
                tick.stop()
            self._finished_flush_interval_loop.set()

    async def flush(self):
        """
        データポイントの内部バッファをUpstreamChunkとしてサーバーへ送信します。
        """
        await self._flush()

    async def _flush(self):
        if len(self._send_buffer) == 0:
            return
        data_ids: List[message.DataID] = []
        data_point_groups_msg: List[message.DataPointGroup] = []
        data_point_groups: List[_model.DataPointGroup] = []
        try:
            for k, v in self._send_buffer.items():
                data_point_groups.append(_model.DataPointGroup(data_id=k, data_points=v))

                self._total_data_points += len(v)
                if self._total_data_points > maxUint64:
                    raise exceptions.ISCPException(message="maximum total_data_points exceeded")
                if k not in self._rev_data_id_aliases:
                    data_ids.append(k)
                    data_point_groups_msg.append(message.DataPointGroup(data_id_or_alias=k, data_points=v))
                    continue

                data_point_groups_msg.append(message.DataPointGroup(data_id_or_alias=self._rev_data_id_aliases[k], data_points=v))

            sequence_number = self._sequence_number_sequence()
            chunk = message.UpstreamChunk(
                stream_id_alias=self._id_alias,
                stream_chunk=message.StreamChunk(
                    sequence_number=sequence_number,
                    data_point_groups=data_point_groups_msg,
                ),
                data_ids=data_ids,
                extension_fields=message.UpstreamChunkExtensionFields(),
            )
            self._final_sequence_number = chunk.stream_chunk.sequence_number
            self._waiting_sequence_numbers.add(chunk.stream_chunk.sequence_number)
            await self._send_data_point_callback_queue.put(
                _model.UpstreamChunk(
                    sequence_number=chunk.stream_chunk.sequence_number,
                    data_point_groups=data_point_groups,
                )
            )
            await self._sender(chunk)
            self._send_buffer = defaultdict(lambda: [])
            self._send_buffer_size = 0
        except exceptions.ISCPException as e:
            self._internal_error = e
            self._closed.set()
            for t in self._all_loops:
                t.cancel()

            await asyncio.wait(self._all_loops)

            resp = await self._requester(
                message.UpstreamCloseRequest(
                    request_id=0,
                    stream_id=self._id,
                    total_data_points=self._total_data_points,
                    final_sequence_number=self._final_sequence_number,
                    extension_fields=message.UpstreamCloseRequestExtensionFields(
                        close_session=self._close_session,
                    ),
                )
            )
            if isinstance(resp, message.UpstreamCloseResponse):
                if resp.result_code is message.ResultCode.SUCCEEDED:
                    return
                logger.error(
                    f"failed to close a upstream. stream_id \
                            [{self._id}] code=[{resp.result_code}] msg=[{resp.result_string}]",
                )
                return

            logger.error(exceptions.ISCPFailedMessageError(received_message=resp))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        with contextlib.suppress(exceptions.ISCPException):
            await self.close()

    async def write_data_points(self, data_id: message.DataID, *data_points: message.DataPoint):
        """
        データポイントを送信します。

        Args:
            data_id(iscp.DataID): データID
            *data_points(iscp.DataPoint): データポイント
        """

        if self._started_draining.is_set():
            raise exceptions.ISCPTransportClosedError()

        async with self._send_buffer_condition:
            self._send_buffer[data_id].extend(data_points)
            self._send_buffer_size += sum([len(v.payload) for v in data_points])
            self._send_buffer_condition.notify_all()

    async def _handle_ack(self, msg: message.UpstreamChunkAck):
        await self._ack_queue.put(msg)

    async def close(self, overwrite_close_session: Optional[bool] = None):
        """
        アップストリームを閉じます。

        Args:
            overwrite_close_session(Optional[bool]): アップストリームに設定されている `close_session` を上書きします。
        """
        if self._closed.is_set():
            return
        if self._started_draining.is_set():
            raise exceptions.ISCPException("already draining")

        self._started_draining.set()

        try:
            while (
                self._send_buffer
                or not self._finished_flush_buffer_size_loop.is_set()
                or not self._finished_flush_interval_loop.is_set()
            ):
                async with self._send_buffer_condition:
                    self._send_buffer_condition.notify_all()
                    await asyncio.sleep(0)

            if len(self._waiting_sequence_numbers) != 0:
                await asyncio.wait_for(self._received_all_ack.wait(), timeout=self._close_timeout)
        except asyncio.TimeoutError as e:
            logger.warning(e)

        try:
            for t in self._all_loops:
                t.cancel()

            await asyncio.wait(self._all_loops)

            resp = await self._requester(
                message.UpstreamCloseRequest(
                    request_id=0,
                    stream_id=self._id,
                    total_data_points=self._total_data_points,
                    final_sequence_number=self._final_sequence_number,
                    extension_fields=message.UpstreamCloseRequestExtensionFields(
                        close_session=overwrite_close_session if overwrite_close_session else self._close_session
                    ),
                )
            )
            if isinstance(resp, message.UpstreamCloseResponse):
                if resp.result_code is message.ResultCode.SUCCEEDED:
                    return
                logger.error(
                    f"failed to close a upstream. stream_id \
                            [{self._id}] code=[{resp.result_code}] msg=[{resp.result_string}]",
                )
                return
            raise exceptions.ISCPFailedMessageError(received_message=resp)
        finally:
            self._closed.set()


@contextlib.asynccontextmanager
async def _event_or_coro(aw: Coroutine, *evs: asyncio.Event):
    ts = [asyncio.create_task(ev.wait()) for ev in evs]
    ts.append(asyncio.create_task(aw))
    try:
        yield await asyncio.wait(ts, return_when=asyncio.FIRST_COMPLETED)

    finally:
        for t in ts:
            t.cancel()
