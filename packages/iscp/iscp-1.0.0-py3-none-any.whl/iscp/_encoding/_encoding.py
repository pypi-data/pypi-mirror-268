from abc import ABCMeta, abstractmethod

from iscp._message import Message
from iscp._transport._transport import Reader, Writer
from iscp._transport._negotiation_params import EncodingName

__all__ = ["Encoding"]

EncodingName = EncodingName


class Encoding(metaclass=ABCMeta):
    @abstractmethod
    async def encodeTo(self, writer: Writer, message: Message):
        pass

    @abstractmethod
    async def decodeFrom(self, reader: Reader) -> Message:
        pass

    @abstractmethod
    def name(self) -> EncodingName:
        pass
