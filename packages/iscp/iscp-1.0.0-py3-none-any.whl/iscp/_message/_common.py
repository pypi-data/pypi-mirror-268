from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from time import time_ns
from typing import List, Union

__all__ = [
    "QoS",
    "DataPoint",
    "DataID",
    "DataPointGroup",
    "DataFilter",
    "DownstreamFilter",
    "StreamChunk",
    "DataIDOrAlias",
    "DateTime",
]

WILDCARD = "#"


class QoS(str, Enum):
    """
    QoSを表します。
    """

    UNRELIABLE = "UNRELIABLE"
    """UNRELIABLE"""
    RELIABLE = "RELIABLE"
    """RELIABLE"""
    PARTIAL = "PARTIAL"
    """PARTIAL"""

    @classmethod
    def parse(cls, arg: str):
        """
        文字列表現からQoSを返却します。

        Args:
            arg(str): 文字列
        """
        upper = arg.upper()
        if upper == cls.UNRELIABLE:
            return cls.UNRELIABLE
        if upper == cls.RELIABLE:
            return cls.RELIABLE
        if upper == cls.PARTIAL:
            return cls.PARTIAL
        raise ValueError(f"unrecognized qos {arg}")


@dataclass
class DataPoint(object):
    """
    データポイントを表します。

    データポイントは、経過時間を付与されたバイナリデータです。 バイナリデータのことをペイロードと呼びます。

    Attributes:
        elapsed_time(int): 経過時間ナノ秒
        payload: ペイロード
    """

    elapsed_time: int
    payload: bytes


@dataclass(frozen=True)
class DataID(object):
    """
    DataIDは、データポイントの、名称とデータ型を表す識別子です。

    おもに、ブローカーおよびノードでのデータの意味と型の特定、
    ダウンストリームフィルタにて指定された受信条件に各時系列データポイントが合致するかどうかの判定、などに使用されます。

    特殊文字 ``/`` はセパレータです。名称や型の階層構造を表現することができます。

    Attributes:
        name(str): 名称
        type(type): 型
    """

    name: str
    type: str

    @classmethod
    def parse(cls, data_id: str):
        """
        DataIDの文字列表現からDataIDを生成します。

        Args:
            data_id(str): DataIDの文字列表現
        """
        sp = data_id.split(sep=":")
        if len(sp) != 2:
            raise ValueError(f"invalid data_id[{data_id}]`")
        return cls(type=sp[0], name=sp[1])

    def __str__(self) -> str:
        return f"{self.type}:{self.name}"


DataIDOrAlias = Union[DataID, int]


@dataclass
class DataPointGroup(object):
    """
    ストリームチャンクの中のデータポイントをデータIDごとにまとめた集合です。

    Attributes:
        data_id_or_alias(iscp.DataIDOrAlias): データIDまたはそのエイリアス
        data_points(List[iscp.DataPoint]): データポイントのリスト

    """

    data_id_or_alias: DataIDOrAlias
    data_points: List[DataPoint]


@dataclass
class DataFilter(object):
    """
    受信するデータを指定するためのデータフィルタです。

    名称や型の指定において階層構造を表現したいときには、特殊文字 ``/`` をセパレータとして使用することができます。

    特殊文字 ``#`` はマルチレベルワイルドカードです。

    - フィルタが ``#`` のとき、 ``name`` はマッチします。
    - フィルタが ``#`` のとき、 ``group/name`` はマッチします。
    - フィルタが ``group/#`` のとき、 ``group/name`` はマッチします。
    - フィルタが ``group/#`` のとき、 ``group/sub-group/name`` はマッチします。
    - フィルタが ``group/#`` のとき、 ``other-group/name`` はマッチしません。

    特殊文字 ``+`` は単一レベルワイルドカードです。

    - フィルタが ``+`` のとき、 ``name`` はマッチします。
    - フィルタが ``group/+`` のとき、 ``group/name`` はマッチします。
    - フィルタが ``group/+/name`` のとき、 ``group/sub-group/name`` はマッチします。
    - フィルタが ``group/+/name`` のとき、 ``group/other-group/name`` はマッチします。
    - フィルタが ``group/+/name`` のとき、 ``group/other-group/some-name`` はマッチしません。

    Attributes:
        name: 名称
        type: 型
    """

    name: str
    type: str

    @classmethod
    def full_open(cls):
        return cls(name=WILDCARD, type=WILDCARD)

    @classmethod
    def parse(cls, data_filter: str):
        sp = data_filter.split(sep=":")
        if len(sp) != 2:
            raise ValueError(f"invalid data_filter[{data_filter}]`")
        return cls(type=sp[0], name=sp[1])

    def __str__(self) -> str:
        return f"{self.type}:{self.name}"


