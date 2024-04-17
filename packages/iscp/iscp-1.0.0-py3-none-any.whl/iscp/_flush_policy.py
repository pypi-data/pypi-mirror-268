from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Optional

from ._ticker import Ticker

__all__ = [
    "FlushPolicy",
    "Immediately",
    "IntervalOnly",
    "BufferSizeOnly",
    "IntervalOrBufferSize",
    "NoFlush",
]

_DEFAULT_BUFFER_SIZE = 100_000
_DEFAULT_INTERVAL = 1.0


class FlushPolicy(metaclass=ABCMeta):
    """
    Upstreamのフラッシュの方法について定義します。
    """

    @abstractmethod
    def IsFlush(self, size: int) -> bool:
        """
        内部バッファのサイズからフラッシュするかどうかを判定します。

        Args:
            size(int): 内部バッファサイズ

        Returns:
            bool: フラッシュするかどうか。
        """
        pass

    @abstractmethod
    def Ticker(self) -> Optional[Ticker]:
        """
        時間間隔によるフラッシュを行うためのTickerを取得します。

        Tickerが時間を返す度にフラッシュを行います。Noneの場合は時間間隔によるフラッシュを行いません。

        Returns:
            Optional[Ticker]: Ticker
        """
        pass


class Immediately(FlushPolicy):
    """
    即時フラッシュを行うFlushPolicyです。
    """

    def IsFlush(self, _: int) -> bool:
        return True

    def Ticker(self) -> Optional[Ticker]:
        return None


class IntervalOnly(FlushPolicy):
    """
    インターバルによるフラッシュを行うFlushPolicyです。

    Attributes:
        interval(float): フラッシュインターバル（秒）
    """

    def __init__(self, interval: float = _DEFAULT_INTERVAL):
        self._interval = interval
        self._next_flushed_at: Optional[datetime] = None

    def IsFlush(self, _: int) -> bool:
        return False

    def Ticker(self) -> Optional[Ticker]:
        return Ticker(delay=self._interval)


class IntervalOrBufferSize(FlushPolicy):
    """
    インターバル、またはバッファサイズによるフラッシュを行うFlushPolicyです。

    Attributes:
        buffer_size(int): バッファサイズ
        interval(float): フラッシュインターバル（秒）
    """

    def __init__(self, buffer_size: int = _DEFAULT_BUFFER_SIZE, interval: float = _DEFAULT_INTERVAL):
        self._interval_only = IntervalOnly(interval=interval)
        self._buffer_size_only = BufferSizeOnly(buffer_size=buffer_size)

    def IsFlush(self, size: int) -> bool:
        return self._buffer_size_only.IsFlush(size)

    def Ticker(self) -> Optional[Ticker]:
        return self._interval_only.Ticker()


class BufferSizeOnly(FlushPolicy):
    """
    バッファサイズによるフラッシュを行うFlushPolicyです。

    Attributes:
        buffer_size(int): バッファサイズ
    """

    def __init__(self, buffer_size: int = _DEFAULT_BUFFER_SIZE):
        self._buffer_size = buffer_size

    def IsFlush(self, size: int) -> bool:
        return self._buffer_size < size

    def Ticker(self) -> Optional[Ticker]:
        return None


class NoFlush(FlushPolicy):
    """
    フラッシュを行わないFlushPolicyです。このFlushPolicyを指定した場合は、明示的にフラッシュを行う必要があります。
    """

    def IsFlush(self, _: int) -> bool:
        return False

    def Ticker(self) -> Optional[Ticker]:
        return None
