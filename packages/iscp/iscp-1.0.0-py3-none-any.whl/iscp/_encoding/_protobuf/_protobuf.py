# from ....iscp-proto.gen.pytnon.iscp2.v1.message_pbs import Message as MessagePB
# from ..._encoding.codegen.message_pb2 import Message as MessagePB
from ..._encoding._codegen.iscp2.v1.message_pb2 import Message as MessagePB
from ..._message import Message
from ..._transport._transport import Writer, Reader

from .._encoding import Encoding, EncodingName
from .converter import ProtoToWire, WireToProto
from ..._exceptions import ISCPMalformedMessageError

__all__ = ["Protobuf"]


class Protobuf(Encoding):
    async def encodeTo(self, writer: Writer, message: Message):
        await writer.write(self.to_bytes(message))

    async def decodeFrom(self, reader: Reader) -> Message:
        return self.from_bytes(await reader.read())

    def name(self) -> EncodingName:
        return EncodingName.PROTOBUF

    @staticmethod
    def to_bytes(msg: Message) -> bytes:
        try:
            return WireToProto.convert(msg).SerializeToString()  # type: ignore
        except Exception as e:
            raise ISCPMalformedMessageError from e

    @staticmethod
    def from_bytes(bs: bytes) -> Message:
        try:
            msg = MessagePB()
            msg.ParseFromString(bs)
            return ProtoToWire.convert(msg)
        except Exception as e:
            raise ISCPMalformedMessageError from e
