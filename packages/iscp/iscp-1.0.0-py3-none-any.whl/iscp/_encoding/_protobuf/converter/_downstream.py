__all__ = ["WireToProto", "ProtoToWire"]

from typing import Dict, List
from uuid import UUID

from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import DownstreamChunk as DownstreamChunkPB
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamChunkAck as DownstreamChunkAckPB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamChunkAckComplete as DownstreamChunkAckCompletePB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamChunkResult as DownstreamChunkResultPB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamCloseRequest as DownstreamCloseRequestPB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamCloseResponse as DownstreamCloseResponsePB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamMetadata as DownstreamMetadataPB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamMetadataAck as DownstreamMetadataAckPB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamOpenRequest as DownstreamOpenRequestPB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamOpenResponse as DownstreamOpenResponsePB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamResumeRequest as DownstreamResumeRequestPB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import (
    DownstreamResumeResponse as DownstreamResumeResponsePB,
)
from iscp._encoding._codegen.iscp2.v1.downstream_pb2 import UpstreamInfo as UpstreamInfoPB
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamChunkAckCompleteExtensionFields as DownstreamChunkAckCompleteExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamChunkAckExtensionFields as DownstreamChunkAckExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamChunkExtensionFields as DownstreamChunkExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamChunkResultExtensionFields as DownstreamChunkResultExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamCloseRequestExtensionFields as DownstreamCloseRequestExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamCloseResponseExtensionFields as DownstreamCloseResponseExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamMetadataAckExtensionFields as DownstreamMetadataAckExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamMetadataExtensionFields as DownstreamMetadataExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamOpenRequestExtensionFields as DownstreamOpenRequestExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamOpenResponseExtensionFields as DownstreamOpenResponseExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamResumeRequestExtensionFields as DownstreamResumeRequestExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.downstream_pb2 import (
    DownstreamResumeResponseExtensionFields as DownstreamResumeResponseExtensionFieldsPB,
)
from iscp._exceptions import ISCPMalformedMessageError
from iscp._message import (
    BaseTime,
    DownstreamAbnormalClose,
    DownstreamChunkAck,
    DownstreamChunkAckComplete,
    DownstreamChunkAckCompleteExtensionFields,
    DownstreamChunkAckExtensionFields,
    DownstreamChunkExtensionFields,
    DownstreamChunkResult,
    DownstreamChunkResultExtensionFields,
    DownstreamCloseRequest,
    DownstreamCloseRequestExtensionFields,
    DownstreamCloseResponse,
    DownstreamCloseResponseExtensionFields,
    Metadata,
    DownstreamMetadataAck,
    DownstreamMetadataAckExtensionFields,
    DownstreamMetadataExtensionFields,
    DownstreamNormalClose,
    DownstreamOpen,
    DownstreamOpenRequest,
    DownstreamOpenRequestExtensionFields,
    DownstreamOpenResponse,
    DownstreamOpenResponseExtensionFields,
    DownstreamResume,
    DownstreamResumeRequest,
    DownstreamResumeRequestExtensionFields,
    DownstreamResumeResponse,
    DownstreamResumeResponseExtensionFields,
    UpstreamAbnormalClose,
    UpstreamInfo,
    UpstreamNormalClose,
    UpstreamOpen,
    UpstreamResume,
    DateTime,
)

from iscp._message._downstream import (
    DownstreamChunk,
    DownstreamMetadata,
)

from . import _common, _metadata, _result_code


