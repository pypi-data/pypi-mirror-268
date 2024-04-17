from typing import Optional
from uuid import UUID

from iscp._encoding._codegen.iscp2.v1.connection_pb2 import ConnectRequest as ConnectRequestPB
from iscp._encoding._codegen.iscp2.v1.connection_pb2 import ConnectResponse as ConnectResponsePB
from iscp._encoding._codegen.iscp2.v1.connection_pb2 import Disconnect as DisconnectPB
from iscp._encoding._codegen.iscp2.v1.extensions.connection_pb2 import (
    ConnectRequestExtensionFields as ConnectRequestExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.connection_pb2 import (
    ConnectResponseExtensionFields as ConnectResponseExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.connection_pb2 import (
    DisconnectExtensionFields as DisconnectExtensionFieldsPB,
)
from iscp._encoding._codegen.iscp2.v1.extensions.connection_pb2 import (
    IntdashExtensionFields as IntdashExtensionFieldsPB,
)
from iscp._message import (
    ConnectRequest,
    ConnectRequestExtensionFields,
    ConnectResponse,
    ConnectResponseExtensionFields,
    Disconnect,
    DisconnectExtensionFields,
    IntdashExtensionFields,
)

from . import _result_code

__all__ = ["WireToProto", "ProtoToWire"]


class WireToProto(object):
    @classmethod
    def connect_request(cls, arg: ConnectRequest) -> ConnectRequestPB:
        res = ConnectRequestPB()
        res.request_id = arg.request_id  # type: ignore
        res.node_id = arg.node_id  # type: ignore
        res.extension_fields.CopyFrom(cls.connect_request_extension_fields(arg.extension_fields))  # type: ignore
        res.protocol_version = arg.protocol_version  # type: ignore
        res.ping_interval = int(arg.ping_interval)  # type: ignore
        res.ping_timeout = int(arg.ping_timeout)  # type: ignore
        return res

    @classmethod
    def connect_response(cls, arg: ConnectResponse) -> ConnectResponsePB:
        res = ConnectResponsePB()
        res.request_id = arg.request_id  # type: ignore
        res.protocol_version = arg.protocol_version  # type: ignore
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)  # type: ignore
        res.result_string = arg.result_string  # type: ignore
        res.extension_fields.CopyFrom(cls.connect_response_extension_fields(arg.extension_fields))  # type: ignore
        return res

    @classmethod
    def disconnect(cls, arg: Disconnect) -> DisconnectPB:
        res = DisconnectPB()
        res.result_code = _result_code.WireToProto.result_code(arg.result_code)  # type: ignore
        res.result_string = arg.result_string  # type: ignore
        res.extension_fields.CopyFrom(  # type: ignore
            cls.disconnect_extension_fields(arg.extension_fields),
        )
        return res

    @classmethod
    def connect_request_extension_fields(
        cls,
        arg: Optional[ConnectRequestExtensionFields],
    ) -> ConnectRequestExtensionFieldsPB:
        res = ConnectRequestExtensionFieldsPB()
        if arg is None:
            return res
        res.access_token = arg.access_token  # type: ignore
        res.intdash.CopyFrom(cls.intdash_extension_fields(arg.intdash))  # type: ignore
        return res

    @classmethod
    def connect_response_extension_fields(
        cls,
        _: ConnectResponseExtensionFields,
    ) -> ConnectResponseExtensionFieldsPB:
        return ConnectResponseExtensionFieldsPB()

    @classmethod
    def disconnect_extension_fields(
        cls,
        _: DisconnectExtensionFields,
    ) -> DisconnectExtensionFieldsPB:  # type: ignore
        return DisconnectExtensionFieldsPB()

    @classmethod
    def intdash_extension_fields(
        cls,
        arg: IntdashExtensionFields,
    ) -> IntdashExtensionFieldsPB:
        res = IntdashExtensionFieldsPB()
        res.project_uuid = str(arg.project_uuid)  # type: ignore
        return res


class ProtoToWire(object):
    @classmethod
    def connect_request(cls, arg: ConnectRequestPB) -> ConnectRequest:
        return ConnectRequest(
            request_id=arg.request_id,  # type: ignore
            node_id=arg.node_id,  # type: ignore
            extension_fields=cls.connect_request_extension_fields(arg.extension_fields),  # type: ignore
            protocol_version=arg.protocol_version,  # type: ignore
            ping_interval=arg.ping_interval,  # type: ignore
            ping_timeout=arg.ping_timeout,  # type: ignore
        )

    @classmethod
    def connect_response(cls, arg: ConnectResponsePB) -> ConnectResponse:
        return ConnectResponse(
            request_id=arg.request_id,  # type: ignore
            protocol_version=arg.protocol_version,  # type: ignore
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),  # type: ignore
            result_string=arg.result_string,  # type: ignore
            extension_fields=cls.connect_response_extension_fields(arg.extension_fields),  # type: ignore
        )

    @classmethod
    def disconnect(cls, arg: DisconnectPB) -> Disconnect:
        return Disconnect(
            result_code=_result_code.ProtoToWire.result_code(arg.result_code),  # type: ignore
            result_string=arg.result_string,  # type: ignore
            extension_fields=cls.disconnect_extension_fields(
                arg.extension_fields,  # type: ignore
            ),
        )

    @classmethod
    def connect_response_extension_fields(
        cls,
        _: ConnectResponseExtensionFieldsPB,
    ) -> ConnectResponseExtensionFields:
        return ConnectResponseExtensionFields()

    @classmethod
    def connect_request_extension_fields(
        cls,
        arg: ConnectRequestExtensionFieldsPB,
    ) -> ConnectRequestExtensionFields:
        return ConnectRequestExtensionFields(
            access_token=arg.access_token,  # type: ignore
            intdash=cls.intdash_extension_fields(arg.intdash),  # type: ignore
        )

    @classmethod
    def disconnect_extension_fields(
        cls,
        _: DisconnectExtensionFieldsPB,
    ) -> DisconnectExtensionFields:  # type: ignore
        return DisconnectExtensionFields()

    @classmethod
    def intdash_extension_fields(
        cls,
        arg: IntdashExtensionFieldsPB,
    ) -> IntdashExtensionFields:
        return IntdashExtensionFields(project_uuid=UUID(arg.project_uuid))  # type: ignore
