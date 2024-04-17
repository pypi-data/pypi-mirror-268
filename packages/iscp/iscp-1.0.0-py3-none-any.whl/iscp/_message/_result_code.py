from enum import Enum

__all__ = ["ResultCode"]


class ResultCode(Enum):
    """
    ResultCode は、要求の処理結果を表す識別コードです。

    ResultCode は、以下の値を取ります。
    """

    SUCCEEDED = 0
    """処理が正常に成功したことを表します。"""
    NORMAL_CLOSURE = 0
    """正常にコネクションが閉じられたことを表します。"""
    INCOMPATIBLE_VERSION = 1
    """ノードとブローカーのバージョンに互換性が無いことを表します。"""
    MAXIMUM_DATA_ID_ALIAS = 2
    """データIDエイリアス値の数が上限に達し、データIDエイリアス値を新たに割り当てることができないことを表します。"""
    MAXIMUM_UPSTREAM_ALIAS = 3
    """アップストリームエイリアス値の数が上限に達し、アップストリームエイリアス値を新たに割り当てることができないことを表します。"""
    UNSPECIFIED_ERROR = 64
    """種類を規定しないエラーです。予期しないエラーが発生した場合に使用されます。"""
    NO_NODE_ID = 65
    """接続時にノードIDを指定していないことを表します。"""
    AUTH_FAILED = 66
    """認証や認可の処理に失敗したことを表します。"""
    CONNECT_TIMEOUT = 67
    """妥当な時間までに、通信の開始シーケンスが完了しなかったことを表します。"""
    MALFORMED_MESSAGE = 68
    """不正な形式のメッセージを受信したことを表します。"""
    PROTOCOL_ERROR = 69
    """プロトコル違反を表します。"""
    ACK_TIMEOUT = 70
    """ACKの返却までに時間がかかりすぎて、送信側よりネットワークが切断されたことを表します。"""
    INVALID_PAYLOAD = 71
    """ペイロードの形式が不正であることを表します。"""
    INVALID_DATA_ID = 72
    """データIDが不正であることを表します。"""
    INVALID_DATA_ID_ALIAS = 73
    """データIDエイリアスが不正であることを表します。"""
    INVALID_DATA_FILTER = 74
    """データフィルタが不正であることを表します。"""
    STREAM_NOT_FOUND = 75
    """受信者が保持している情報の中に、対象のストリームが含まれないことを表します。"""
    RESUME_REQUEST_CONFLICT = 76
    """再開しようとしたストリームが接続中であることを表します。"""
    PROCESS_FAILED = 77
    """処理が失敗したことを表します。"""
    DESIRED_QOS_NOT_SUPPORTED = 78
    """要求されたQoSをサポートしていないことを表します。"""
    PING_TIMEOUT = 79
    """Pingのタイムアウトが発生したことを表します。"""
    TOO_LARGE_MESSAGE_SIZE = 80
    """メッセージのサイズが大きすぎることを表します。"""
    TOO_MANY_DATA_ID_ALIASES = 81
    """データIDエイリアスが多すぎることを表します。"""
    TOO_MANY_STREAMS = 82
    """ストリームが多すぎることを表します。"""
    TOO_LONG_ACK_INTERVAL = 83
    """ACKの返却間隔が長すぎることを表します。"""
    TOO_MANY_DOWNSTREAM_FILTERS = 84
    """ダウンストリームフィルタが多すぎることを表します。"""
    TOO_MANY_DATA_FILTERS = 85
    """データフィルタが多すぎることを表します。"""
    TOO_LONG_EXPIRY_INTERVAL = 86
    """有効期限が長すぎることを表します。"""
    TOO_LONG_PING_TIMEOUT = 87
    """Pingタイムアウト値が大きすぎることを表します。"""
    TOO_SHORT_PING_INTERVAL = 88
    """Ping間隔が短すぎることを表します。"""
    TOO_SHORT_PING_TIMEOUT = 89
    """Pingタイムアウトが短すぎることを表します。"""
    RATE_LIMIT_REACHED = 90
    """すでに永続化されているセッションの生成元ノードと、新たに永続化しようとするノードが異なることを表します。"""
    NODE_ID_MISMATCH = 128
    """レートリミットに到達したことを表します。"""
    SESSION_NOT_FOUND = 129
    """セッションが見つからなかったことを表します。"""
    SESSION_ALREADY_CLOSED = 130
    """セッションがすでに閉じられていることを表します。"""
    SESSION_CANNOT_CLOSED = 131
    """セッションを閉じることができないことを表します。"""
