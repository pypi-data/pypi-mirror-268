from dataclasses import dataclass
from typing import Dict, List
from uuid import UUID

from ._common import DataID, DateTime, QoS, StreamChunk
from ._message import Message, RequestMessage
from ._metadata import BaseTime
from ._result_code import ResultCode

__all__ = [
    "UpstreamOpenRequestExtensionFields",
    "UpstreamOpenResponseExtensionFields",
    "UpstreamResumeRequestExtensionFields",
    "UpstreamResumeResponseExtensionFields",
    "UpstreamCloseRequestExtensionFields",
    "UpstreamCloseResponseExtensionFields",
    "UpstreamChunkExtensionFields",
    "UpstreamChunkAckExtensionFields",
    "UpstreamMetadataExtensionFields",
    "UpstreamMetadataAckExtensionFields",
    "UpstreamChunkResultExtensionFields",
    "UpstreamOpenRequest",
    "UpstreamOpenResponse",
    "UpstreamResumeRequest",
    "UpstreamMetadataAck",
    "UpstreamMetadata",
    "UpstreamChunkAck",
    "UpstreamChunkResult",
    "UpstreamChunk",
    "UpstreamCloseResponse",
    "UpstreamCloseRequest",
    "UpstreamResumeResponse",
    "SendableMetadata",
]

SendableMetadata = BaseTime


@dataclass
class UpstreamOpenRequestExtensionFields(object):
    persist: bool


@dataclass
class UpstreamOpenResponseExtensionFields(object):
    pass


@dataclass
class UpstreamResumeRequestExtensionFields(object):
    pass


@dataclass
class UpstreamResumeResponseExtensionFields(object):
    pass


@dataclass
class UpstreamCloseRequestExtensionFields(object):
    close_session: bool = False


@dataclass
class UpstreamCloseResponseExtensionFields(object):
    pass


@dataclass
class UpstreamChunkExtensionFields(object):
    """
    ストリームチャンク（上り用）に含まれる拡張フィールドです。
    """

    pass


@dataclass
class UpstreamChunkAckExtensionFields(object):
    """
    ストリームチャンク（上り用）に対する確認応答に含まれる拡張フィールドです。
    """

    pass


@dataclass
class UpstreamMetadataExtensionFields(object):
    persist: bool = False


@dataclass
class UpstreamMetadataAckExtensionFields(object):
    pass


@dataclass
class UpstreamChunkResultExtensionFields(object):
    """
    ストリームチャンク（上り用）の処理結果に含まれる拡張フィールドです。
    """

    pass


@dataclass
class UpstreamChunkResult(object):
    """
    ストリームチャンク（上り用）で送信されたデータポイントの処理結果です。

    Attributes:
        sequence_number(int): シーケンス番号
        result_code(iscp.ResultCode): 結果コード
        result_string(str): 結果文字列
        extension_fields(iscp.UpstreamChunkResultExtensionFields):  拡張フィールド
    """

    sequence_number: int
    result_code: ResultCode
    result_string: str
    extension_fields: UpstreamChunkResultExtensionFields


@dataclass
class UpstreamOpenRequest(RequestMessage):
    session_id: str
    request_id: int
    expiry_interval: float
    data_ids: List[DataID]
    qos: QoS
    ack_interval: float
    extension_fields: UpstreamOpenRequestExtensionFields


@dataclass
class UpstreamOpenResponse(RequestMessage):
    request_id: int
    assigned_stream_id: UUID
    assigned_stream_id_alias: int
    data_id_aliases: Dict[int, DataID]
    server_time: DateTime
    result_code: ResultCode
    result_string: str
    extension_fields: UpstreamOpenResponseExtensionFields


@dataclass
class UpstreamResumeRequest(RequestMessage):
    request_id: int
    stream_id: UUID
    extension_fields: UpstreamResumeRequestExtensionFields


@dataclass
class UpstreamResumeResponse(RequestMessage):
    request_id: int
    assigned_stream_id_alias: int
    result_code: ResultCode
    result_string: str
    extension_fields: UpstreamResumeResponseExtensionFields


@dataclass
class UpstreamCloseRequest(RequestMessage):
    request_id: int
    stream_id: UUID
    total_data_points: int
    final_sequence_number: int
    extension_fields: UpstreamCloseRequestExtensionFields


@dataclass
class UpstreamCloseResponse(RequestMessage):
    request_id: int
    result_code: ResultCode
    result_string: str
    extension_fields: UpstreamCloseResponseExtensionFields


@dataclass
class UpstreamChunk(Message):
    """
    ストリームチャンク（上り用）です。


    Attributes:
        stream_id_alias(int): ストリームIDエイリアス
        data_ids(List[iscp.DataID]): データIDのリスト
        stream_chunk(iscp.StreamChunk): ストリームチャンク
        extension_fields(iscp.UpstreamChunkExtensionFields) : 拡張フィールド
    """

    stream_id_alias: int
    stream_chunk: StreamChunk
    data_ids: List[DataID]
    extension_fields: UpstreamChunkExtensionFields


@dataclass
class UpstreamChunkAck(Message):
    """
    ストリームチャンク（上り用）に対する確認応答です。

    Attributes:
        stream_id_alias(int): ストリームIDエイリアス
        results(List[iscp.UpstreamChunkResult]): 処理結果のリスト
        data_id_aliases(Dict[int, iscp.DataID]): データIDエイリアス
        extension_fields(iscp.UpstreamChunkAckExtensionFields): 拡張フィールド
    """

    stream_id_alias: int
    results: List[UpstreamChunkResult]
    data_id_aliases: Dict[int, DataID]
    extension_fields: UpstreamChunkAckExtensionFields


@dataclass
class UpstreamMetadata(RequestMessage):
    """
    アップストリームメタデータです。
    メタデータを格納してノードからブローカーへ転送するためのメッセージです。

    Attributes:
        metadata(SendableMetadata): メタデータ
        extension_fields(iscp.UpstreamMetadataExtensionFields): 拡張フィールド
    """

    metadata: SendableMetadata
    extension_fields: UpstreamMetadataExtensionFields


@dataclass
class UpstreamMetadataAck(RequestMessage):
    result_code: ResultCode
    result_string: str
    extension_fields: UpstreamMetadataAckExtensionFields
