from dataclasses import dataclass
from typing import Dict, List, Optional
from uuid import UUID

from . import _message as message
from . import _model

__all__ = [
    "UpstreamChunk",
    "DownstreamChunk",
    "DataPointGroup",
    "DownstreamMetadata",
    "DownstreamCall",
    "UpstreamCall",
    "UpstreamChunkAck",
    "UpstreamChunkResult",
    "DownstreamReplyCall",
    "UpstreamReplyCall",
    "UpstreamState",
    "DownstreamState",
]


@dataclass
class DataPointGroup(object):
    """
    データID付きのデータポイントを表します。

    Attributes:
        data_id(iscp.DataID): データID
        data_points(List[iscp.DataPoint]):  データポイント配列

    """

    data_id: message.DataID
    data_points: list[message.DataPoint]


@dataclass
class UpstreamChunk(object):
    """
    アップストリームチャンクを表します。


    Attributes:
        sequence_number(int):  シーケンス番号
        data_point_groups(List[iscp.DataPointGroup]):  データポイントグループのリスト
    """

    sequence_number: int
    data_point_groups: List[DataPointGroup]


@dataclass
class UpstreamChunkResult(object):
    """
    アップストリームチャンクで送信されたデータポイントの処理結果を表します。

    Attributes:
        sequence_number(int): シーケンス番号
        result_code(iscp.ResultCode): 結果コード
        result_string(str): 結果文字列
    """

    sequence_number: int
    result_code: message.ResultCode
    result_string: str


@dataclass
class UpstreamChunkAck(object):
    """
    アップストリームチャンクに対する確認応答を表します。


    Attributes:
        results(List[iscp.UpstreamChunkResult]): 処理結果のリスト
    """

    results: List[UpstreamChunkResult]


@dataclass
class DownstreamChunk(object):
    """
    ダウンストリームチャンクを表します。

    Attributes:
        upstream_info(iscp.UpstreamInfo): アップストリーム情報
        sequence_number(int):  シーケンス番号
        data_point_groups(List[iscp.DataPointGroup]):  データポイントグループのリスト

    """

    upstream_info: message.UpstreamInfo
    sequence_number: int
    data_point_groups: List[DataPointGroup]


@dataclass
class DownstreamMetadata(object):
    """
    ダウンストリームメタデータを表します。

    Attributes:
        source_node_id(str): 送信元ノードID
        metadata(iscp.Metadata): メタデータ

    """

    source_node_id: str
    metadata: message.Metadata


@dataclass
class DownstreamCall(object):
    """
    ダウンストリームコールを表します。

    Attributes:
        call_id(str): コールID
        source_node_id(str):  送信元ノードID
        name(str):  名称
        type(str):  型
        payload(bytes):  ペイロード
    """

    call_id: str
    source_node_id: str
    name: str
    type: str
    payload: bytes


@dataclass
class DownstreamReplyCall(object):
    """
    ダウンストリームコールを表します。

    Attributes:
        request_call_id(str):  リクエストコールID
        source_node_id(str):  送信元ノードID
        name(str):  名称
        type(str):  型
        payload(bytes):  ペイロード
    """

    call_id: str
    request_call_id: str
    source_node_id: str
    name: str
    type: str
    payload: bytes


@dataclass
class UpstreamCall(object):
    """
    アップストリームコールを表します。

    Attributes:
        destination_node_id(str):  宛先ノードID
        name(str):  名称
        type(str):  型
        payload(bytes):  ペイロード
    """

    destination_node_id: str
    name: str
    type: str
    payload: bytes


@dataclass
class UpstreamReplyCall(object):
    """
    アップストリームリプライコールを表します。

    Attributes:
        request_call_id(str):  リクエストコールID
        destination_node_id(str): 送信先ノードID
        name(str):  名称
        type(str):  型
        payload(bytes):  ペイロード
    """

    request_call_id: str
    destination_node_id: str
    name: str
    type: str
    payload: bytes


@dataclass
class UpstreamState(object):
    """
    アップストリームの状態を表します。

    Attributes:
        data_id_aliases(Dict[int, iscp.DataID]): データIDエイリアスとデータIDのマップ
        total_data_points(int): 総送信データポイント数
        last_issued_sequence_number(int): 最後に払い出されたシーケンス番号
        data_points_buffer(list[_model.DataPointGroup]): 内部に保存しているデータポイントバッファ
    """

    data_id_aliases: Dict[int, message.DataID]
    total_data_points: int
    data_points_buffer: list[_model.DataPointGroup]
    last_issued_sequence_number: Optional[int] = None


@dataclass
class DownstreamState(object):
    """
    ダウンストリームの状態を表します。

    Attributes:
        id(UUID): ストリームID
        data_id_aliases(Dict[int, iscp.DataID]): データIDエイリアスとデータIDのマップ
        last_issued_data_id_alias(int): 最後に払い出されたデータIDエイリアス
        upstream_infos(Dict[int, iscp.UpstreamInfo]): アップストリームエイリアスとアップストリーム情報のマップ
        last_issued_upstream_info_alias(int): 最後に払い出されたアップストリーム情報のエイリアス
        last_issued_ack_sequence_number(int): 最後に払い出されたAckのシーケンス番号
        server_time(iscp.DateTime): DownstreamOpenResponseで返却されたサーバー時刻
    """

    id: UUID
    data_id_aliases: Dict[int, message.DataID]
    upstream_infos: Dict[int, message.UpstreamInfo]
    server_time: message.DateTime
    last_issued_data_id_alias: Optional[int] = None
    last_issued_upstream_info_alias: Optional[int] = None
    last_issued_ack_id: Optional[int] = None
