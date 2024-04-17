import asyncio
import logging
import uuid
from asyncio.exceptions import CancelledError
from collections import defaultdict
from contextlib import contextmanager, suppress
from dataclasses import dataclass
from typing import AsyncIterator, Awaitable, Callable, Dict, Generator, List, Optional
from uuid import UUID

from . import _message as message
from . import _model
from ._downstream import Downstream, DownstreamClosedEventHandler
from ._encoding import Encoding, Protobuf
from ._exceptions import ISCPException, ISCPFailedMessageError, ISCPTransportClosedError
from ._flush_policy import FlushPolicy, IntervalOrBufferSize
from ._message import DownstreamCall, DownstreamChunk, DownstreamMetadata
from ._sequence import Sequence
from ._ticker import Ticker
from ._transport import (
    Connector,
    EncodingName,
    NegotiationParams,
    Reader,
    Transport,
    Unreliable,
    Writer,
)
from ._upstream import (
    AfterReceiveAckCallback,
    BeforeSendDataPointsCallback,
    Upstream,
    UpstreamClosedEventHandler,
)

__all__ = ["TokenSource", "Conn", "DisconnectedEventHandler", "DisconnectedEvent"]

logger = logging.getLogger(__name__)

DEFAULT_PING_INTERVAL = 10.0
DEFAULT_PING_TIMEOUT = 1.0
DEFAULT_FLUSH_POLICY = IntervalOrBufferSize()

TokenSource = Callable[[], str]


@dataclass
class DisconnectedEvent:
    """
    切断時のイベントです。

    Attributes:
        error(Optional[iscp.ISCPException]): 内部エラー発生した場合の例外
    """

    error: Optional[ISCPException] = None


DisconnectedEventHandler = Callable[[DisconnectedEvent], None]


