import dataclasses
import io
from dataclasses import dataclass
from enum import Enum
from urllib.parse import urlencode

__all__ = ["NegotiationParams", "EncodingName"]


class EncodingName(str, Enum):
    """
    エンコーディングの名前です。
    """

    PROTOBUF = "proto"
    """ProtocolBuffers"""

    @classmethod
    def parse(cls, arg: str):
        pass
        lower = arg.lower()
        if lower in [cls.PROTOBUF, "protobuf"]:
            return cls.PROTOBUF
        raise ValueError(f"unrecognized encoding {arg}")


@dataclass
class NegotiationParams(object):
    """
    ネゴシエーションパラメータを表します。

    Attributes:
        enc(iscp.EncodingName): エンコーディング名です。

    """

    enc: EncodingName = EncodingName.PROTOBUF

    def encode_to_url_values(self) -> str:
        """
        URLパラメータにエンコードします。

        Returns:
            str: URLパラメータにエンコードされたネゴシエーションパラメータ
        """
        return urlencode({"enc": self.enc.value})

    def encode_to_binary(self) -> bytes:
        """
        バイナリ形式にエンコードします。

        Returns:
            bytes: バイナリ形式にエンコードされたネゴシエーションパラメータ
        """
        wr = io.BytesIO()
        for k, v in dataclasses.asdict(self).items():
            key = k.encode()
            key_size = len(key)
            wr.write(key_size.to_bytes(2, "big", signed=False))
            wr.write(key)

            val = v.encode()
            val_size = len(val)
            wr.write(val_size.to_bytes(2, "big", signed=False))
            wr.write(val)
        return wr.getvalue()
