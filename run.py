from app.server import create_server, serve
from app.mq import consume_rabbitmq
import threading

DEVELOPMENT_MODE = "development"
PRODUCTION_MODE = "production"


def start_serve():
    server = create_server()
    serve(server)


if __name__ == '__main__':
    serve_thread = threading.Thread(target=start_serve)
    mq_thread = threading.Thread(target=consume_rabbitmq)

    serve_thread.start()
    mq_thread.start()

    serve_thread.join()
    mq_thread.join()
