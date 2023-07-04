import docker


def build_image(dockerfile_path, tag):
    client = docker.from_env()

    # create docker image
    image, build_logs = client.images.build(path=dockerfile_path, tag=tag)

    # build log
    for log in build_logs:
        print(log)


def run_container(image_name):
    client = docker.from_env()

    # get container
    container = client.containers.run(image_name, ports={'5005/tcp': 5005}, detach=True)

    container.start()

    return container


def stop_container(container_name):
    client = docker.from_env()

    container = client.containers.get(container_name)

    container.stop()
    container.remove()


def test():
    print('test')


if __name__ == '__main__':
    # create_image_and_run_container('/Users/chenxingyang/PycharmProjects/flask_demo', 'flask-demo',
    #                                'flask-demo')
    # run_container('flask-demo')
    stop_container()
