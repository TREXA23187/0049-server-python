class Config(object):
    SECRET_KEY = "xxx"

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
