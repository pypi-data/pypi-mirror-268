from ...._encoding._codegen.iscp2.v1.message_pb2 import Message as MessagePB
from ...._exceptions import ISCPMalformedMessageError
from ...._message import (
    ConnectRequest,
    ConnectResponse,
    Disconnect,
    DownstreamChunkAck,
    DownstreamChunkAckComplete,
    DownstreamCloseRequest,
    DownstreamCloseResponse,
    DownstreamMetadataAck,
    DownstreamOpenRequest,
    DownstreamOpenResponse,
    DownstreamResumeRequest,
    DownstreamResumeResponse,
    Message,
    Ping,
    Pong,
    UpstreamCall,
    UpstreamCallAck,
    UpstreamChunk,
    UpstreamChunkAck,
    UpstreamCloseRequest,
    UpstreamCloseResponse,
    UpstreamMetadata,
    UpstreamMetadataAck,
    UpstreamOpenRequest,
    UpstreamOpenResponse,
    UpstreamResumeRequest,
    UpstreamResumeResponse,
)

from ...._message._downstream import (
    DownstreamChunk,
    DownstreamMetadata,
)

from ...._message._e2e import (
    DownstreamCall,
)

from . import _connection, _downstream, _e2e_call, _ping_pong, _upstream

__all__ = ["WireToProto", "ProtoToWire"]


