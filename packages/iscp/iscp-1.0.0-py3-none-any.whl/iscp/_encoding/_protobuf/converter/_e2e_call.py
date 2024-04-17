__all__ = ["WireToProto", "ProtoToWire"]

from iscp._encoding._codegen.iscp2.v1.e2e_call_pb2 import DownstreamCall as DownstreamCallPB
from iscp._encoding._codegen.iscp2.v1.e2e_call_pb2 import UpstreamCall as UpstreamCallPB
from iscp._encoding._codegen.iscp2.v1.e2e_call_pb2 import UpstreamCallAck as UpstreamCallAckPB
from iscp._encoding._codegen.iscp2.v1.extensions.e2e_call_pb2 import (
    DownstreamCallExtensionFields as DownstreamCallExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.e2e_call_pb2 import (
    UpstreamCallAckExtensionFields as UpstreamCallAckExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.e2e_call_pb2 import (
    UpstreamCallExtensionFields as UpstreamCallExtensionFieldsPB,
)
from iscp._message import (
    DownstreamCallExtensionFields,
    UpstreamCall,
    UpstreamCallAck,
    UpstreamCallAckExtensionFields,
    UpstreamCallExtensionFields,
)

from iscp._message._e2e import (
    DownstreamCall,
)

from . import _result_code


class WireToProto(object):
    @classmethod
    def upstream_call_extension_fields(cls, arg: UpstreamCallExtensionFields) -> UpstreamCallExtensionFieldsPB:
        return UpstreamCallExtensionFieldsPB()

    @classmethod
    def upstream_call_ack_extension_fields(cls, arg: UpstreamCallAckExtensionFields) -> UpstreamCallAckExtensionFieldsPB:
        return UpstreamCallAckExtensionFieldsPB()

    @classmethod
    def downstream_call_extension_fields(cls, arg: DownstreamCallExtensionFields) -> DownstreamCallExtensionFieldsPB:
        return DownstreamCallExtensionFieldsPB()

    @classmethod
    def upstream_call(cls, arg: UpstreamCall) -> UpstreamCallPB:
        res = UpstreamCallPB()
        res.call_id = arg.call_id
        res.request_call_id = arg.request_call_id
        res.destination_node_id = arg.destination_node_id
        res.name = arg.name
        res.type = arg.type
        res.payload = arg.payload
        res.extension_fields.CopyFrom(cls.upstream_call_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_call_ack(cls, arg: UpstreamCallAck) -> UpstreamCallAckPB:
        res = UpstreamCallAckPB()
        res.call_id = arg.call_id
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.upstream_call_ack_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_call(cls, arg: DownstreamCall) -> DownstreamCallPB:
        res = DownstreamCallPB()
        res.call_id = arg.call_id
        res.request_call_id = arg.request_call_id
        res.source_node_id = arg.source_node_id
        res.name = arg.name
        res.type = arg.type
        res.payload = arg.payload
        res.extension_fields.CopyFrom(cls.downstream_call_extension_fields(arg.extension_fields))
        return res


class ProtoToWire(object):
    @classmethod
    def upstream_call_extension_fields(cls, _: UpstreamCallExtensionFieldsPB) -> UpstreamCallExtensionFields:
        return UpstreamCallExtensionFields()

    @classmethod
    def upstream_call_ack_extension_fields(cls, _: UpstreamCallAckExtensionFieldsPB) -> UpstreamCallAckExtensionFields:
        return UpstreamCallAckExtensionFields()

    @classmethod
    def downstream_call_extension_fields(cls, _: DownstreamCallExtensionFieldsPB) -> DownstreamCallExtensionFields:
        return DownstreamCallExtensionFields()

    @classmethod
    def upstream_call(cls, arg: UpstreamCallPB) -> UpstreamCall:
        return UpstreamCall(
            call_id=arg.call_id,
            request_call_id=arg.request_call_id,
            destination_node_id=arg.destination_node_id,
            name=arg.name,
            type=arg.type,
            payload=arg.payload,
            extension_fields=cls.upstream_call_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_call_ack(cls, arg: UpstreamCallAckPB) -> UpstreamCallAck:
        return UpstreamCallAck(
            call_id=arg.call_id,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.upstream_call_ack_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_call(cls, arg: DownstreamCallPB) -> DownstreamCall:
        return DownstreamCall(
            call_id=arg.call_id,
            request_call_id=arg.request_call_id,
            source_node_id=arg.source_node_id,
            name=arg.name,
            type=arg.type,
            payload=arg.payload,
            extension_fields=cls.downstream_call_extension_fields(arg.extension_fields),
        )
