from dataclasses import dataclass
from typing import List, Union
from uuid import UUID

from ._common import DateTime, DownstreamFilter, QoS

__all__ = [
    "Metadata",
    "BaseTime",
    "UpstreamOpen",
    "UpstreamAbnormalClose",
    "UpstreamResume",
    "UpstreamNormalClose",
    "DownstreamOpen",
    "DownstreamAbnormalClose",
    "DownstreamResume",
    "DownstreamNormalClose",
]


@dataclass
class BaseTime(object):
    """
    基準時刻です。

    Attributes:
        session_id(str): セッションID
        name(str): 名前
        priority(int): 優先度
        elapsed_time(int): 経過時間（ナノ秒）
        base_time(iscp.DateTime): 時刻
    """

    session_id: str
    name: str
    priority: int
    elapsed_time: int  # Nano秒
    base_time: DateTime


@dataclass
class UpstreamOpen(object):
    """
    あるアップストリームが開いたことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
        session_id(str): セッションID
        qos(iscp.QoS): QoS
    """

    stream_id: UUID
    session_id: str
    qos: QoS


@dataclass
class UpstreamAbnormalClose(object):
    """
    あるアップストリームが異常切断したことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
        session_id(str): セッションID
    """

    stream_id: UUID
    session_id: str


@dataclass
class UpstreamResume(object):
    """
    あるアップストリームが再開したことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
        session_id(str): セッションID
        qos(iscp.QoS): QoS
    """

    stream_id: UUID
    session_id: str
    qos: QoS


@dataclass
class UpstreamNormalClose(object):
    """
    あるアップストリームが正常切断したことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
        session_id(str): セッションID
        total_data_points(int): 総データポイント数
        final_sequence_number(int): 最終シーケンス番号
    """

    stream_id: UUID
    session_id: str
    total_data_points: int
    final_sequence_number: int


@dataclass
class DownstreamOpen(object):
    """
    あるダウンストリームが開いたことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
        downstream_filters(List[DownstreamFilter]): ダウンストリームフィルター
        qos(iscp.QoS): QoS
    """

    stream_id: UUID
    downstream_filters: List[DownstreamFilter]
    qos: QoS


@dataclass
class DownstreamAbnormalClose(object):
    """
    あるダウンストリームが異常切断したことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
    """

    stream_id: UUID


@dataclass
class DownstreamResume(object):
    """
    あるダウンストリームが再開したことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
        downstream_filters(List[DownstreamFilter]): ダウンストリームフィルター
        qos(iscp.QoS): QoS
    """

    stream_id: UUID
    downstream_filters: List[DownstreamFilter]
    qos: QoS


@dataclass
class DownstreamNormalClose(object):
    """
    あるダウンストリームが正常切断したことを知らせるメタデータです。

    Attributes:
        stream_id(UUID): ストリームID
    """

    stream_id: UUID


Metadata = Union[
    BaseTime,
    UpstreamOpen,
    UpstreamAbnormalClose,
    UpstreamResume,
    UpstreamNormalClose,
    DownstreamOpen,
    DownstreamAbnormalClose,
    DownstreamResume,
    DownstreamNormalClose,
]
