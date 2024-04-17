from dataclasses import dataclass

from ._message import Message
from ._result_code import ResultCode

__all__ = [
    "UpstreamCallExtensionFields",
    "UpstreamCallAckExtensionFields",
    "DownstreamCallExtensionFields",
    "UpstreamCall",
    "UpstreamCallAck",
    "DownstreamCall",
]


@dataclass
class UpstreamCallExtensionFields(object):
    pass


@dataclass
class UpstreamCallAckExtensionFields(object):
    pass


@dataclass
class DownstreamCallExtensionFields(object):
    pass


@dataclass
class UpstreamCall(Message):
    call_id: str
    request_call_id: str
    destination_node_id: str
    name: str
    type: str
    payload: bytes
    extension_fields: UpstreamCallExtensionFields


@dataclass
class UpstreamCallAck(Message):
    call_id: str
    result_code: ResultCode
    result_string: str
    extension_fields: UpstreamCallAckExtensionFields


@dataclass
class DownstreamCall(Message):
    call_id: str
    request_call_id: str
    source_node_id: str
    name: str
    type: str
    payload: bytes
    extension_fields: DownstreamCallExtensionFields
