from typing import Dict, List

from iscp._encoding._codegen.iscp2.v1.common_pb2 import DataFilter as DataFilterPB
from iscp._encoding._codegen.iscp2.v1.common_pb2 import DataID as DataIDPB
from iscp._encoding._codegen.iscp2.v1.common_pb2 import DataPoint as DataPointPB
from iscp._encoding._codegen.iscp2.v1.common_pb2 import DataPointGroup as DataPointGroupPB
from iscp._encoding._codegen.iscp2.v1.common_pb2 import DownstreamFilter as DownstreamFilterPB
from iscp._encoding._codegen.iscp2.v1.common_pb2 import QoS as QoSPB
from iscp._encoding._codegen.iscp2.v1.common_pb2 import StreamChunk as StreamChunkPB
from iscp._exceptions import ISCPMalformedMessageError
from iscp._message import (
    DataFilter,
    DataID,
    DataPoint,
    DataPointGroup,
    DownstreamFilter,
    QoS,
    StreamChunk,
)


class WireToProto(object):
    @classmethod
    def qos(cls, arg: QoS) -> QoSPB:
        return getattr(QoSPB, arg.name)

    @classmethod
    def data_ids(cls, arg: List[DataID]) -> List[DataIDPB]:
        return [cls.data_id(data_id) for data_id in arg]

    @classmethod
    def data_id(cls, arg: DataID) -> DataIDPB:
        res = DataIDPB()
        cls._data_id(res, arg)
        return res

    @classmethod
    def data_id_aliases(cls, dest: Dict[int, DataIDPB], arg: Dict[int, DataID]):
        for k, v in arg.items():
            cls._data_id(dest[k], v)

    @classmethod
    def _data_id(cls, dest: DataIDPB, arg: DataID):
        dest.name = arg.name
        dest.type = arg.type

    @classmethod
    def stream_chunk(cls, arg: StreamChunk) -> StreamChunkPB:
        res = StreamChunkPB()
        res.sequence_number = arg.sequence_number
        res.data_point_groups.extend(cls.data_point_groups(arg.data_point_groups))
        return res

    @classmethod
    def data_point_groups(cls, arg: List[DataPointGroup]) -> List[DataPointGroupPB]:
        return [cls.data_point_group(v) for v in arg]

    @classmethod
    def data_point_group(cls, arg: DataPointGroup) -> DataPointGroupPB:
        res = DataPointGroupPB()
        res.data_points.extend(cls.data_points(arg.data_points))
        cls.data_id_or_alias(res, arg.data_id_or_alias)
        return res

    @classmethod
    def data_id_or_alias(cls, dest: DataPointGroupPB, arg: DataID | int):
        if isinstance(arg, DataID):
            dest.data_id.CopyFrom(cls.data_id(arg))  # type: ignore
            return

        if isinstance(arg, int):
            dest.data_id_alias = arg  # type: ignore
            return

        raise ISCPMalformedMessageError("unrecognized data_id_or_alias")

    @classmethod
    def data_points(cls, arg: List[DataPoint]) -> List[DataPointPB]:
        return [cls.data_point(v) for v in arg]

    @classmethod
    def data_point(cls, arg: DataPoint) -> DataPointPB:
        res = DataPointPB()
        res.elapsed_time = arg.elapsed_time
        res.payload = arg.payload
        return res

    @classmethod
    def data_filter(cls, arg: DataFilter) -> DataFilterPB:
        res = DataFilterPB()
        res.name = arg.name
        res.type = arg.type
        return res

    @classmethod
    def data_filters(cls, arg: List[DataFilter]) -> List[DataFilterPB]:
        return [cls.data_filter(v) for v in arg]

    @classmethod
    def downstream_filter(cls, arg: DownstreamFilter) -> DownstreamFilterPB:
        res = DownstreamFilterPB()
        res.source_node_id = arg.source_node_id
        res.data_filters.extend(cls.data_filters(arg.data_filters))
        return res

    @classmethod
    def downstream_filters(cls, arg: List[DownstreamFilter]) -> List[DownstreamFilterPB]:
        return [cls.downstream_filter(v) for v in arg]


class ProtoToWire(object):
    @classmethod
    def qos(cls, arg: QoSPB) -> QoS:
        return QoS[QoSPB.Name(arg)]

    @classmethod
    def data_ids(cls, arg: List[DataIDPB]) -> List[DataID]:
        return [cls.data_id(data_id) for data_id in arg]

    @classmethod
    def data_id(cls, arg: DataIDPB) -> DataID:
        return DataID(
            name=arg.name,
            type=arg.type,
        )

    @classmethod
    def data_id_aliases(cls, arg: Dict[int, DataIDPB]) -> Dict[int, DataID]:
        return {k: cls.data_id(v) for k, v in arg.items()}

    @classmethod
    def stream_chunk(cls, arg: StreamChunkPB) -> StreamChunk:
        return StreamChunk(
            sequence_number=arg.sequence_number,
            data_point_groups=cls.data_point_groups(arg.data_point_groups),
        )

    @classmethod
    def data_point_groups(cls, arg: List[DataPointGroupPB]) -> List[DataPointGroup]:
        return [cls.data_point_group(v) for v in arg]

    @classmethod
    def data_point_group(cls, arg: DataPointGroupPB) -> DataPointGroup:
        return DataPointGroup(
            data_id_or_alias=cls.data_id_or_alias(arg),
            data_points=cls.data_points(arg.data_points),
        )

    @classmethod
    def data_id_or_alias(cls, arg: DataPointGroupPB) -> DataID | int:
        which_one_of = arg.WhichOneof("data_id_or_alias")
        if which_one_of == "data_id":
            return cls.data_id(arg.data_id)  # type: ignore

        if which_one_of == "data_id_alias":
            return arg.data_id_alias  # type: ignore

        raise ISCPMalformedMessageError("unrecognized data_id_or_alias")

    @classmethod
    def data_points(cls, arg: List[DataPointPB]) -> List[DataPoint]:
        return [cls.data_point(v) for v in arg]

    @classmethod
    def data_point(cls, arg: DataPointPB) -> DataPoint:
        return DataPoint(
            elapsed_time=arg.elapsed_time,
            payload=arg.payload,
        )

    @classmethod
    def data_filter(cls, arg: DataFilterPB) -> DataFilter:
        return DataFilter(
            name=arg.name,
            type=arg.type,
        )

    @classmethod
    def data_filters(cls, arg: List[DataFilterPB]) -> List[DataFilter]:
        return [cls.data_filter(v) for v in arg]

    @classmethod
    def downstream_filter(cls, arg: DownstreamFilterPB) -> DownstreamFilter:
        return DownstreamFilter(
            source_node_id=arg.source_node_id,
            data_filters=cls.data_filters(arg.data_filters),
        )

    @classmethod
    def downstream_filters(cls, arg: List[DownstreamFilterPB]) -> List[DownstreamFilter]:
        return [cls.downstream_filter(v) for v in arg]
