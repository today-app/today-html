from flask import Flask, render_template

from webassets import Bundle

from app.extensions import assets
from app.config import config

def create_app(config_name="default"):
    app = Flask(__name__)
    app_config = config[config_name]
    app.config.from_object(app_config)

    init_assets(app)
    init_blueprint(app)

    return app

def init_assets(app):
    assets.init_app(app)
    css_all = Bundle('src/css/*.css', filters='postcss', output='dist/css/main.css')

    assets.register('css_all', css_all)


def init_blueprint(app):
    @app.route('/')
    def index():
        return render_template('index.html')
