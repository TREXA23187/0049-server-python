from app import proto
from ..utils import docker_utils


class InstanceService(proto.instance_pb2_grpc.InstanceServiceServicer):

    def CreateInstance(self, request, context):
        container = docker_utils.run_container('flask-demo')

        return proto.instance_pb2.InstanceResponse(instance_id=container.id, instance_name=container.name)