@dataclass
class DownstreamFilter(object):
    """
    ダウンストリームフィルタを表します。

    Attributes:
        source_node_id(str): 送信元ノードID
        data_filters(List[iscp.DataFilter]): データフィルタのリスト
    """

    source_node_id: str
    data_filters: List[DataFilter]

    @classmethod
    def all_for(cls, source_node_id: str):
        """
        指定したノードが送信するすべてのデータを取得するフィルタです。

        Args:
            source_node_id(str): データ取得対象とする送信元ノード
        """
        return cls(
            source_node_id=source_node_id,
            data_filters=[DataFilter.full_open()],
        )


@dataclass
class StreamChunk(object):
    """
    ストリームを時間で区切ったデータポイントのまとまりです。

    iSCP におけるデータ伝送は、このチャンク単位で行われます。

    Attributes:
        sequence_number(int): シーケンス番号
        data_point_groups(List[iscp.DataPointGroup]): データポイントグループのリスト
    """

    sequence_number: int
    data_point_groups: List[DataPointGroup]


# カスタムクラス
@dataclass
class DateTime(object):
    """
    iSCPで使用する日時を表します。

    Attributes:
        datetime(datetime): 日時（マイクロ秒精度）
        nano_secs(int): ナノ秒部
    """

    datetime: datetime
    nano_secs: int = 0

    @classmethod
    def from_unix_nano(cls, unix_nano: int):
        """
        UNIX時刻（ナノ秒単位）からiscp.DateTimeを生成します。

        Args:
            unix_nano(int): UNIX時刻（ナノ秒単位）
        Returns:
            iscp.DateTime: 日時
        """
        nano_secs = unix_nano % 1000
        unix_sec = int((unix_nano - nano_secs) / 1000) / 1_000_000
        return cls(datetime=datetime.fromtimestamp(unix_sec), nano_secs=nano_secs)

    @classmethod
    def utcnow(cls):
        """
        現在時刻（UTC）を取得します。
        """
        return cls.from_unix_nano(time_ns())

    def unix_nano(self) -> int:
        """
        UNIX時刻（ナノ秒単位）を返却します。

        Returns:
            int: UNIX時刻（ナノ秒単位）
        """
        return int(self.datetime.timestamp() * 1_000_000) * 1000 + self.nano_secs

    def isoformat(self, sep="T", timespec="auto") -> str:
        """
        UNIX時刻（ナノ秒単位）を返却します。

        Args:
            sep(str): セパレータ。デフォルトは"T"
            timespec(str): 仕様。デフォルトは "auto"
        Returns:
            str: ISO文字列
        """

        s = "%04d-%02d-%02d%c" % (self.datetime.year, self.datetime.month, self.datetime.day, sep) + _format_time(
            self.datetime.hour, self.datetime.minute, self.datetime.second, self.nano_secs, timespec
        )

        off = self.datetime.utcoffset()
        tz = _format_offset(off)
        if tz:
            s += tz

        return s


def _format_time(hh, mm, ss, ns, timespec="auto"):
    specs = {
        "hours": "{:02d}",
        "minutes": "{:02d}:{:02d}",
        "seconds": "{:02d}:{:02d}:{:02d}",
        "milliseconds": "{:02d}:{:02d}:{:02d}.{:03d}",
        "microseconds": "{:02d}:{:02d}:{:02d}.{:06d}",
        "nanoseconds": "{:02d}:{:02d}:{:02d}.{:09d}",
    }

    if timespec == "auto":
        # Skip trailing microseconds when us==0.
        timespec = "nanoseconds" if ns else "seconds"
    elif timespec == "milliseconds":
        ns //= 1000000
    elif timespec == "microseconds":
        ns //= 1000
    try:
        fmt = specs[timespec]
    except KeyError:
        raise ValueError("Unknown timespec value")
    else:
        return fmt.format(hh, mm, ss, ns)


def _format_offset(off):
    s = ""
    if off is not None:
        if off.days < 0:
            sign = "-"
            off = -off
        else:
            sign = "+"
        hh, mm = divmod(off, timedelta(hours=1))
        mm, ss = divmod(mm, timedelta(minutes=1))
        s += "%s%02d:%02d" % (sign, hh, mm)
        if ss or ss.microseconds:
            s += ":%02d" % ss.seconds

            if ss.microseconds:
                s += ".%06d" % ss.microseconds
    return s