class WireToProto(object):
    @staticmethod
    def convert(arg: Message) -> MessagePB:
        res = MessagePB()

        if isinstance(arg, ConnectRequest):
            res.connect_request.CopyFrom(_connection.WireToProto.connect_request(arg))  # type: ignore
            return res

        if isinstance(arg, ConnectResponse):
            res.connect_response.CopyFrom(_connection.WireToProto.connect_response(arg))  # type: ignore
            return res

        if isinstance(arg, Disconnect):
            res.disconnect.CopyFrom(_connection.WireToProto.disconnect(arg))  # type: ignore
            return res

        if isinstance(arg, UpstreamOpenRequest):
            res.upstream_open_request.CopyFrom(_upstream.WireToProto.upstream_open_request(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamOpenResponse):
            res.upstream_open_response.CopyFrom(_upstream.WireToProto.upstream_open_response(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamResumeRequest):
            res.upstream_resume_request.CopyFrom(_upstream.WireToProto.upstream_resume_request(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamResumeResponse):
            res.upstream_resume_response.CopyFrom(_upstream.WireToProto.upstream_resume_response(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamCloseRequest):
            res.upstream_close_request.CopyFrom(_upstream.WireToProto.upstream_close_request(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamCloseResponse):
            res.upstream_close_response.CopyFrom(_upstream.WireToProto.upstream_close_response(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamChunk):
            res.upstream_chunk.CopyFrom(_upstream.WireToProto.upstream_chunk(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamChunkAck):
            res.upstream_chunk_ack.CopyFrom(_upstream.WireToProto.upstream_chunk_ack(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamMetadata):
            res.upstream_metadata.CopyFrom(_upstream.WireToProto.upstream_metadata(arg))  # type: ignore
            return res
        if isinstance(arg, UpstreamMetadataAck):
            res.upstream_metadata_ack.CopyFrom(_upstream.WireToProto.upstream_metadata_ack(arg))  # type: ignore
            return res

        if isinstance(arg, DownstreamOpenRequest):
            res.downstream_open_request.CopyFrom(_downstream.WireToProto.downstream_open_request(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamOpenResponse):
            res.downstream_open_response.CopyFrom(_downstream.WireToProto.downstream_open_response(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamResumeRequest):
            res.downstream_resume_request.CopyFrom(_downstream.WireToProto.downstream_resume_request(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamResumeResponse):
            res.downstream_resume_response.CopyFrom(_downstream.WireToProto.downstream_resume_response(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamCloseRequest):
            res.downstream_close_request.CopyFrom(_downstream.WireToProto.downstream_close_request(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamCloseResponse):
            res.downstream_close_response.CopyFrom(_downstream.WireToProto.downstream_close_response(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamChunk):
            res.downstream_chunk.CopyFrom(_downstream.WireToProto.downstream_chunk(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamChunkAck):
            res.downstream_chunk_ack.CopyFrom(_downstream.WireToProto.downstream_chunk_ack(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamChunkAckComplete):
            res.downstream_chunk_ack_complete.CopyFrom(_downstream.WireToProto.downstream_chunk_ack_complete(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamMetadata):
            res.downstream_metadata.CopyFrom(_downstream.WireToProto.downstream_metadata(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamMetadataAck):
            res.downstream_metadata_ack.CopyFrom(_downstream.WireToProto.downstream_metadata_ack(arg))  # type: ignore
            return res

        if isinstance(arg, UpstreamCall):
            res.upstream_call.CopyFrom(_e2e_call.WireToProto.upstream_call(arg))  # type: ignore
            return res

        if isinstance(arg, UpstreamCallAck):
            res.upstream_call_ack.CopyFrom(_e2e_call.WireToProto.upstream_call_ack(arg))  # type: ignore
            return res
        if isinstance(arg, DownstreamCall):
            res.downstream_call.CopyFrom(_e2e_call.WireToProto.downstream_call(arg))  # type: ignore
            return res

        if isinstance(arg, Ping):
            res.ping.CopyFrom(_ping_pong.WireToProto.ping(arg))  # type: ignore
            return res
        if isinstance(arg, Pong):
            res.pong.CopyFrom(_ping_pong.WireToProto.pong(arg))  # type: ignore
            return res

        raise ISCPMalformedMessageError()


class ProtoToWire(object):
    @staticmethod
    def convert(arg: MessagePB) -> Message:
        msg = arg.WhichOneof("message")  # type: ignore

        if msg == "connect_request":
            return _connection.ProtoToWire.connect_request(arg.connect_request)  # type: ignore

        if msg == "connect_response":
            return _connection.ProtoToWire.connect_response(arg.connect_response)  # type: ignore

        if msg == "disconnect":
            return _connection.ProtoToWire.disconnect(arg.disconnect)  # type: ignore

        if msg == "upstream_open_request":
            return _upstream.ProtoToWire.upstream_open_request(arg.upstream_open_request)  # type: ignore

        if msg == "upstream_open_response":
            return _upstream.ProtoToWire.upstream_open_response(arg.upstream_open_response)  # type: ignore

        if msg == "upstream_resume_request":
            return _upstream.ProtoToWire.upstream_resume_request(arg.upstream_resume_request)  # type: ignore

        if msg == "upstream_resume_response":
            return _upstream.ProtoToWire.upstream_resume_response(arg.upstream_resume_response)  # type: ignore

        if msg == "upstream_close_request":
            return _upstream.ProtoToWire.upstream_close_request(arg.upstream_close_request)  # type: ignore

        if msg == "upstream_close_response":
            return _upstream.ProtoToWire.upstream_close_response(arg.upstream_close_response)  # type: ignore

        if msg == "upstream_chunk":
            return _upstream.ProtoToWire.upstream_chunk(arg.upstream_chunk)  # type: ignore

        if msg == "upstream_chunk_ack":
            return _upstream.ProtoToWire.upstream_chunk_ack(arg.upstream_chunk_ack)  # type: ignore

        if msg == "upstream_metadata":
            return _upstream.ProtoToWire.upstream_metadata(arg.upstream_metadata)  # type: ignore

        if msg == "upstream_metadata_ack":
            return _upstream.ProtoToWire.upstream_metadata_ack(arg.upstream_metadata_ack)  # type: ignore

        if msg == "downstream_open_request":
            return _downstream.ProtoToWire.downstream_open_request(arg.downstream_open_request)  # type: ignore
        if msg == "downstream_open_response":
            return _downstream.ProtoToWire.downstream_open_response(arg.downstream_open_response)  # type: ignore
        if msg == "downstream_resume_request":
            return _downstream.ProtoToWire.downstream_resume_request(arg.downstream_resume_request)  # type: ignore
        if msg == "downstream_resume_response":
            return _downstream.ProtoToWire.downstream_resume_response(arg.downstream_resume_response)  # type: ignore
        if msg == "downstream_close_request":
            return _downstream.ProtoToWire.downstream_close_request(arg.downstream_close_request)  # type: ignore
        if msg == "downstream_close_response":
            return _downstream.ProtoToWire.downstream_close_response(arg.downstream_close_response)  # type: ignore
        if msg == "downstream_chunk":
            return _downstream.ProtoToWire.downstream_chunk(arg.downstream_chunk)  # type: ignore
        if msg == "downstream_chunk_ack":
            return _downstream.ProtoToWire.downstream_chunk_ack(arg.downstream_chunk_ack)  # type: ignore
        if msg == "downstream_chunk_ack_complete":
            return _downstream.ProtoToWire.downstream_chunk_ack_complete(arg.downstream_chunk_ack_complete)  # type: ignore
        if msg == "downstream_metadata":
            return _downstream.ProtoToWire.downstream_metadata(arg.downstream_metadata)  # type: ignore
        if msg == "downstream_metadata_ack":
            return _downstream.ProtoToWire.downstream_metadata_ack(arg.downstream_metadata_ack)  # type: ignore

        if msg == "upstream_call":
            return _e2e_call.ProtoToWire.upstream_call(arg.upstream_call)  # type: ignore

        if msg == "upstream_call_ack":
            return _e2e_call.ProtoToWire.upstream_call_ack(arg.upstream_call_ack)  # type: ignore

        if msg == "downstream_call":
            return _e2e_call.ProtoToWire.downstream_call(arg.downstream_call)  # type: ignore

        if msg == "ping":
            return _ping_pong.ProtoToWire.ping(arg.ping)  # type: ignore
        if msg == "pong":
            return _ping_pong.ProtoToWire.pong(arg.pong)  # type: ignore

        raise ISCPMalformedMessageError(message=f"infalid type: {msg}")
