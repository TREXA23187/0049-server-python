from app import proto


class FileService(proto.file_pb2_grpc.FileServiceServicer):
    def UploadFile(self, request, context):
        with open('data/uploaded.file.txt', 'wb') as f:
            for chunk in request:
                f.write(chunk.value)
        return proto.file_pb2.Response(flag=1)
