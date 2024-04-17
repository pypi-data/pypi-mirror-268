from iscp._encoding._codegen.iscp2.v1.result_code_pb2 import ResultCode as ResultCodePB
from iscp._message import ResultCode

__all__ = ["WireToProto", "ProtoToWire"]


class WireToProto(object):
    @classmethod
    def result_code(cls, arg: ResultCode) -> ResultCodePB:  # type: ignore
        return getattr(ResultCodePB, arg.name)


class ProtoToWire(object):
    @classmethod
    def result_code(cls, arg: ResultCodePB) -> ResultCode:  # type: ignore
        return ResultCode[ResultCodePB.Name(arg)]
