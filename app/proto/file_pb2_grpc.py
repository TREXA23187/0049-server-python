# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import file_pb2 as file__pb2


class FileServiceStub(object):
    """python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./file.proto

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadFile = channel.stream_unary(
            '/proto.FileService/UploadFile',
            request_serializer=file__pb2.Bytes.SerializeToString,
            response_deserializer=file__pb2.Response.FromString,
        )


class FileServiceServicer(object):
    """python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./file.proto

    """

    def UploadFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'UploadFile': grpc.stream_unary_rpc_method_handler(
            servicer.UploadFile,
            request_deserializer=file__pb2.Bytes.FromString,
            response_serializer=file__pb2.Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'proto.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class FileService(object):
    """python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./file.proto

    """

    @staticmethod
    def UploadFile(request_iterator,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/proto.FileService/UploadFile',
                                              file__pb2.Bytes.SerializeToString,
                                              file__pb2.Response.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout,
                                              metadata)
