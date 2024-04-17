__all__ = ["WireToProto", "ProtoToWire"]


from iscp._encoding._codegen.iscp2.v1.extensions.ping_pong_pb2 import (
    PingExtensionFields as PingExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.ping_pong_pb2 import (
    PongExtensionFields as PongExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.ping_pong_pb2 import Ping as PingPB
from iscp._encoding._codegen.iscp2.v1.ping_pong_pb2 import Pong as PongPB
from iscp._message import Ping, PingExtensionFields, Pong, PongExtensionFields


class WireToProto(object):
    @classmethod
    def ping_extension_fields(cls, _: PingExtensionFields) -> PingExtensionFieldsPB:
        return PingExtensionFieldsPB()

    @classmethod
    def pong_extension_fields(cls, _: PongExtensionFields) -> PongExtensionFieldsPB:
        return PongExtensionFieldsPB()

    @classmethod
    def ping(cls, arg: Ping) -> PingPB:
        res = PingPB()
        res.request_id = arg.request_id
        res.extension_fields.CopyFrom(cls.ping_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def pong(cls, arg: Pong) -> PongPB:
        res = PongPB()
        res.request_id = arg.request_id
        res.extension_fields.CopyFrom(cls.pong_extension_fields(arg.extension_fields))
        return res


class ProtoToWire(object):
    @classmethod
    def ping_extension_fields(cls, _: PingExtensionFieldsPB) -> PingExtensionFields:
        return PingExtensionFields()

    @classmethod
    def pong_extension_fields(cls, _: PongExtensionFieldsPB) -> PongExtensionFields:
        return PongExtensionFields()

    @classmethod
    def ping(cls, arg: PingPB) -> Ping:
        return Ping(
            request_id=arg.request_id,
            extension_fields=cls.ping_extension_fields(arg.extension_fields),
        )

    @classmethod
    def pong(cls, arg: PongPB) -> Pong:
        return Pong(
            request_id=arg.request_id,
            extension_fields=cls.pong_extension_fields(arg.extension_fields),
        )
