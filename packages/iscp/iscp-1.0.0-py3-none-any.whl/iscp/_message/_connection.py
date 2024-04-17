from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from ._message import Message, RequestMessage
from ._result_code import ResultCode

__all__ = [
    "ConnectRequest",
    "ConnectRequestExtensionFields",
    "IntdashExtensionFields",
    "ConnectResponse",
    "ConnectResponseExtensionFields",
    "Disconnect",
    "DisconnectExtensionFields",
]


@dataclass
class IntdashExtensionFields(Message):
    project_uuid: Optional[UUID]


@dataclass
class ConnectRequestExtensionFields(Message):
    access_token: str  # アクセストークン
    intdash: IntdashExtensionFields


@dataclass
class ConnectResponseExtensionFields(Message):
    pass


@dataclass
class ConnectRequest(Message):
    request_id: int  # リクエストID
    node_id: str  # ノードID
    protocol_version: str  # プロトコルバージョン
    ping_interval: float  # Ping間隔秒数
    ping_timeout: float  # Pingタイムアウト秒数
    extension_fields: ConnectRequestExtensionFields = field(
        default_factory=lambda: ConnectRequestExtensionFields(
            access_token="",
            intdash=IntdashExtensionFields(project_uuid=UUID("00000000-0000-0000-0000-000000000000")),
        )
    )  # 拡張フィールド


@dataclass
class ConnectResponse(RequestMessage):
    request_id: int  # リクエストID
    protocol_version: str  # プロトコルバージョン
    result_code: ResultCode  # 結果コード
    result_string: str  # 結果文字列
    extension_fields: ConnectResponseExtensionFields = field(default_factory=lambda: ConnectResponseExtensionFields())  # 拡張フィールド


@dataclass
class DisconnectExtensionFields(Message):
    pass


@dataclass
class Disconnect(Message):
    result_code: ResultCode  # 結果コード
    result_string: str  # 結果文字列
    extension_fields: DisconnectExtensionFields = field(default_factory=lambda: DisconnectExtensionFields())  # 拡張フィールド
