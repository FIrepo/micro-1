# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from runtime import runtime_pb2 as runtime_dot_runtime__pb2


class RuntimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/runtime.Runtime/Create',
                request_serializer=runtime_dot_runtime__pb2.CreateRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.CreateResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/runtime.Runtime/Read',
                request_serializer=runtime_dot_runtime__pb2.ReadRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.ReadResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/runtime.Runtime/Delete',
                request_serializer=runtime_dot_runtime__pb2.DeleteRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.DeleteResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/runtime.Runtime/Update',
                request_serializer=runtime_dot_runtime__pb2.UpdateRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.UpdateResponse.FromString,
                )
        self.Logs = channel.unary_stream(
                '/runtime.Runtime/Logs',
                request_serializer=runtime_dot_runtime__pb2.LogsRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.LogRecord.FromString,
                )
        self.CreateNamespace = channel.unary_unary(
                '/runtime.Runtime/CreateNamespace',
                request_serializer=runtime_dot_runtime__pb2.CreateNamespaceRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.CreateNamespaceResponse.FromString,
                )
        self.DeleteNamespace = channel.unary_unary(
                '/runtime.Runtime/DeleteNamespace',
                request_serializer=runtime_dot_runtime__pb2.DeleteNamespaceRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.DeleteNamespaceResponse.FromString,
                )


class RuntimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Logs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNamespace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNamespace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RuntimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=runtime_dot_runtime__pb2.CreateRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.CreateResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=runtime_dot_runtime__pb2.ReadRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.ReadResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=runtime_dot_runtime__pb2.DeleteRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.DeleteResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=runtime_dot_runtime__pb2.UpdateRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.UpdateResponse.SerializeToString,
            ),
            'Logs': grpc.unary_stream_rpc_method_handler(
                    servicer.Logs,
                    request_deserializer=runtime_dot_runtime__pb2.LogsRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.LogRecord.SerializeToString,
            ),
            'CreateNamespace': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNamespace,
                    request_deserializer=runtime_dot_runtime__pb2.CreateNamespaceRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.CreateNamespaceResponse.SerializeToString,
            ),
            'DeleteNamespace': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNamespace,
                    request_deserializer=runtime_dot_runtime__pb2.DeleteNamespaceRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.DeleteNamespaceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'runtime.Runtime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Runtime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/runtime.Runtime/Create',
            runtime_dot_runtime__pb2.CreateRequest.SerializeToString,
            runtime_dot_runtime__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/runtime.Runtime/Read',
            runtime_dot_runtime__pb2.ReadRequest.SerializeToString,
            runtime_dot_runtime__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/runtime.Runtime/Delete',
            runtime_dot_runtime__pb2.DeleteRequest.SerializeToString,
            runtime_dot_runtime__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/runtime.Runtime/Update',
            runtime_dot_runtime__pb2.UpdateRequest.SerializeToString,
            runtime_dot_runtime__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Logs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/runtime.Runtime/Logs',
            runtime_dot_runtime__pb2.LogsRequest.SerializeToString,
            runtime_dot_runtime__pb2.LogRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNamespace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/runtime.Runtime/CreateNamespace',
            runtime_dot_runtime__pb2.CreateNamespaceRequest.SerializeToString,
            runtime_dot_runtime__pb2.CreateNamespaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNamespace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/runtime.Runtime/DeleteNamespace',
            runtime_dot_runtime__pb2.DeleteNamespaceRequest.SerializeToString,
            runtime_dot_runtime__pb2.DeleteNamespaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SourceStub(object):
    """Source service is used by the CLI to upload source to the service. The service will return
    a unique ID representing the location of that source. This ID can then be used as a source
    for the service when doing Runtime.Create. The server will handle cleanup of uploaded source.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upload = channel.stream_unary(
                '/runtime.Source/Upload',
                request_serializer=runtime_dot_runtime__pb2.UploadRequest.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.UploadResponse.FromString,
                )


class SourceServicer(object):
    """Source service is used by the CLI to upload source to the service. The service will return
    a unique ID representing the location of that source. This ID can then be used as a source
    for the service when doing Runtime.Create. The server will handle cleanup of uploaded source.
    """

    def Upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upload': grpc.stream_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=runtime_dot_runtime__pb2.UploadRequest.FromString,
                    response_serializer=runtime_dot_runtime__pb2.UploadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'runtime.Source', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Source(object):
    """Source service is used by the CLI to upload source to the service. The service will return
    a unique ID representing the location of that source. This ID can then be used as a source
    for the service when doing Runtime.Create. The server will handle cleanup of uploaded source.
    """

    @staticmethod
    def Upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/runtime.Source/Upload',
            runtime_dot_runtime__pb2.UploadRequest.SerializeToString,
            runtime_dot_runtime__pb2.UploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BuildStub(object):
    """Build service is used by containers to download prebuilt binaries. The client will pass the 
    service (name and version are required attributed) and the server will then stream the latest
    binary to the client.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_stream(
                '/runtime.Build/Read',
                request_serializer=runtime_dot_runtime__pb2.Service.SerializeToString,
                response_deserializer=runtime_dot_runtime__pb2.BuildReadResponse.FromString,
                )


class BuildServicer(object):
    """Build service is used by containers to download prebuilt binaries. The client will pass the 
    service (name and version are required attributed) and the server will then stream the latest
    binary to the client.
    """

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BuildServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_stream_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=runtime_dot_runtime__pb2.Service.FromString,
                    response_serializer=runtime_dot_runtime__pb2.BuildReadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'runtime.Build', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Build(object):
    """Build service is used by containers to download prebuilt binaries. The client will pass the 
    service (name and version are required attributed) and the server will then stream the latest
    binary to the client.
    """

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/runtime.Build/Read',
            runtime_dot_runtime__pb2.Service.SerializeToString,
            runtime_dot_runtime__pb2.BuildReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
