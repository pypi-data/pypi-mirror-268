from dataclasses import dataclass

from ._message import RequestMessage

__all__ = ["PingExtensionFields", "PongExtensionFields", "Ping", "Pong"]


@dataclass
class PingExtensionFields(object):
    pass


@dataclass
class PongExtensionFields(object):
    pass


@dataclass
class Ping(RequestMessage):
    extension_fields: PingExtensionFields


@dataclass
class Pong(RequestMessage):
    extension_fields: PongExtensionFields
