__all__ = ["WireToProto", "ProtoToWire"]


from typing import List
from uuid import UUID

from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamChunkAckExtensionFields as UpstreamChunkAckExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamChunkExtensionFields as UpstreamChunkExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamChunkResultExtensionFields as UpstreamChunkResultExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamCloseRequestExtensionFields as UpstreamCloseRequestExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamCloseResponseExtensionFields as UpstreamCloseResponseExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamMetadataAckExtensionFields as UpstreamMetadataAckExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamMetadataExtensionFields as UpstreamMetadataExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamOpenRequestExtensionFields as UpstreamOpenRequestExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamOpenResponseExtensionFields as UpstreamOpenResponseExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamResumeRequestExtensionFields as UpstreamResumeRequestExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.upstream_pb2 import (
    UpstreamResumeResponseExtensionFields as UpstreamResumeResponseExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import UpstreamChunk as UpstreamChunkPB
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import UpstreamChunkAck as UpstreamChunkAckPB
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamChunkResult as UpstreamChunkResultPB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamCloseRequest as UpstreamCloseRequestPB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamCloseResponse as UpstreamCloseResponsePB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import UpstreamMetadata as UpstreamMetadataPB
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamMetadataAck as UpstreamMetadataAckPB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamOpenRequest as UpstreamOpenRequestPB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamOpenResponse as UpstreamOpenResponsePB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamResumeRequest as UpstreamResumeRequestPB,
)
from iscp._encoding._codegen.iscp2.v1.upstream_pb2 import (
    UpstreamResumeResponse as UpstreamResumeResponsePB,
)
from iscp._exceptions import ISCPMalformedMessageError
from iscp._message import (
    BaseTime,
    Metadata,
    UpstreamChunk,
    UpstreamChunkAck,
    UpstreamChunkAckExtensionFields,
    UpstreamChunkExtensionFields,
    UpstreamChunkResult,
    UpstreamChunkResultExtensionFields,
    UpstreamCloseRequest,
    UpstreamCloseRequestExtensionFields,
    UpstreamCloseResponse,
    UpstreamCloseResponseExtensionFields,
    UpstreamMetadata,
    UpstreamMetadataAck,
    UpstreamMetadataAckExtensionFields,
    UpstreamMetadataExtensionFields,
    UpstreamOpenRequest,
    UpstreamOpenRequestExtensionFields,
    UpstreamOpenResponse,
    UpstreamOpenResponseExtensionFields,
    UpstreamResumeRequest,
    UpstreamResumeRequestExtensionFields,
    UpstreamResumeResponse,
    UpstreamResumeResponseExtensionFields,
    DateTime,
)

from . import _common, _metadata, _result_code


