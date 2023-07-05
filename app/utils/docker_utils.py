import docker
from docker.errors import NotFound


def build_image(dockerfile_path, tag):
    client = docker.from_env()

    # create docker image
    image, build_logs = client.images.build(path=dockerfile_path, tag=tag)

    # build log
    for log in build_logs:
        print(log)


def run_container(image_name, url):
    client = docker.from_env()

    [ip, port] = str.split(url, ':')

    # get container
    container = client.containers.run(image_name, ports={f'5005/tcp': port}, detach=True)

    container.start()

    return container


def start_container(container_name_or_id):
    try:
        client = docker.from_env()

        container = client.containers.get(container_name_or_id)

        container.start()

        return True
    except Exception:
        return False


def stop_container(container_name_or_id, should_remove=False):
    try:
        client = docker.from_env()

        container = client.containers.get(container_name_or_id)

        container.stop()

        if should_remove:
            container.remove()

        return True
    except Exception:
        return False


def get_container_status(container_name_or_id):
    client = docker.DockerClient()

    try:
        container = client.containers.get(container_name_or_id)

        # 'created', 'restarting', 'running', 'removing', 'paused', 'exited','dead'
        return container.status
    except NotFound:
        return 'not exist'


if __name__ == '__main__':
    # create_image_and_run_container('/Users/chenxingyang/PycharmProjects/flask_demo', 'flask-demo',
    #                                'flask-demo')
    # run_container('flask-demo')
    print(get_container_status('b369bd73ca88235dd1d6492d014be3797e8cfb5b494128c2df3dd149058ad86d'))
