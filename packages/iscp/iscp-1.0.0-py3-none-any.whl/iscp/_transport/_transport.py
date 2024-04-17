from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Tuple

from ._negotiation_params import NegotiationParams

__all__ = ["Writer", "Reader", "Transport", "Unreliable", "Connector", "TransportName"]


class TransportName(str, Enum):
    """
    トランスポートのの名前です。
    """

    WEBSOCKET = "websocket"
    """WebSocket"""

    QUIC = "quic"
    """QUIC"""

    @classmethod
    def parse(cls, arg: str):
        pass
        lower = arg.lower()
        if lower == cls.WEBSOCKET:
            return cls.WEBSOCKET
        if lower == cls.QUIC:
            return cls.QUIC
        raise ValueError(f"unrecognized transport name {arg}")


class Writer(metaclass=ABCMeta):
    """
    iSCPメッセージのWriterインターフェースです。
    """

    @abstractmethod
    async def write(self, bytes):
        """
        iSCPの1メッセージ分を書き込みます。
        """
        pass


class Reader(metaclass=ABCMeta):
    """
    iSCPメッセージのReaderインターフェースです。
    """

    @abstractmethod
    async def read(self) -> bytes:
        """
        iSCPの1メッセージ分を読み込みます。
        """
        pass


class Transport(Writer, Reader, metaclass=ABCMeta):
    """
    iSCPのトランスポートインターフェースです。
    """

    @abstractmethod
    async def close(self):
        """
        トランスポートを閉じます。
        """
        pass

    @abstractmethod
    def negotiation_params(self) -> NegotiationParams:
        """
        ネゴシエーションパラメータを取得します。

        Returns:
            iscp.NegotiationParams: ネゴシエーションパラメータ
        """
        pass

    @abstractmethod
    def address(self) -> str:
        """
        接続先アドレスを取得します。

        Returns:
            str: 接続先アドレス
        """
        pass

    @abstractmethod
    def name(self) -> TransportName:
        """
        トランスポートの名前を取得します。

        Returns:
            iscp.TransportName: トランスポートの名前
        """
        pass


class Unreliable(metaclass=ABCMeta):
    @abstractmethod
    def get_unreliable(self) -> Tuple[Writer, Reader]:
        pass


class Connector(metaclass=ABCMeta):
    """
    iSCPコネクターのインターフェースです。
    """

    @abstractmethod
    async def connect(self, address: str, negotiation_params: NegotiationParams) -> Transport:
        """
        iSCPを使って接続します。

        Args:
            address(str): 接続先のアドレス。`127.0.0.1:8080` 形式。
            negotiation_params(iscp.NegotiationParams): ネゴシエーションパラメータ

        Returns:
            iscp.Transport: iSCPのトランスポート
        """
        pass
