__all__ = [
    "ISCPException",
    "ISCPTransportClosedError",
    "ISCPFailedMessageError",
    "ISCPMalformedMessageError",
    "ISCPUnexpectedError",
]


from dataclasses import dataclass
from typing import Optional

from .. import _message as message


@dataclass
class ISCPException(Exception):
    """
    iSCPモジュールで定義されている例外の基底クラスです。

    Attributes:
        message(Optional[str]): 例外メッセージです。
    """

    message: Optional[str] = None


@dataclass
class ISCPUnexpectedError(ISCPException):
    """
    予期しない例外です。
    """


@dataclass
class ISCPTransportClosedError(ISCPException):
    """
    トランスポートが閉じられている状態でトランスポートへの読み書きをした場合に送出される例外です。
    """


@dataclass
class ISCPMalformedMessageError(ISCPException):
    """
    メッセージのエンコードやデコードに失敗した時に送出される例外です。
    """


@dataclass
class ISCPFailedMessageError(ISCPException):
    """
    iSCPでの通信中に、失敗を意味する結果コードが含まれたメッセージを受信した場合に送出される例外です。

    Attributes:
        received_message(iscp.Message): 受信メッセージ
        message(Optional[str]): エラーメッセージ
    """

    def __init__(self, received_message: message.Message, message: Optional[str] = None):
        super().__init__(message)
        self.received_message = received_message
