from app import proto
from ..utils import docker_utils


class InstanceService(proto.instance_pb2_grpc.InstanceServiceServicer):

    def CreateInstance(self, request, context):
        container = docker_utils.run_container('flask-demo', request.url)

        return proto.instance_pb2.CreateInstanceResponse(instance_id=container.id, instance_name=container.name)

    def GetInstanceInfo(self, request, context):
        status = docker_utils.get_container_status(request.instance_id)

        return proto.instance_pb2.InstanceInfoResponse(status=status)
