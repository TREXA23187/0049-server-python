from app.server import create_server, serve

DEVELOPMENT_MODE = "development"
PRODUCTION_MODE = "production"

if __name__ == '__main__':
    server = create_server()
    serve(server)
