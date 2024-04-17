__all__ = ["Message"]


import dataclasses

__all__ = ["Message", "RequestMessage", "StreamMessage"]


@dataclasses.dataclass
class Message(object):
    pass


@dataclasses.dataclass
class RequestMessage(Message):
    request_id: int


@dataclasses.dataclass
class StreamMessage(Message):
    stream_id_alias: int