class WireToProto(object):
    @classmethod
    def upstream_metadata_ack_extension_fields(
        cls,
        _: UpstreamMetadataAckExtensionFields,
    ) -> UpstreamMetadataAckExtensionFieldsPB:
        res = UpstreamMetadataAckExtensionFieldsPB()
        return res

    @classmethod
    def upstream_metadata_extension_fields(
        cls,
        arg: UpstreamMetadataExtensionFields,
    ) -> UpstreamMetadataExtensionFieldsPB:
        res = UpstreamMetadataExtensionFieldsPB()
        res.persist = arg.persist  # type: ignore
        return res

    @classmethod
    def upstream_chunk_ack_extension_fields(
        cls,
        _: UpstreamChunkAckExtensionFields,
    ) -> UpstreamChunkAckExtensionFieldsPB:
        res = UpstreamChunkAckExtensionFieldsPB()
        return res

    @classmethod
    def upstream_chunk_extension_fields(
        cls,
        _: UpstreamChunkExtensionFields,
    ) -> UpstreamChunkExtensionFieldsPB:
        res = UpstreamChunkExtensionFieldsPB()
        return res

    @classmethod
    def upstream_close_response_extension_fields(
        cls,
        _: UpstreamCloseResponseExtensionFields,
    ) -> UpstreamCloseResponseExtensionFieldsPB:
        res = UpstreamCloseResponseExtensionFieldsPB()
        return res

    @classmethod
    def upstream_close_request_extension_fields(
        cls,
        arg: UpstreamCloseRequestExtensionFields,
    ) -> UpstreamCloseRequestExtensionFieldsPB:
        res = UpstreamCloseRequestExtensionFieldsPB()
        res.close_session = arg.close_session  # type: ignore
        return res

    @classmethod
    def upstream_resume_response_extension_fields(
        cls,
        _: UpstreamResumeResponseExtensionFields,
    ) -> UpstreamResumeResponseExtensionFieldsPB:
        res = UpstreamResumeResponseExtensionFieldsPB()
        return res

    @classmethod
    def upstream_chunk_result_extension_fields(
        cls,
        _: UpstreamChunkResultExtensionFieldsPB,
    ) -> UpstreamChunkResultExtensionFieldsPB:
        res = UpstreamChunkResultExtensionFieldsPB()
        return res

    @classmethod
    def upstream_resume_request_extension_fields(
        cls,
        _: UpstreamResumeRequestExtensionFields,
    ) -> UpstreamResumeRequestExtensionFieldsPB:
        res = UpstreamResumeRequestExtensionFieldsPB()
        return res

    @classmethod
    def upstream_open_response_extension_fields(
        cls,
        _: UpstreamOpenResponseExtensionFields,
    ) -> UpstreamOpenResponseExtensionFieldsPB:
        res = UpstreamOpenResponseExtensionFieldsPB()
        return res

    @classmethod
    def upstream_open_request_extension_fields(
        cls,
        arg: UpstreamOpenRequestExtensionFields,
    ) -> UpstreamOpenRequestExtensionFieldsPB:
        res = UpstreamOpenRequestExtensionFieldsPB()
        res.persist = arg.persist  # type: ignore
        return res

    @classmethod
    def upstream_open_request(cls, arg: UpstreamOpenRequest) -> UpstreamOpenRequestPB:
        res = UpstreamOpenRequestPB()
        res.session_id = arg.session_id
        res.request_id = arg.request_id
        res.expiry_interval = arg.expiry_interval
        res.data_ids.extend(_common.WireToProto.data_ids(arg.data_ids))
        res.qos = _common.WireToProto.qos(arg.qos)
        res.ack_interval = arg.ack_interval
        res.extension_fields.CopyFrom(cls.upstream_open_request_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_open_response(cls, arg: UpstreamOpenResponse) -> UpstreamOpenResponsePB:
        res = UpstreamOpenResponsePB()
        res.request_id = arg.request_id
        res.assigned_stream_id = arg.assigned_stream_id.bytes
        res.assigned_stream_id_alias = arg.assigned_stream_id_alias
        _common.WireToProto.data_id_aliases(res.data_id_aliases, arg.data_id_aliases)
        res.server_time = arg.server_time.unix_nano()
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.upstream_open_response_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_resume_request(cls, arg: UpstreamResumeRequest) -> UpstreamResumeRequestPB:
        res = UpstreamResumeRequestPB()
        res.request_id = arg.request_id
        res.stream_id = arg.stream_id.bytes
        res.extension_fields.CopyFrom(cls.upstream_resume_request_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_resume_response(
        cls,
        arg: UpstreamResumeResponse,
    ) -> UpstreamResumeResponsePB:
        res = UpstreamResumeResponsePB()
        res.request_id = arg.request_id
        res.assigned_stream_id_alias = arg.assigned_stream_id_alias
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.upstream_resume_response_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_close_request(cls, arg: UpstreamCloseRequest) -> UpstreamCloseRequestPB:
        res = UpstreamCloseRequestPB()
        res.request_id = arg.request_id
        res.stream_id = arg.stream_id.bytes
        res.total_data_points = arg.total_data_points
        res.final_sequence_number = arg.final_sequence_number
        res.extension_fields.CopyFrom(cls.upstream_close_request_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_close_response(cls, arg: UpstreamCloseResponse) -> UpstreamCloseResponsePB:
        res = UpstreamCloseResponsePB()
        res.request_id = arg.request_id
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.upstream_close_response_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_chunk(cls, arg: UpstreamChunk) -> UpstreamChunkPB:
        res = UpstreamChunkPB()
        res.stream_id_alias = arg.stream_id_alias
        res.stream_chunk.CopyFrom(_common.WireToProto.stream_chunk(arg.stream_chunk))
        res.data_ids.extend(_common.WireToProto.data_ids(arg.data_ids))
        res.extension_fields.CopyFrom(cls.upstream_chunk_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_chunk_results(
        cls,
        arg: List[UpstreamChunkResult],
    ) -> List[UpstreamChunkResultPB]:
        return [cls.upstream_chunk_result(v) for v in arg]

    @classmethod
    def upstream_chunk_result(cls, arg: UpstreamChunkResult) -> UpstreamChunkResultPB:
        res = UpstreamChunkResultPB()
        res.sequence_number = arg.sequence_number
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.upstream_chunk_result_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_chunk_ack(cls, arg: UpstreamChunkAck) -> UpstreamChunkAckPB:
        res = UpstreamChunkAckPB()
        res.stream_id_alias = arg.stream_id_alias
        res.results.extend(cls.upstream_chunk_results(arg.results))
        _common.WireToProto.data_id_aliases(res.data_id_aliases, arg.data_id_aliases)
        res.extension_fields.CopyFrom(cls.upstream_chunk_ack_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def upstream_metadata(cls, arg: UpstreamMetadata) -> UpstreamMetadataPB:
        res = UpstreamMetadataPB()
        res.request_id = arg.request_id
        cls.metadata(res, arg.metadata)
        res.extension_fields.CopyFrom(cls.upstream_metadata_extension_fields(arg.extension_fields))
        return res

    @classmethod
    def metadata(cls, res: UpstreamMetadataPB, arg: Metadata):
        if isinstance(arg, BaseTime):
            res.base_time.CopyFrom(_metadata.WireToProto.base_time(arg))
            return

        raise ISCPMalformedMessageError(f"unrecognized metadata {arg}")

    @classmethod
    def upstream_metadata_ack(cls, arg: UpstreamMetadataAck) -> UpstreamMetadataAckPB:
        res = UpstreamMetadataAckPB()
        res.request_id = arg.request_id
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)
        res.result_string = arg.result_string
        res.extension_fields.CopyFrom(cls.upstream_metadata_ack_extension_fields(arg.extension_fields))
        return res


class ProtoToWire(object):
    @classmethod
    def upstream_metadata_ack_extension_fields(
        cls,
        _: UpstreamMetadataAckExtensionFieldsPB,
    ) -> UpstreamMetadataAckExtensionFields:
        return UpstreamMetadataAckExtensionFields()

    @classmethod
    def upstream_metadata_extension_fields(
        cls,
        arg: UpstreamMetadataExtensionFieldsPB,
    ) -> UpstreamMetadataExtensionFields:
        return UpstreamMetadataExtensionFields(persist=arg.persist)

    @classmethod
    def upstream_chunk_ack_extension_fields(
        cls,
        _: UpstreamChunkAckExtensionFieldsPB,
    ) -> UpstreamChunkAckExtensionFields:
        return UpstreamChunkAckExtensionFields()

    @classmethod
    def upstream_chunk_extension_fields(
        cls,
        _: UpstreamChunkExtensionFieldsPB,
    ) -> UpstreamChunkExtensionFields:
        return UpstreamChunkExtensionFields()

    @classmethod
    def upstream_close_response_extension_fields(
        cls,
        _: UpstreamCloseResponseExtensionFieldsPB,
    ) -> UpstreamCloseResponseExtensionFields:
        return UpstreamCloseResponseExtensionFields()

    @classmethod
    def upstream_close_request_extension_fields(
        cls,
        arg: UpstreamCloseRequestExtensionFieldsPB,
    ) -> UpstreamCloseRequestExtensionFields:
        return UpstreamCloseRequestExtensionFields(close_session=arg.close_session)

    @classmethod
    def upstream_resume_response_extension_fields(
        cls,
        _: UpstreamResumeResponseExtensionFieldsPB,
    ) -> UpstreamResumeResponseExtensionFields:
        return UpstreamResumeResponseExtensionFields()

    @classmethod
    def upstream_resume_request_extension_fields(
        cls,
        _: UpstreamResumeRequestExtensionFieldsPB,
    ) -> UpstreamResumeRequestExtensionFields:
        return UpstreamResumeRequestExtensionFields()

    @classmethod
    def upstream_open_response_extension_fields(
        cls,
        _: UpstreamOpenResponseExtensionFieldsPB,
    ) -> UpstreamOpenResponseExtensionFields:
        return UpstreamOpenResponseExtensionFields()

    @classmethod
    def upstream_chunk_result_extension_fields(
        cls,
        _: UpstreamChunkResultExtensionFieldsPB,
    ) -> UpstreamChunkResultExtensionFields:
        return UpstreamChunkResultExtensionFields()

    @classmethod
    def upstream_open_request_extension_fields(
        cls,
        arg: UpstreamOpenRequestExtensionFieldsPB,
    ) -> UpstreamOpenRequestExtensionFields:
        return UpstreamOpenRequestExtensionFields(persist=arg.persist)

    @classmethod
    def upstream_open_request(cls, arg: UpstreamOpenRequestPB) -> UpstreamOpenRequest:
        return UpstreamOpenRequest(
            session_id=arg.session_id,  # type: ignore
            request_id=arg.request_id,  # type: ignore
            expiry_interval=arg.expiry_interval,
            data_ids=_common.ProtoToWire.data_ids(arg.data_ids),  # type: ignore
            qos=_common.ProtoToWire.qos(arg.qos),  # type: ignore
            ack_interval=arg.ack_interval,
            extension_fields=cls.upstream_open_request_extension_fields(
                arg.extension_fields,  # type: ignore
            ),
        )

    @classmethod
    def upstream_open_response(cls, arg: UpstreamOpenResponsePB) -> UpstreamOpenResponse:
        res = UpstreamOpenResponse(
            request_id=arg.request_id,  # type: ignore
            assigned_stream_id=UUID(bytes=arg.assigned_stream_id),  # type: ignore
            assigned_stream_id_alias=arg.assigned_stream_id_alias,  # type: ignore
            data_id_aliases=_common.ProtoToWire.data_id_aliases(arg.data_id_aliases),  # type: ignore
            server_time=DateTime.from_unix_nano(arg.server_time),
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),  # type: ignore
            result_string=arg.result_string,  # type: ignore
            extension_fields=cls.upstream_open_response_extension_fields(arg.extension_fields),  # type: ignore
        )
        return res

    @classmethod
    def upstream_resume_request(cls, arg: UpstreamResumeRequestPB) -> UpstreamResumeRequest:
        return UpstreamResumeRequest(
            request_id=arg.request_id,
            stream_id=UUID(bytes=arg.stream_id),
            extension_fields=cls.upstream_resume_request_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_resume_response(
        cls,
        arg: UpstreamResumeResponsePB,
    ) -> UpstreamResumeResponse:
        return UpstreamResumeResponse(
            request_id=arg.request_id,
            assigned_stream_id_alias=arg.assigned_stream_id_alias,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),  # type: ignore
            result_string=arg.result_string,
            extension_fields=cls.upstream_resume_response_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_close_request(cls, arg: UpstreamCloseRequestPB) -> UpstreamCloseRequest:
        return UpstreamCloseRequest(
            request_id=arg.request_id,
            stream_id=UUID(bytes=arg.stream_id),
            total_data_points=arg.total_data_points,
            final_sequence_number=arg.final_sequence_number,
            extension_fields=cls.upstream_close_request_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_close_response(cls, arg: UpstreamCloseResponsePB) -> UpstreamCloseResponse:
        return UpstreamCloseResponse(
            request_id=arg.request_id,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),  # type: ignore
            result_string=arg.result_string,
            extension_fields=cls.upstream_close_response_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_chunk(cls, arg: UpstreamChunkPB) -> UpstreamChunk:
        return UpstreamChunk(
            stream_id_alias=arg.stream_id_alias,
            stream_chunk=_common.ProtoToWire.stream_chunk(arg.stream_chunk),
            data_ids=_common.ProtoToWire.data_ids(arg.data_ids),  # type: ignore
            extension_fields=cls.upstream_chunk_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_chunk_results(
        cls,
        arg: List[UpstreamChunkResultPB],
    ) -> List[UpstreamChunkResult]:
        return [cls.upstream_chunk_result(v) for v in arg]

    @classmethod
    def upstream_chunk_result(cls, arg: UpstreamChunkResultPB) -> UpstreamChunkResult:
        return UpstreamChunkResult(
            sequence_number=arg.sequence_number,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),
            result_string=arg.result_string,
            extension_fields=cls.upstream_chunk_result_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_chunk_ack(cls, arg: UpstreamChunkAckPB) -> UpstreamChunkAck:
        return UpstreamChunkAck(
            stream_id_alias=arg.stream_id_alias,
            results=cls.upstream_chunk_results(arg.results),
            data_id_aliases=_common.ProtoToWire.data_id_aliases(arg.data_id_aliases),  # type: ignore
            extension_fields=cls.upstream_chunk_ack_extension_fields(arg.extension_fields),
        )

    @classmethod
    def upstream_metadata(cls, arg: UpstreamMetadataPB) -> UpstreamMetadata:
        return UpstreamMetadata(
            request_id=arg.request_id,
            metadata=cls.metadata(arg),
            extension_fields=cls.upstream_metadata_extension_fields(arg.extension_fields),
        )

    @classmethod
    def metadata(cls, arg: UpstreamMetadataPB) -> Metadata:

        which_one_of = arg.WhichOneof("metadata")
        if which_one_of == "base_time":
            return _metadata.ProtoToWire.base_time(arg.base_time)

        raise ISCPMalformedMessageError(f"unrecognized metadata {arg}")

    @classmethod
    def upstream_metadata_ack(cls, arg: UpstreamMetadataAckPB) -> UpstreamMetadataAck:
        return UpstreamMetadataAck(
            request_id=arg.request_id,
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),  # type: ignore
            result_string=arg.result_string,
            extension_fields=cls.upstream_metadata_ack_extension_fields(arg.extension_fields),
        )
