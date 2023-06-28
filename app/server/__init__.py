import grpc
from concurrent import futures
import atexit
from app import proto

from . import data_server
from . import iris_server
from . import file_server

_HOST = 'localhost'
_PORT = '8088'
_MAX_WORKERS = 4


def create_server():
    # Define the server and set the maximum number of connections
    # concurrent.futures is a concurrent library, similar to the concept of Thread pool
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=_MAX_WORKERS))  # create server

    # Add derived interface services to the server (implementing their own processing functions)
    proto.data_pb2_grpc.add_FormatDataServicer_to_server(data_server.FormatData(), server)
    proto.iris_pb2_grpc.add_PredictionTaskServicer_to_server(iris_server.PredictionTask(), server)
    proto.file_pb2_grpc.add_FileServiceServicer_to_server(file_server.FileService(), server)

    server.add_insecure_port(_HOST + ':' + _PORT)

    return server


def serve(server):
    server.start()  # start the server
    print(f"server in running on: http://{_HOST}:{_PORT}")

    atexit.register(lambda: server.stop(0))
    server.wait_for_termination()
