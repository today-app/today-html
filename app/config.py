
import os

APP_DIR = os.path.dirname(__file__)
BASE_POSTCSS_BIN = os.path.join(
    os.path.dirname(APP_DIR), "node_modules/postcss-cli/bin/postcss"
)

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", 'secret-key')
    ASSETS_DEBUG = True
    POSTCSS_BIN = os.environ.get("POSTCSS_BIN", BASE_POSTCSS_BIN)


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    

class TestingConfig(Config):
    DEBUG = False
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
