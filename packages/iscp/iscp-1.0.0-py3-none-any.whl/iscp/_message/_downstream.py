from dataclasses import dataclass
from typing import Dict, List
from uuid import UUID

from ._common import DataID, DateTime, DownstreamFilter, QoS, StreamChunk
from ._message import Message, RequestMessage, StreamMessage
from ._metadata import Metadata
from ._result_code import ResultCode

__all__ = [
    "UpstreamInfo",
    "DownstreamOpenRequestExtensionFields",
    "DownstreamOpenResponseExtensionFields",
    "DownstreamResumeRequestExtensionFields",
    "DownstreamResumeResponseExtensionFields",
    "DownstreamCloseRequestExtensionFields",
    "DownstreamCloseResponseExtensionFields",
    "DownstreamChunkExtensionFields",
    "DownstreamChunkAckExtensionFields",
    "DownstreamChunkAckCompleteExtensionFields",
    "DownstreamMetadataExtensionFields",
    "DownstreamMetadataAckExtensionFields",
    "DownstreamOpenResponse",
    "DownstreamMetadataAck",
    "DownstreamMetadata",
    "DownstreamChunk",
    "DownstreamChunkAck",
    "DownstreamChunkAckComplete",
    "DownstreamChunkResult",
    "DownstreamCloseRequest",
    "DownstreamCloseResponse",
    "DownstreamResumeRequest",
    "DownstreamResumeResponse",
    "DownstreamChunkResultExtensionFields",
    "DownstreamOpenRequest",
]


@dataclass(frozen=True)
class UpstreamInfo(object):
    """
    アップストリームの情報です。

    Attributes:
        session_id(str): セッションID
        stream_id: ストリームID
        source_node_id: 送信元ノードID
    """

    session_id: str
    stream_id: UUID
    source_node_id: str


@dataclass
class DownstreamOpenRequestExtensionFields(object):
    pass


@dataclass
class DownstreamOpenResponseExtensionFields(object):
    pass


@dataclass
class DownstreamResumeRequestExtensionFields(object):
    pass


@dataclass
class DownstreamResumeResponseExtensionFields(object):
    pass


@dataclass
class DownstreamCloseRequestExtensionFields(object):
    pass


@dataclass
class DownstreamCloseResponseExtensionFields(object):
    pass


@dataclass
class DownstreamChunkExtensionFields(object):
    pass


@dataclass
class DownstreamChunkAckExtensionFields(object):
    pass


@dataclass
class DownstreamChunkAckCompleteExtensionFields(object):
    pass


@dataclass
class DownstreamMetadataExtensionFields(object):
    pass


@dataclass
class DownstreamMetadataAckExtensionFields(object):
    pass


@dataclass
class DownstreamChunkResultExtensionFields(object):
    pass


@dataclass
class DownstreamChunkResult(object):
    stream_id_of_upstream: UUID
    sequence_number_in_upstream: int
    result_code: ResultCode
    result_string: str
    extension_fields: DownstreamChunkResultExtensionFields


@dataclass
class DownstreamOpenRequest(RequestMessage):
    desired_stream_id_alias: int
    downstream_filters: List[DownstreamFilter]
    expiry_interval: float
    data_id_aliases: Dict[int, DataID]
    qos: QoS
    extension_fields: DownstreamOpenRequestExtensionFields
    omit_empty_chunk: bool


@dataclass
class DownstreamOpenResponse(RequestMessage):
    assigned_stream_id: UUID
    server_time: DateTime
    result_code: ResultCode
    result_string: str
    extension_fields: DownstreamOpenResponseExtensionFields


@dataclass
class DownstreamResumeRequest(RequestMessage):
    request_id: int
    stream_id: UUID
    desired_stream_id_alias: int
    extension_fields: DownstreamResumeRequestExtensionFields


@dataclass
class DownstreamResumeResponse(RequestMessage):
    result_code: ResultCode
    result_string: str
    extension_fields: DownstreamResumeResponseExtensionFields


@dataclass
class DownstreamCloseRequest(RequestMessage):
    stream_id: UUID
    extension_fields: DownstreamCloseRequestExtensionFields


@dataclass
class DownstreamCloseResponse(RequestMessage):
    result_code: ResultCode
    result_string: str
    extension_fields: DownstreamCloseResponseExtensionFields


UpstreamOrAlias = UpstreamInfo | int


@dataclass
class DownstreamChunk(Message):
    stream_id_alias: int
    upstream_or_alias: UpstreamOrAlias
    stream_chunk: StreamChunk
    extension_fields: DownstreamChunkExtensionFields


@dataclass
class DownstreamChunkAck(StreamMessage):
    stream_id_alias: int
    ack_id: int
    results: List[DownstreamChunkResult]
    upstream_aliases: Dict[int, UpstreamInfo]
    data_id_aliases: Dict[int, DataID]
    extension_fields: DownstreamChunkAckExtensionFields


@dataclass
class DownstreamChunkAckComplete(Message):
    stream_id_alias: int
    ack_id: int
    result_code: ResultCode
    result_string: str
    extension_fields: DownstreamChunkAckCompleteExtensionFields


@dataclass
class DownstreamMetadata(Message):
    request_id: int
    stream_id_alias: int
    metadata: Metadata
    source_node_id: str
    extension_fields: DownstreamMetadataExtensionFields


@dataclass
class DownstreamMetadataAck(RequestMessage):
    request_id: int
    result_code: ResultCode
    result_string: str
    extension_fields: DownstreamMetadataAckExtensionFields