class Conn(object):
    """
    iSCPのコネクションを表すクラスです。

    .. attention::

       このクラスのオブジェクトは、必ず Conn の `connect()` を使用して生成してください。

       .. code-block:: python

           async with await Conn.connect(...) as conn:
            pass

       このコードは以下のコードと等価です。

       .. code-block:: python

           conn = await Conn.connect(...)
           try:
               pass
           finally:
               await conn.close()

    """

    @classmethod
    async def connect(
        cls,
        address: str,
        connector: Connector,
        *,
        encoding: EncodingName | str = EncodingName.PROTOBUF,
        node_id: Optional[str] = None,
        ping_interval: float = DEFAULT_PING_INTERVAL,
        ping_timeout: float = DEFAULT_PING_TIMEOUT,
        project_uuid: Optional[UUID | str] = None,
        token_source: Optional[TokenSource] = None,
        disconnected_event_handler: Optional[DisconnectedEventHandler] = None,
    ):
        """
        iSCPブローカーに接続します。

        Args:
            address(str): 接続先のアドレス。`127.0.0.1:8080` 形式。
            connector(iscp.Connector): トランスポートのコネクターです。
            encoding(iscp.EncodingName|str): エンコーディング名
            node_id(Optional[str]): ノードID
            ping_interval(float): Ping間隔（秒）
            ping_timeout(float): Pingタイムアウト（秒）。タイムアウトが発生した場合トランスポートを切断します。
            project_uuid(Optional[UUID | str]): プロジェクトUUID
            token_source(Optional[iscp.TokenSource]): トークンソース。iSCPコネクションを開くたびに、このメソッドをコールしトークンを取得します。
            disconnected_event_handler(Optional[iscp.DisconnectedEventHandler]): 切断イベントのハンドラ
        Returns:
            iscp.Conn: iSCPコネクション

        """
        # TODO: JSONサポート
        if isinstance(encoding, str):
            encoding = EncodingName.parse(encoding)

        tr = await connector.connect(address, NegotiationParams(enc=encoding))
        if isinstance(project_uuid, str):
            project_uuid = UUID(project_uuid)

        res = cls(
            transport=tr,
            node_id=node_id,
            ping_interval=ping_interval,
            ping_timeout=ping_timeout,
            project_uuid=project_uuid,
            token_source=token_source,
            disconnected_event_handler=disconnected_event_handler,
        )
        return await res._open()

    def __init__(
        self,
        transport: Transport,
        *,
        node_id: Optional[str] = None,
        protocol_version: str = "2.0.0",
        ping_interval: float = DEFAULT_PING_INTERVAL,
        ping_timeout: float = DEFAULT_PING_TIMEOUT,
        project_uuid: Optional[UUID] = None,
        token_source: Optional[TokenSource] = None,
        disconnected_event_handler: Optional[DisconnectedEventHandler] = None,
    ):
        self._transport = transport
        self._unreliable_writer: Optional[Writer] = None
        self._unreliable_reader: Optional[Reader] = None
        if isinstance(self._transport, Unreliable):
            wr, rd = self._transport.get_unreliable()
            self._unreliable_writer: Optional[Writer] = wr
            self._unreliable_reader: Optional[Reader] = rd

        self._protocol_version = protocol_version
        self._node_id = node_id
        self._ping_timeout = ping_timeout
        self._ping_interval = ping_interval
        self._req_sequence = Sequence.for_request_id()
        self._stream_sequence = Sequence.for_stream_id()
        self._project_uuid = project_uuid
        self._token_source = token_source

        # Event
        self._called_close_event = asyncio.Event()
        self._closed = asyncio.Event()

        # Read queue
        self._downstream_call_queue: asyncio.Queue[Optional[DownstreamCall]] = asyncio.Queue(256)
        self._downstream_reply_queue: asyncio.Queue[Optional[DownstreamCall]] = asyncio.Queue(256)

        # Request callback queues
        self._request_callback_queues: Dict[int, asyncio.Queue[message.RequestMessage]] = {}
        self._upstream_call_callback_queues: Dict[str, asyncio.Queue[message.UpstreamCallAck]] = {}
        self._downstream_reply_callback_queues: Dict[str, asyncio.Queue[_model.DownstreamReplyCall]] = {}

        # StreamHolder
        self._upstreams: Dict[int, Upstream] = {}
        self._downstreams: Dict[int, Downstream] = {}
        self._metadata_downstreams: Dict[str, Dict[int, Downstream]] = defaultdict(lambda: {})  # source_node_id and downstreams

        # All tasks
        # cancel everything on close
        self._all_tasks: List[asyncio.Task] = []

        self._encoding: Encoding = Protobuf()
        self._disconnected_handler = disconnected_event_handler

        self._internal_error: Optional[ISCPException] = None

    async def __aenter__(self):
        return self

    @property
    def node_id(self):
        """
        ノードIDを取得します。

        Returns:
            Optional[str]: ノードID
        """
        return self._node_id

    @property
    def ping_interval(self):
        """
        Ping間隔（秒）を取得します。

        Returns:
            float: Ping間隔（秒）
        """
        return self._ping_interval

    @property
    def ping_timeout(self):
        """
        Pingタイムアウト（秒）を取得します。

        Returns:
            float: Pingタイムアウト（秒）

        """
        return self._ping_timeout

    @property
    def project_uuid(self):
        """
        プロジェクトUUIDを取得します。

        Returns:
            Optional[UUID]: プロジェクトUUID
        """
        return self._project_uuid

    @property
    def address(self):
        """
        アドレスを取得します。

        Returns:
            str: アドレス
        """
        return self._transport.address()

    @property
    def encoding(self):
        """
        エンコーディング名を取得します。

        Returns:
            iscp.EncodingName: エンコーディング名
        """
        return self._encoding.name()

    @property
    def transport(self):
        """
        トランスポート名を取得します。

        Returns:
            iscp.TransportName: トランスポート名
        """
        return self._transport.name()

    async def _open(self):
        negotiation_params = self._transport.negotiation_params()
        if negotiation_params.enc == EncodingName.PROTOBUF:
            self._encoding: Encoding = Protobuf()
        else:
            self._encoding: Encoding = Protobuf()

        resp = await self._wait_for_connected()

        if resp.result_code != message.ResultCode.SUCCEEDED:
            raise ISCPFailedMessageError(received_message=resp, message=f"code=[{resp.result_code}] msg=[{resp.result_string}]")

        asyncio.create_task(self._wait_called_close_then_close())
        asyncio.create_task(self._wait_closed_for_event_handler())

        self._start()
        return self

    def _start(self):
        # transport read loop
        self._all_tasks.append(asyncio.create_task(self._read_loop()))
        if self._unreliable_reader:
            self._all_tasks.append(asyncio.create_task(self._unreliable_read_loop(self._unreliable_reader)))

        # keep alive loop
        self._all_tasks.append(asyncio.create_task(self._keep_alive_loop()))

    async def _stop(self):
        for t in self._all_tasks:
            t.cancel()

        with suppress(CancelledError):
            await asyncio.wait(self._all_tasks)

    async def _unreliable_read_loop(self, reader: Reader):
        while not self._called_close_event.is_set():
            msg = await self._encoding.decodeFrom(reader)

            # dispatch
            if isinstance(msg, DownstreamChunk):
                await self._downstreams[msg.stream_id_alias]._handle_chunk(msg)

    async def _read_loop(self):
        while not self._called_close_event.is_set():
            await asyncio.sleep(0)
            msg = await self._read()

            # dispatch
            if isinstance(msg, message.Ping):
                await self._write(
                    message.Pong(
                        request_id=msg.request_id,
                        extension_fields=message.PongExtensionFields(),
                    )
                )
            elif isinstance(msg, DownstreamChunk):
                await self._downstreams[msg.stream_id_alias]._handle_chunk(msg)
            elif isinstance(msg, DownstreamMetadata):
                if msg.stream_id_alias in self._metadata_downstreams[msg.source_node_id]:
                    await self._metadata_downstreams[msg.source_node_id][msg.stream_id_alias]._handle_metadata(msg)
            elif isinstance(msg, message.DownstreamChunkAckComplete):
                (
                    await self._downstreams[msg.stream_id_alias]._handle_chunk_ack_complete(msg)
                    if msg.stream_id_alias in self._downstreams
                    else None
                )
            elif isinstance(msg, message.UpstreamChunkAck):
                await self._upstreams[msg.stream_id_alias]._handle_ack(msg) if msg.stream_id_alias in self._upstreams else None
            elif isinstance(msg, DownstreamCall):
                if msg.request_call_id == "":
                    await self._downstream_call_queue.put(msg)
                elif msg.request_call_id in self._downstream_reply_callback_queues:
                    await self._downstream_reply_queue.put(msg)
                    await self._downstream_reply_callback_queues[msg.request_call_id].put(
                        _model.DownstreamReplyCall(
                            call_id=msg.call_id,
                            name=msg.name,
                            payload=msg.payload,
                            request_call_id=msg.request_call_id,
                            source_node_id=msg.source_node_id,
                            type=msg.type,
                        )
                    )
            elif isinstance(msg, message.UpstreamCallAck):
                if msg.call_id in self._upstream_call_callback_queues:
                    await self._upstream_call_callback_queues[msg.call_id].put(msg)
            elif isinstance(msg, message.RequestMessage):
                reply_queue = self._request_callback_queues[msg.request_id]
                if reply_queue is None:
                    continue
                await reply_queue.put(msg)
                del self._request_callback_queues[msg.request_id]
            else:
                logger.error(f"received unrecognized message[{msg}]")
                await self.close()
                return

    async def _wait_closed_for_event_handler(self):
        await self._closed.wait()
        if self._disconnected_handler:
            self._disconnected_handler(DisconnectedEvent(error=self._internal_error))

    async def _wait_called_close_then_close(self):
        await self._called_close_event.wait()
        await self._close()

    async def _send_request(self, msg: message.RequestMessage) -> message.RequestMessage:
        """リクエストメッセージを送信します。

        Args:
            msg (iscp.RequestMessage): リクエスト・メッセージ。msg内のrequest_id属性は必ず上書きされます。
        Returns:
            iscp.RequestMessage: 要求に対する応答メッセージ

        """
        if self._called_close_event.is_set():
            raise ISCPTransportClosedError()

        msg.request_id = self._req_sequence()
        reply_queue = asyncio.Queue(maxsize=1)
        self._request_callback_queues[msg.request_id] = reply_queue

        await self._write(msg)

        res = await reply_queue.get()
        reply_queue.task_done()
        return res

    async def _send_upstream_chunk(self, msg: message.UpstreamChunk) -> None:
        await self._write(msg)

    async def _send_upstream_chunk_unreliable(self, msg: message.UpstreamChunk) -> None:
        if self._unreliable_writer:
            await self._encoding.encodeTo(self._unreliable_writer, msg)
            return
        # fallback
        await self._send_upstream_chunk(msg)

    async def _keep_alive_loop(self):
        try:
            async with Ticker.of(self._ping_interval) as ticker:
                async for _ in ticker():
                    pong = await asyncio.wait_for(
                        self._send_request(
                            message.Ping(request_id=0, extension_fields=message.PingExtensionFields()),
                        ),
                        timeout=self._ping_timeout,
                    )
                    logger.debug(f"received pong timeout[{pong.request_id}]")
                    if self._called_close_event.is_set():
                        return

        except asyncio.TimeoutError:
            logger.error(f"ping pong timeout[{self._ping_timeout}]")
            self._internal_error = ISCPException(message="ping pong timeout")
            self._called_close_event.set()
            return
        except Exception as e:
            logger.error(e)

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def _wait_for_connected(self) -> message.ConnectResponse:
        req = message.ConnectRequest(
            request_id=self._req_sequence(),
            node_id=self._node_id if self._node_id else "",
            protocol_version=self._protocol_version,
            ping_interval=self._ping_interval,
            ping_timeout=self._ping_timeout,
            extension_fields=message.ConnectRequestExtensionFields(
                access_token=self._token_source() if self._token_source else "",
                intdash=message.IntdashExtensionFields(
                    project_uuid=self._project_uuid or UUID("00000000-0000-0000-0000-000000000000")
                ),
            ),
        )

        req.extension_fields.access_token = self._token_source() if self._token_source else ""
        req.extension_fields.intdash.project_uuid = (
            self._project_uuid if self._project_uuid else UUID("00000000-0000-0000-0000-000000000000")
        )

        await self._write(req)
        resp = await self._read()

        if isinstance(resp, message.ConnectResponse):
            return resp
        else:
            raise ISCPFailedMessageError(received_message=resp)

    async def open_upstream(
        self,
        session_id: str,
        *,
        expiry_interval: float = 1,
        data_ids: Optional[List[message.DataID]] = None,
        qos: message.QoS | str = message.QoS.UNRELIABLE,
        ack_interval: float = 1,
        persist: bool = False,
        send_data_points_callback: Optional[BeforeSendDataPointsCallback] = None,
        receive_ack_callback: Optional[AfterReceiveAckCallback] = None,
        flush_policy: FlushPolicy = DEFAULT_FLUSH_POLICY,
        close_timeout: float = 1,
        closed_event_handler: Optional[UpstreamClosedEventHandler] = None,
        close_session: bool = False,
    ) -> Upstream:
        """
        アップストリームを開きます。

        Args:
            session_id (str): セッションID
            expiry_interval (float):  有効期限（秒）
            data_ids (Optional[List[iscp.DataID]]):  データIDのリスト
            qos (iscp.QoS|str): QoS
            ack_interval (float): Ack返却間隔（秒）
            persist (bool):  永続化するかどうか
            send_data_points_callback (Optional[iscp.BeforeSendDataPointsCallback]):  データポイント送信時のフック
            receive_ack_callback (Optional[iscp.AfterReceiveAckCallback]):  Ack受信時のフック
            flush_policy (iscp.FlushPolicy): データポイントのフラッシュポリシー
            close_timeout (float): クローズのタイムアウト（秒）
            closed_event_handler (Optional[iscp.UpstreamClosedEventHandler]): アップストリームクローズイベントのハンドラ
            close_session(bool): アップストリームクローズ時にセッションをクローズするかどうか
        """
        if data_ids is None:
            data_ids = []

        if isinstance(qos, str):
            qos = message.QoS.parse(qos)

        resp = await self._send_request(
            message.UpstreamOpenRequest(
                request_id=0,
                session_id=session_id or "",
                expiry_interval=expiry_interval,
                data_ids=data_ids,
                qos=qos,
                ack_interval=ack_interval,
                extension_fields=message.UpstreamOpenRequestExtensionFields(persist=persist),
            )
        )

        if isinstance(resp, message.UpstreamOpenResponse):
            if resp.result_code is not message.ResultCode.SUCCEEDED:
                raise ISCPFailedMessageError(
                    received_message=resp, message=f"code=[{resp.result_code}] msg=[{resp.result_string}]"
                )

            up = Upstream(
                id=resp.assigned_stream_id,
                id_alias=resp.assigned_stream_id_alias,
                data_id_aliases=resp.data_id_aliases,
                server_time=resp.server_time,
                requester=self._send_request,
                sender=(
                    self._send_upstream_chunk_unreliable
                    if qos is message.QoS.UNRELIABLE and self._unreliable_writer
                    else self._send_upstream_chunk
                ),
                receive_ack_callback=receive_ack_callback,
                send_data_point_callback=send_data_points_callback,
                close_timeout=close_timeout,
                session_id=session_id or "",
                ack_interval=ack_interval,
                expiry_interval=expiry_interval,
                flush_policy=flush_policy,
                qos=qos,
                persist=persist,
                closed_event_handler=closed_event_handler,
                close_session=close_session,
            )
            await up._start()
            self._upstreams[up._id_alias] = up
            self._all_tasks.append(asyncio.create_task(self._remove_upstream_when_closed(up)))
            return up

        raise ISCPFailedMessageError(received_message=resp)

    async def _remove_upstream_when_closed(self, up: Upstream):
        await up._closed.wait()
        del self._upstreams[up._id_alias]

    async def open_downstream(
        self,
        filters: List[message.DownstreamFilter],
        *,
        data_ids: Optional[List[message.DataID]] = None,
        qos: message.QoS | str = message.QoS.UNRELIABLE,
        expiry_interval: float = 1,
        ack_interval: float = 1,
        closed_event_handler: Optional[DownstreamClosedEventHandler] = None,
        omit_empty_chunk=False,
    ) -> Downstream:
        """

        ダウンストリームを開きます。

        Args:
            filters (List[iscp.DownstreamFilter]): ダウンストリームフィルタのリスト
            data_ids (Optional[List[iscp.DataID]]): データIDのリスト
            qos (iscp.QoS|str): QoS
            expiry_interval (float): 有効期限（秒）
            ack_interval (float): Ack返却間隔（秒）
            closed_event_handler (Optional[iscp.DownstreamClosedEventHandler]): ダウンストリームクローズイベントのハンドラ
            omit_empty_chunk (bool): 空チャンク省略フラグ。Trueにすると空のDataPointGroupのチャンクはサーバーから配信されません。
        Returns:
            iscp.Downstream: ダウンストリーム
        """

        stream_id_alias = self._stream_sequence()
        data_id_alias_sequence = Sequence.for_data_id_alias()
        if isinstance(qos, str):
            qos = message.QoS.parse(qos)
        req = message.DownstreamOpenRequest(
            request_id=0,
            desired_stream_id_alias=stream_id_alias,
            downstream_filters=filters,
            expiry_interval=expiry_interval,
            data_id_aliases={} if data_ids is None else {data_id_alias_sequence(): v for v in data_ids},
            qos=qos,
            extension_fields=message.DownstreamOpenRequestExtensionFields(),
            omit_empty_chunk=omit_empty_chunk,
        )
        resp = await self._send_request(req)

        if isinstance(resp, message.DownstreamOpenResponse):
            if resp.result_code is not message.ResultCode.SUCCEEDED:
                raise ISCPFailedMessageError(
                    received_message=resp, message=f"code=[{resp.result_code}] msg=[{resp.result_string}]"
                )

            down = Downstream(
                id_alias=stream_id_alias,
                id=resp.assigned_stream_id,
                server_time=resp.server_time,
                filters=[],
                requester=self._send_request,
                expiry_interval=expiry_interval,
                stream_message_sender=self._write,
                request_message_sender=self._write,
                qos=qos,
                data_id_alias_sequence=data_id_alias_sequence,
                data_id_aliases=req.data_id_aliases,
                closed_event_handler=closed_event_handler,
                ack_interval=ack_interval,
            )
            self._downstreams[stream_id_alias] = down
            self._all_tasks.append(asyncio.create_task(self._remove_downstream_when_closed(down)))
            for f in filters:
                self._metadata_downstreams[f.source_node_id][stream_id_alias] = down

            await down._start()
            return down

        raise ISCPFailedMessageError(received_message=resp)

    async def _remove_downstream_when_closed(self, down: Downstream):
        await down._is_closed.wait()
        del self._downstreams[down._stream_id_alias]

    async def _write(self, msg: message.Message):
        await self._encoding.encodeTo(self._transport, msg)

    async def _read(self) -> message.Message:
        return await self._encoding.decodeFrom(self._transport)

    async def close(self):
        """
        コネクションを閉じます。
        """
        self._called_close_event.set()
        await self._closed.wait()

    async def _close(self):
        if self._closed.is_set():
            return
        try:
            await self._write(
                message.Disconnect(
                    result_code=message.ResultCode.NORMAL_CLOSURE,
                    result_string="NORMAL_CLOSURE",
                )
            )
            await self._stop()
            await self._transport.close()
        except Exception as e:
            logger.error(e)
        finally:
            self._closed.set()

    async def send_reply_call(self, reply_call: _model.UpstreamReplyCall) -> str:
        """
        E2Eコールのリプライを送信します。

        Args:
            reply_call(iscp.UpstreamReplyCall): アップストリームリプライコール

        Returns:
            str: コールID

        """
        call_id = _random_string()
        await self._send_call(
            message.UpstreamCall(
                call_id=call_id,
                destination_node_id=reply_call.destination_node_id,
                name=reply_call.name,
                type=reply_call.type,
                payload=reply_call.payload,
                request_call_id=reply_call.request_call_id,
                extension_fields=message.UpstreamCallExtensionFields(),
            )
        )
        return call_id

    async def send_call(self, upstream_call: _model.UpstreamCall) -> str:
        """
        E2Eコールを送信します。

        Args:
            upstream_call(iscp.UpstreamCall): アップストリームコール

        Returns:
            str: コールID

        """
        call_id = _random_string()
        await self._send_call(
            message.UpstreamCall(
                call_id=call_id,
                request_call_id="",
                destination_node_id=upstream_call.destination_node_id,
                name=upstream_call.name,
                type=upstream_call.type,
                payload=upstream_call.payload,
                extension_fields=message.UpstreamCallExtensionFields(),
            )
        )
        return call_id

    async def _send_call(self, upstream_call: message.UpstreamCall):
        self._upstream_call_callback_queues[upstream_call.call_id] = asyncio.Queue(1)
        await self._write(upstream_call)
        resp = await self._upstream_call_callback_queues[upstream_call.call_id].get()
        if resp.result_code is not message.ResultCode.SUCCEEDED:
            raise ISCPFailedMessageError(received_message=resp, message=f"code=[{resp.result_code}] msg=[{resp.result_string}]")

    async def calls(self, *, timeout: Optional[float] = None) -> AsyncIterator[_model.DownstreamCall]:
        """
        E2Eコールを受信します。

        Args:
            timeout (Optional[float]): 読み込みタイムアウト（秒）。指定しない場合はタイムアウトしません。

        Yields:
            iscp.DownstreamCall: ダウンストリームコール

        Examples:
            >>> async for call in conn.calls():
                  pass

        """
        while True:
            res = await asyncio.wait_for(self._downstream_call_queue.get(), timeout=timeout)
            self._downstream_call_queue.task_done()
            if not res:
                return
            yield _model.DownstreamCall(
                call_id=res.call_id,
                source_node_id=res.source_node_id,
                name=res.name,
                type=res.type,
                payload=res.payload,
            )

    async def reply_calls(self, *, timeout: Optional[float] = None) -> AsyncIterator[_model.DownstreamReplyCall]:
        """
        E2Eリプライコールを受信します。

        Args:
            timeout (Optional[float]): 読み込みタイムアウト（秒）。指定しない場合はタイムアウトしません。

        Yields:
            iscp.DownstreamReplyCall: ダウンストリームリプライコール

        Examples:
            >>> async for call in conn.reply_calls():
                  pass

        """
        while True:
            res = await asyncio.wait_for(self._downstream_reply_queue.get(), timeout=timeout)
            self._downstream_reply_queue.task_done()
            if not res:
                return
            yield _model.DownstreamReplyCall(
                call_id=res.call_id,
                request_call_id=res.request_call_id,
                source_node_id=res.source_node_id,
                name=res.name,
                type=res.type,
                payload=res.payload,
            )

    @contextmanager
    def _subscribe_reply_call(
        self,
    ) -> Generator[tuple[str, Awaitable[_model.DownstreamReplyCall]], None, None]:
        """
        リプライコールをサブスクライブします。

        Args:
            request_call_id (str): サブスクライブするリクエストコールID

        Yields:
            Awaitable[iscp.DownstreamCall]: ダウンストリームコールのAwaitableオブジェクト

        Examples:
            >>> with conn.subscribe_reply_call() as (call_id, aw):
                  conn.send_call(...) # ここでcall_idを利用して下さい。
                  reply_call = await aw

        """
        call_id = _random_string()
        self._downstream_reply_callback_queues[call_id] = asyncio.Queue(1)
        try:
            yield (call_id, asyncio.create_task(self._downstream_reply_callback_queues[call_id].get()))
        finally:
            self._unsubscribe_reply_call(call_id)

    def _unsubscribe_reply_call(
        self,
        request_call_id: str,
    ):
        del self._downstream_reply_callback_queues[request_call_id]

    async def send_call_and_wait_reply_call(self, upstream_call: _model.UpstreamCall) -> _model.DownstreamReplyCall:
        """
        E2Eコールを送信し、リプライコールを受信するまで待ちます。

        Args:
            upstream_call(iscp.UpstreamCall): アップストリームコール

        Returns:
            iscp.DownstreamReplyCall: ダウンストリームリプライコール

        """
        # start

        with self._subscribe_reply_call() as (call_id, fut):
            await self._send_call(
                message.UpstreamCall(
                    call_id=call_id,
                    request_call_id="",
                    destination_node_id=upstream_call.destination_node_id,
                    name=upstream_call.name,
                    type=upstream_call.type,
                    payload=upstream_call.payload,
                    extension_fields=message.UpstreamCallExtensionFields(),
                )
            )
            got = await fut
            return _model.DownstreamReplyCall(
                call_id=got.call_id,
                name=got.name,
                type=got.type,
                payload=got.payload,
                request_call_id=got.request_call_id,
                source_node_id=got.source_node_id,
            )

    async def send_base_time(
        self,
        base_time: message.BaseTime,
        *,
        persist: bool = False,
    ):
        """
        基準時刻を送信します。

        Args:
            base_time(iscp.BaseTime):  基準時刻
            persist (bool): 永続化するかどうか

        """
        return await self._send_metadata(metadata=base_time, persist=persist)

    async def _send_metadata(
        self,
        metadata: message.SendableMetadata,
        *,
        persist: bool = False,
    ):
        """
        メタデータを送信します。

        Args:
            base_time(iscp.SendableMetadata):  メタデータ
            persist (bool): 永続化するかどうか

        """
        # reply
        msg = await self._send_request(
            message.UpstreamMetadata(
                request_id=0,
                metadata=metadata,
                extension_fields=message.UpstreamMetadataExtensionFields(persist=persist),
            )
        )
        if isinstance(msg, message.UpstreamMetadataAck):
            if msg.result_code is message.ResultCode.SUCCEEDED:
                return

            raise ISCPFailedMessageError(received_message=msg, message=f"code=[{msg.result_code}] msg=[{msg.result_string}]")

        raise ISCPFailedMessageError(received_message=msg)


def _random_string() -> str:
    return uuid.uuid4().__str__()
