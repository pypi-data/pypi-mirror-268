from uuid import UUID

from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import BaseTime as BaseTimePB
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import (
    DownstreamAbnormalClose as DownstreamAbnormalClosePB,
)
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import (
    DownstreamNormalClose as DownstreamNormalClosePB,
)
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import DownstreamOpen as DownstreamOpenPB
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import DownstreamResume as DownstreamResumePB
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import (
    UpstreamAbnormalClose as UpstreamAbnormalClosePB,
)
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import (
    UpstreamNormalClose as UpstreamNormalClosePB,
)
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import UpstreamOpen as UpstreamOpenPB
from iscp._encoding._codegen.iscp2.v1.metadata_pb2 import UpstreamResume as UpstreamResumePB
from iscp._message import (
    BaseTime,
    DownstreamAbnormalClose,
    DownstreamNormalClose,
    DownstreamOpen,
    DownstreamResume,
    UpstreamAbnormalClose,
    UpstreamNormalClose,
    UpstreamOpen,
    UpstreamResume,
    DateTime,
)

from . import _common


class WireToProto(object):
    @classmethod
    def base_time(cls, arg: BaseTime) -> BaseTimePB:
        res = BaseTimePB()
        res.session_id = arg.session_id
        res.name = arg.name
        res.priority = arg.priority
        res.elapsed_time = arg.elapsed_time
        res.base_time = arg.base_time.unix_nano()
        return res

    @classmethod
    def upstream_open(cls, arg: UpstreamOpen) -> UpstreamOpenPB:
        res = UpstreamOpenPB()
        res.stream_id = arg.stream_id.bytes
        res.session_id = arg.session_id
        res.qos = _common.WireToProto.qos(arg.qos)
        return res

    @classmethod
    def upstream_abnormal_close(cls, arg: UpstreamAbnormalClose) -> UpstreamAbnormalClosePB:
        res = UpstreamAbnormalClosePB()
        res.stream_id = arg.stream_id.bytes
        res.session_id = arg.session_id
        return res

    @classmethod
    def upstream_resume(cls, arg: UpstreamResume) -> UpstreamResumePB:
        res = UpstreamResumePB()
        res.stream_id = arg.stream_id.bytes
        res.session_id = arg.session_id
        res.qos = _common.WireToProto.qos(arg.qos)
        return res

    @classmethod
    def upstream_normal_close(cls, arg: UpstreamNormalClose) -> UpstreamNormalClosePB:
        res = UpstreamNormalClosePB()
        res.stream_id = arg.stream_id.bytes
        res.session_id = arg.session_id
        res.total_data_points = arg.total_data_points
        res.final_sequence_number = arg.final_sequence_number
        return res

    @classmethod
    def downstream_open(cls, arg: DownstreamOpen) -> DownstreamOpenPB:
        res = DownstreamOpenPB()
        res.stream_id = arg.stream_id.bytes
        res.downstream_filters.extend(_common.WireToProto.downstream_filters(arg.downstream_filters))
        res.qos = _common.WireToProto.qos(arg.qos)
        return res

    @classmethod
    def downstream_abnormal_close(
        cls,
        arg: DownstreamAbnormalClose,
    ) -> DownstreamAbnormalClosePB:
        res = DownstreamAbnormalClosePB()
        res.stream_id = arg.stream_id.bytes
        return res

    @classmethod
    def downstream_resume(cls, arg: DownstreamResume) -> DownstreamResumePB:
        res = DownstreamResumePB()
        res.stream_id = arg.stream_id.bytes
        res.downstream_filters.extend(_common.WireToProto.downstream_filters(arg.downstream_filters))
        res.qos = _common.WireToProto.qos(arg.qos)
        return res

    @classmethod
    def downstream_normal_close(cls, arg: DownstreamNormalClose) -> DownstreamNormalClosePB:
        res = DownstreamNormalClosePB()
        res.stream_id = arg.stream_id.bytes
        return res


class ProtoToWire:
    @classmethod
    def base_time(cls, arg: BaseTimePB) -> BaseTime:
        return BaseTime(
            session_id=arg.session_id,
            name=arg.name,
            priority=arg.priority,
            elapsed_time=arg.elapsed_time,
            base_time=DateTime.from_unix_nano(arg.base_time),
        )

    @classmethod
    def upstream_open(cls, arg: UpstreamOpenPB) -> UpstreamOpen:
        return UpstreamOpen(
            stream_id=UUID(bytes=arg.stream_id),
            session_id=arg.session_id,
            qos=_common.ProtoToWire.qos(arg.qos),
        )

    @classmethod
    def upstream_abnormal_close(cls, arg: UpstreamAbnormalClosePB) -> UpstreamAbnormalClose:
        return UpstreamAbnormalClose(
            stream_id=UUID(bytes=arg.stream_id),
            session_id=arg.session_id,
        )

    @classmethod
    def upstream_resume(cls, arg: UpstreamResumePB) -> UpstreamResume:
        return UpstreamResume(
            stream_id=UUID(bytes=arg.stream_id),
            session_id=arg.session_id,
            qos=_common.ProtoToWire.qos(arg.qos),
        )

    @classmethod
    def upstream_normal_close(cls, arg: UpstreamNormalClosePB) -> UpstreamNormalClose:
        return UpstreamNormalClose(
            stream_id=UUID(bytes=arg.stream_id),
            session_id=arg.session_id,
            total_data_points=arg.total_data_points,
            final_sequence_number=arg.final_sequence_number,
        )

    @classmethod
    def downstream_open(cls, arg: DownstreamOpenPB) -> DownstreamOpen:
        return DownstreamOpen(
            stream_id=UUID(bytes=arg.stream_id),
            downstream_filters=_common.ProtoToWire.downstream_filters(arg.downstream_filters),
            qos=_common.ProtoToWire.qos(arg.qos),
        )

    @classmethod
    def downstream_abnormal_close(
        cls,
        arg: DownstreamAbnormalClosePB,
    ) -> DownstreamAbnormalClose:
        return DownstreamAbnormalClose(
            stream_id=UUID(bytes=arg.stream_id),
        )

    @classmethod
    def downstream_resume(cls, arg: DownstreamResumePB) -> DownstreamResume:
        return DownstreamResume(
            stream_id=UUID(bytes=arg.stream_id),
            downstream_filters=_common.ProtoToWire.downstream_filters(arg.downstream_filters),
            qos=_common.ProtoToWire.qos(arg.qos),
        )

    @classmethod
    def downstream_normal_close(cls, arg: DownstreamNormalClosePB) -> DownstreamNormalClose:
        return DownstreamNormalClose(
            stream_id=UUID(bytes=arg.stream_id),
        )
