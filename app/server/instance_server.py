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

    def CreateTrainingImage(self, request, context):
        try:
            if os.path.exists("image_to_build"):
                shutil.rmtree("image_to_build")

            image_to_build_path = "image_to_build"
            Repo.clone_from("https://github.com/TREXA23187/flask_demo", image_to_build_path)

            if request.data_file:
                with open(os.path.join(image_to_build_path, "data/data.csv"), 'wb') as data_file:
                    data_file.write(request.data_file)

            if request.model_file:
                with open(os.path.join(image_to_build_path, "model/enter.py"), 'wb') as model_file:
                    model_file.write(request.model_file)

            if request.image_config:
                with open(os.path.join(image_to_build_path, "config.json"), 'w') as config_file:
                    config = MessageToDict(request.image_config)
                    config["dataLabel"] = json.loads(config["dataLabel"])
                    config["hyperParameters"] = json.loads(config["hyperParameters"])

                    json.dump(config, config_file)

            image = docker_utils.build_image(image_to_build_path, f"{request.repository}:{request.tag}")

            return proto.instance_pb2.CreateImageResponse(image_id=image.id, image_size=image.attrs['Size'])
        except Exception as e:
            print("create image error: ", e)

        finally:
            if os.path.exists("image_to_build"):
                shutil.rmtree("image_to_build")

    def CreateDeploymentImage(self, request, context):
        try:
            if os.path.exists("image_to_build"):
                shutil.rmtree("image_to_build")

            image_to_build_path = "image_to_build"
            Repo.clone_from("https://github.com/TREXA23187/flask_demo", image_to_build_path)

            if request.trained_model_file:
                with open(os.path.join(image_to_build_path, "model/model.pickle"), 'wb') as model_file:
                    model_file.write(request.trained_model_file)

            if request.label_int_tag:
                with open(os.path.join(image_to_build_path, "model/label_int_tag.json"), 'w') as label_int_tag_file:
                    json.dump(request.trained_model_file, label_int_tag_file)

            if request.image_config:
                with open(os.path.join(image_to_build_path, "config.json"), 'w') as config_file:
                    config = MessageToDict(request.image_config)

                    json.dump(config, config_file)

            image = docker_utils.build_image(image_to_build_path, f"{request.repository}:{request.tag}")

            return proto.instance_pb2.CreateImageResponse(image_id=image.id, image_size=image.attrs['Size'])
        except Exception as e:
            print("create image error: ", e)

        finally:
            if os.path.exists("image_to_build"):
                shutil.rmtree("image_to_build")

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
