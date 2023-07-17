import os.path
import shutil
from app import proto
from ..utils import docker_utils
from ..mq import push_message
from git import Repo
import json
from google.protobuf.json_format import MessageToDict


class InstanceService(proto.instance_pb2_grpc.InstanceServiceServicer):

    def CreateInstance(self, request, context):
        container = docker_utils.run_container(request.image_name, request.url)

        return proto.instance_pb2.CreateInstanceResponse(instance_id=container.id, instance_name=container.name)

    def CreateImage(self, request, context):
        image_to_build_path = "image_to_build"
        Repo.clone_from("https://github.com/TREXA23187/flask_demo", image_to_build_path)

        with open(os.path.join(image_to_build_path, "data/data.csv"), 'wb') as data_file:
            data_file.write(request.data_file)

        with open(os.path.join(image_to_build_path, "model/enter.py"), 'wb') as model_file:
            model_file.write(request.model_file)

        with open(os.path.join(image_to_build_path, "config.json"), 'w') as config_file:
            json.dump(MessageToDict(request.image_config), config_file)

        image = docker_utils.build_image(image_to_build_path, f"{request.repository}:{request.tag}")

        push_message(request.repository.encode('utf-8'))
        shutil.rmtree("image_to_build")
        return proto.instance_pb2.CreateImageResponse(image_id=image.id, image_size=image.attrs['Size'])

    def DeleteImage(self, request, context):
        success = docker_utils.delete_image(request.repository, request.tag)
        return proto.instance_pb2.DeleteImageResponse(success=success)

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