class WireToProto(object):
    @classmethod
    def downstream_open_request_extension_fields(
        cls, _: DownstreamOpenRequestExtensionFields
    ) -> DownstreamOpenRequestExtensionFieldsPB:
        return DownstreamOpenRequestExtensionFieldsPB()

    @classmethod
    def downstream_open_response_extension_fields(
        cls, _: DownstreamOpenResponseExtensionFields
    ) -> DownstreamOpenResponseExtensionFieldsPB:
        return DownstreamOpenResponseExtensionFieldsPB()

    @classmethod
    def downstream_resume_request_extension_fields(
        cls, _: DownstreamResumeRequestExtensionFields
    ) -> DownstreamResumeRequestExtensionFieldsPB:
        return DownstreamResumeRequestExtensionFieldsPB()

    @classmethod
    def downstream_resume_response_extension_fields(
        cls, _: DownstreamResumeResponseExtensionFields
    ) -> DownstreamResumeResponseExtensionFieldsPB:
        return DownstreamResumeResponseExtensionFieldsPB()

    @classmethod
    def downstream_close_request_extension_fields(
        cls, _: DownstreamCloseRequestExtensionFields
    ) -> DownstreamCloseRequestExtensionFieldsPB:
        return DownstreamCloseRequestExtensionFieldsPB()

    @classmethod
    def downstream_close_response_extension_fields(
        cls, _: DownstreamCloseResponseExtensionFields
    ) -> DownstreamCloseResponseExtensionFieldsPB:
        return DownstreamCloseResponseExtensionFieldsPB()

    @classmethod
    def downstream_chunk_extension_fields(cls, _: DownstreamChunkExtensionFields) -> DownstreamChunkExtensionFieldsPB:
        return DownstreamChunkExtensionFieldsPB()

    @classmethod
    def downstream_chunk_ack_extension_fields(cls, _: DownstreamChunkAckExtensionFields) -> DownstreamChunkAckExtensionFieldsPB:
        return DownstreamChunkAckExtensionFieldsPB()

    @classmethod
    def downstream_chunk_ack_complete_extension_fields(
        cls, _: DownstreamChunkAckCompleteExtensionFields
    ) -> DownstreamChunkAckCompleteExtensionFieldsPB:
        return DownstreamChunkAckCompleteExtensionFieldsPB()

    @classmethod
    def downstream_metadata_extension_fields(cls, _: DownstreamMetadataExtensionFields) -> DownstreamMetadataExtensionFieldsPB:
        return DownstreamMetadataExtensionFieldsPB()

    @classmethod
    def downstream_metadata_ack_extension_fields(
        cls, _: DownstreamMetadataAckExtensionFields
    ) -> DownstreamMetadataAckExtensionFieldsPB:
        return DownstreamMetadataAckExtensionFieldsPB()

    @classmethod
    def downstream_chunk_result_extension_fields(
        cls, _: DownstreamChunkResultExtensionFields
    ) -> DownstreamChunkResultExtensionFieldsPB:
        return DownstreamChunkResultExtensionFieldsPB()

    @classmethod
    def downstream_open_request(cls, arg: DownstreamOpenRequest) -> DownstreamOpenRequestPB:
        res = DownstreamOpenRequestPB()
        res.request_id = arg.request_id
        res.desired_stream_id_alias = arg.desired_stream_id_alias
        res.downstream_filters.extend(_common.WireToProto.downstream_filters(arg.downstream_filters))
        res.expiry_interval = arg.expiry_interval
        _common.WireToProto.data_id_aliases(res.data_id_aliases, arg.data_id_aliases)
        res.qos = _common.WireToProto.qos(arg.qos)
        res.extension_fields.CopyFrom(cls.downstream_open_request_extension_fields(arg.extension_fields))
        res.omit_empty_chunk = arg.omit_empty_chunk
        return res

    @classmethod
    def downstream_open_response(cls, arg: DownstreamOpenResponse) -> DownstreamOpenResponsePB:
        res = DownstreamOpenResponsePB()
        res.request_id = arg.request_id
        res.assigned_stream_id = arg.assigned_stream_id.bytes
        res.server_time = arg.server_time.unix_nano()
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.downstream_open_response_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_resume_request(cls, arg: DownstreamResumeRequest) -> DownstreamResumeRequestPB:
        res = DownstreamResumeRequestPB()
        res.request_id = arg.request_id
        res.stream_id = arg.stream_id.bytes
        res.desired_stream_id_alias = arg.desired_stream_id_alias
        res.extension_fields.CopyFrom(cls.downstream_resume_request_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_resume_response(cls, arg: DownstreamResumeResponse) -> DownstreamResumeResponsePB:
        res = DownstreamResumeResponsePB()
        res.request_id = arg.request_id
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.downstream_resume_response_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_close_request(cls, arg: DownstreamCloseRequest) -> DownstreamCloseRequestPB:
        res = DownstreamCloseRequestPB()
        res.request_id = arg.request_id
        res.stream_id = arg.stream_id.bytes
        res.extension_fields.CopyFrom(cls.downstream_close_request_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_close_response(cls, arg: DownstreamCloseResponse) -> DownstreamCloseResponsePB:
        res = DownstreamCloseResponsePB()
        res.request_id = arg.request_id
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.downstream_close_response_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_chunk(cls, arg: DownstreamChunk) -> DownstreamChunkPB:
        res = DownstreamChunkPB()
        res.stream_id_alias = arg.stream_id_alias
        cls.upstream_or_alias(res, arg.upstream_or_alias)
        res.stream_chunk.CopyFrom(_common.WireToProto.stream_chunk(arg.stream_chunk))
        res.extension_fields.CopyFrom(cls.downstream_chunk_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_or_alias(cls, res: DownstreamChunkPB, arg: UpstreamInfo | int):
        if isinstance(arg, UpstreamInfo):
            res.upstream_info.CopyFrom(cls.upstream_info(arg))
            return

        if isinstance(arg, int):
            res.upstream_alias = arg
            return

        raise ISCPMalformedMessageError(f"unrecognized upstream_or_alias{arg}")

    @classmethod
    def downstream_chunk_ack(cls, arg: DownstreamChunkAck) -> DownstreamChunkAckPB:
        res = DownstreamChunkAckPB()
        res.stream_id_alias = arg.stream_id_alias
        res.ack_id = arg.ack_id
        res.results.extend(cls.downstream_chunk_results(arg.results))
        cls.upstream_aliases(res.upstream_aliases, arg.upstream_aliases)
        _common.WireToProto.data_id_aliases(res.data_id_aliases, arg.data_id_aliases)
        res.extension_fields.CopyFrom(cls.downstream_chunk_ack_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_chunk_ack_complete(cls, arg: DownstreamChunkAckComplete) -> DownstreamChunkAckCompletePB:
        res = DownstreamChunkAckCompletePB()
        res.stream_id_alias = arg.stream_id_alias
        res.ack_id = arg.ack_id
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.downstream_chunk_ack_complete_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def downstream_metadata(cls, arg: DownstreamMetadata) -> DownstreamMetadataPB:
        res = DownstreamMetadataPB()
        res.request_id = arg.request_id
        res.stream_id_alias = arg.stream_id_alias
        cls.metadata(res, arg.metadata)
        res.source_node_id = arg.source_node_id
        res.extension_fields.CopyFrom(cls.downstream_metadata_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def metadata(cls, res: DownstreamMetadataPB, arg: Metadata):

        if isinstance(arg, BaseTime):
            res.base_time.CopyFrom(_metadata.WireToProto.base_time(arg))
            return
        if isinstance(arg, UpstreamOpen):
            res.upstream_open.CopyFrom(_metadata.WireToProto.upstream_open(arg))
            return
        if isinstance(arg, UpstreamAbnormalClose):
            res.upstream_abnormal_close.CopyFrom(_metadata.WireToProto.upstream_abnormal_close(arg))
            return
        if isinstance(arg, UpstreamResume):
            res.upstream_resume.CopyFrom(_metadata.WireToProto.upstream_resume(arg))
            return
        if isinstance(arg, UpstreamNormalClose):
            res.upstream_normal_close.CopyFrom(_metadata.WireToProto.upstream_normal_close(arg))
            return
        if isinstance(arg, DownstreamOpen):
            res.downstream_open.CopyFrom(_metadata.WireToProto.downstream_open(arg))
            return
        if isinstance(arg, DownstreamAbnormalClose):
            res.downstream_abnormal_close.CopyFrom(_metadata.WireToProto.downstream_abnormal_close(arg))
            return
        if isinstance(arg, DownstreamResume):
            res.downstream_resume.CopyFrom(_metadata.WireToProto.downstream_resume(arg))
            return
        if isinstance(arg, DownstreamNormalClose):
            res.downstream_normal_close.CopyFrom(_metadata.WireToProto.downstream_normal_close(arg))
            return

        raise ISCPMalformedMessageError(f"unrecognized metadata {arg}")

    @classmethod
    def downstream_metadata_ack(cls, arg: DownstreamMetadataAck) -> DownstreamMetadataAckPB:
        res = DownstreamMetadataAckPB()
        res.request_id = arg.request_id
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.downstream_metadata_ack_extension_fields(arg.extension_fields))
        return res

    #
    # Internals
    #

    @classmethod
    def upstream_aliases(cls, res: Dict[int, UpstreamInfoPB], arg: Dict[int, UpstreamInfo]):
        for k, v in arg.items():
            cls._upstream_info(res[k], v)

    @classmethod
    def upstream_info(cls, arg: UpstreamInfo) -> UpstreamInfoPB:
        res = UpstreamInfoPB()
        cls._upstream_info(res, arg)
        return res

    @classmethod
    def _upstream_info(cls, res: UpstreamInfoPB, arg: UpstreamInfo):
        res.session_id = arg.session_id
        res.stream_id = arg.stream_id.bytes
        res.source_node_id = arg.source_node_id

    @classmethod
    def downstream_chunk_results(cls, arg: List[DownstreamChunkResult]) -> List[DownstreamChunkResultPB]:
        return [cls.downstream_chunk_result(v) for v in arg]

    @classmethod
    def downstream_chunk_result(cls, arg: DownstreamChunkResult) -> DownstreamChunkResultPB:
        res = DownstreamChunkResultPB()
        res.stream_id_of_upstream = arg.stream_id_of_upstream.bytes
        res.sequence_number_in_upstream = arg.sequence_number_in_upstream
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.downstream_chunk_result_extension_fields(arg.extension_fields))
        return res


class ProtoToWire(object):
    @classmethod
    def downstream_open_request_extension_fields(
        cls, _: DownstreamOpenRequestExtensionFieldsPB
    ) -> DownstreamOpenRequestExtensionFields:
        return DownstreamOpenRequestExtensionFields()

    @classmethod
    def downstream_open_response_extension_fields(
        cls, _: DownstreamOpenResponseExtensionFieldsPB
    ) -> DownstreamOpenResponseExtensionFields:
        return DownstreamOpenResponseExtensionFields()

    @classmethod
    def downstream_resume_request_extension_fields(
        cls, _: DownstreamResumeRequestExtensionFieldsPB
    ) -> DownstreamResumeRequestExtensionFields:
        return DownstreamResumeRequestExtensionFields()

    @classmethod
    def downstream_resume_response_extension_fields(
        cls, _: DownstreamResumeResponseExtensionFieldsPB
    ) -> DownstreamResumeResponseExtensionFields:
        return DownstreamResumeResponseExtensionFields()

    @classmethod
    def downstream_close_request_extension_fields(
        cls, _: DownstreamCloseRequestExtensionFieldsPB
    ) -> DownstreamCloseRequestExtensionFields:
        return DownstreamCloseRequestExtensionFields()

    @classmethod
    def downstream_close_response_extension_fields(
        cls, _: DownstreamCloseResponseExtensionFieldsPB
    ) -> DownstreamCloseResponseExtensionFields:
        return DownstreamCloseResponseExtensionFields()

    @classmethod
    def downstream_chunk_extension_fields(cls, _: DownstreamChunkExtensionFieldsPB) -> DownstreamChunkExtensionFields:
        return DownstreamChunkExtensionFields()

    @classmethod
    def downstream_chunk_ack_extension_fields(cls, _: DownstreamChunkAckExtensionFieldsPB) -> DownstreamChunkAckExtensionFields:
        return DownstreamChunkAckExtensionFields()

    @classmethod
    def downstream_chunk_ack_complete_extension_fields(
        cls, _: DownstreamChunkAckCompleteExtensionFieldsPB
    ) -> DownstreamChunkAckCompleteExtensionFields:
        return DownstreamChunkAckCompleteExtensionFields()

    @classmethod
    def downstream_metadata_extension_fields(cls, _: DownstreamMetadataExtensionFieldsPB) -> DownstreamMetadataExtensionFields:
        return DownstreamMetadataExtensionFields()

    @classmethod
    def downstream_metadata_ack_extension_fields(
        cls, _: DownstreamMetadataAckExtensionFieldsPB
    ) -> DownstreamMetadataAckExtensionFields:
        return DownstreamMetadataAckExtensionFields()

    @classmethod
    def downstream_chunk_result_extension_fields(
        cls, _: DownstreamChunkResultExtensionFieldsPB
    ) -> DownstreamChunkResultExtensionFields:
        return DownstreamChunkResultExtensionFields()

    @classmethod
    def downstream_open_request(cls, arg: DownstreamOpenRequestPB) -> DownstreamOpenRequest:
        return DownstreamOpenRequest(
            request_id=arg.request_id,
            desired_stream_id_alias=arg.desired_stream_id_alias,
            downstream_filters=_common.ProtoToWire.downstream_filters(arg.downstream_filters),
            expiry_interval=arg.expiry_interval,
            data_id_aliases=_common.ProtoToWire.data_id_aliases(arg.data_id_aliases),
            qos=_common.ProtoToWire.qos(arg.qos),
            extension_fields=cls.downstream_open_request_extension_fields(arg.extension_fields),
            omit_empty_chunk=arg.omit_empty_chunk,
        )

    @classmethod
    def downstream_open_response(cls, arg: DownstreamOpenResponsePB) -> DownstreamOpenResponse:
        return DownstreamOpenResponse(
            request_id=arg.request_id,
            assigned_stream_id=UUID(bytes=arg.assigned_stream_id),
            server_time=DateTime.from_unix_nano(arg.server_time),
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.downstream_open_response_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_resume_request(cls, arg: DownstreamResumeRequestPB) -> DownstreamResumeRequest:
        return DownstreamResumeRequest(
            request_id=arg.request_id,
            stream_id=UUID(bytes=arg.stream_id),
            desired_stream_id_alias=arg.desired_stream_id_alias,
            extension_fields=cls.downstream_resume_request_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_resume_response(cls, arg: DownstreamResumeResponsePB) -> DownstreamResumeResponse:
        return DownstreamResumeResponse(
            request_id=arg.request_id,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.downstream_resume_response_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_close_request(cls, arg: DownstreamCloseRequestPB) -> DownstreamCloseRequest:
        return DownstreamCloseRequest(
            request_id=arg.request_id,
            stream_id=UUID(bytes=arg.stream_id),
            extension_fields=cls.downstream_close_request_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_close_response(cls, arg: DownstreamCloseResponsePB) -> DownstreamCloseResponse:
        return DownstreamCloseResponse(
            request_id=arg.request_id,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.downstream_close_response_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_chunk(cls, arg: DownstreamChunkPB) -> DownstreamChunk:
        return DownstreamChunk(
            stream_id_alias=arg.stream_id_alias,
            upstream_or_alias=cls.upstream_or_alias(arg),
            stream_chunk=_common.ProtoToWire.stream_chunk(arg.stream_chunk),
            extension_fields=cls.downstream_chunk_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_or_alias(cls, arg: DownstreamChunkPB) -> UpstreamInfo | int:
        which_one_of = arg.WhichOneof("upstream_or_alias")
        if which_one_of == "upstream_info":
            return cls.upstream_info(arg.upstream_info)

        if which_one_of == "upstream_alias":
            return arg.upstream_alias

        raise ISCPMalformedMessageError(f"unrecognized upstream_or_alias{arg}")

    @classmethod
    def downstream_chunk_ack(cls, arg: DownstreamChunkAckPB) -> DownstreamChunkAck:
        return DownstreamChunkAck(
            stream_id_alias=arg.stream_id_alias,
            ack_id=arg.ack_id,
            results=cls.downstream_chunk_results(arg.results),
            upstream_aliases=cls.upstream_aliases(arg.upstream_aliases),
            data_id_aliases=_common.ProtoToWire.data_id_aliases(arg.data_id_aliases),
            extension_fields=cls.downstream_chunk_ack_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_chunk_ack_complete(cls, arg: DownstreamChunkAckCompletePB) -> DownstreamChunkAckComplete:
        return DownstreamChunkAckComplete(
            stream_id_alias=arg.stream_id_alias,
            ack_id=arg.ack_id,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.downstream_chunk_ack_complete_extension_fields(arg.extension_fields),
        )

    @classmethod
    def downstream_metadata(cls, arg: DownstreamMetadataPB) -> DownstreamMetadata:
        return DownstreamMetadata(
            request_id=arg.request_id,
            stream_id_alias=arg.stream_id_alias,
            metadata=cls.metadata(arg),
            source_node_id=arg.source_node_id,
            extension_fields=cls.downstream_metadata_extension_fields(arg.extension_fields),
        )

    @classmethod
    def metadata(cls, arg: DownstreamMetadataPB) -> Metadata:

        which_one_of = arg.WhichOneof("metadata")

        if which_one_of == "base_time":
            return _metadata.ProtoToWire.base_time(arg.base_time)
        if which_one_of == "upstream_open":
            return _metadata.ProtoToWire.upstream_open(arg.upstream_open)
        if which_one_of == "upstream_abnormal_close":
            return _metadata.ProtoToWire.upstream_abnormal_close(arg.upstream_abnormal_close)
        if which_one_of == "upstream_resume":
            return _metadata.ProtoToWire.upstream_resume(arg.upstream_resume)
        if which_one_of == "upstream_normal_close":
            return _metadata.ProtoToWire.upstream_normal_close(arg.upstream_normal_close)
        if which_one_of == "downstream_open":
            return _metadata.ProtoToWire.downstream_open(arg.downstream_open)
        if which_one_of == "downstream_abnormal_close":
            return _metadata.ProtoToWire.downstream_abnormal_close(arg.downstream_abnormal_close)
        if which_one_of == "downstream_resume":
            return _metadata.ProtoToWire.downstream_resume(arg.downstream_resume)
        if which_one_of == "downstream_normal_close":
            return _metadata.ProtoToWire.downstream_normal_close(arg.downstream_normal_close)

        raise ISCPMalformedMessageError(f"unrecognized metadata {arg}")

    @classmethod
    def downstream_metadata_ack(cls, arg: DownstreamMetadataAckPB) -> DownstreamMetadataAck:
        return DownstreamMetadataAck(
            request_id=arg.request_id,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.downstream_metadata_ack_extension_fields(arg.extension_fields),
        )

    #
    # Internals
    #

    @classmethod
    def upstream_aliases(cls, arg: Dict[int, UpstreamInfoPB]) -> Dict[int, UpstreamInfo]:
        return {k: cls.upstream_info(v) for k, v in arg.items()}

    @classmethod
    def upstream_info(cls, arg: UpstreamInfoPB) -> UpstreamInfo:
        return UpstreamInfo(
            session_id=arg.session_id,
            stream_id=UUID(bytes=arg.stream_id),
            source_node_id=arg.source_node_id,
        )

    @classmethod
    def downstream_chunk_results(cls, arg: List[DownstreamChunkResultPB]) -> List[DownstreamChunkResult]:
        return [cls.downstream_chunk_result(v) for v in arg]

    @classmethod
    def downstream_chunk_result(cls, arg: DownstreamChunkResultPB) -> DownstreamChunkResult:
        return DownstreamChunkResult(
            stream_id_of_upstream=UUID(bytes=arg.stream_id_of_upstream),
            sequence_number_in_upstream=arg.sequence_number_in_upstream,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.downstream_chunk_result_extension_fields(arg.extension_fields),
        )
