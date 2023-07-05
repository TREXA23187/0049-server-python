from app import proto
from ..utils import docker_utils


class InstanceService(proto.instance_pb2_grpc.InstanceServiceServicer):

    def CreateInstance(self, request, context):
        container = docker_utils.run_container('flask-demo', request.url)

        return proto.instance_pb2.CreateInstanceResponse(instance_id=container.id, instance_name=container.name)

    def GetInstanceInfo(self, request, context):
        status = docker_utils.get_container_status(request.instance_id)

        return proto.instance_pb2.InstanceInfoResponse(status=status)

    def OperateInstance(self, request, context):
        success = None
        if request.operation == 'start':
            success = docker_utils.start_container(request.instance_id)
        elif request.operation == 'remove':
            success = docker_utils.stop_container(request.instance_id, True)
        else:
            success = docker_utils.stop_container(request.instance_id)

        return proto.instance_pb2.OperateInstanceResponse(success=success)
