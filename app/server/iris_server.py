from app import proto
from app import view


class PredictionTask(proto.iris_pb2_grpc.PredictionTaskServicer):
    def LaunchTask(self, request, context):
        result = view.iris_dt.launch_task(request.sepal_length, request.sepal_width, request.petal_length,
                                          request.petal_width)

        return proto.iris_pb2.TaskResponse(result=result)
