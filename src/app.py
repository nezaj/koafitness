from flask import Flask, render_template

from .loggers import get_app_stderr_handler
from . import assets
from . import public

def create_app(config_obj):
    " Factory for creating app "
    app = Flask(__name__)
    app.config.from_object(config_obj)
    initialize_app(app)
    register_loggers(app)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app

def register_loggers(app):
    " Sets up app and sqlalchemy loggers "
    app.logger.handlers = []
    app.logger.setLevel(app.config["APP_LOG_LEVEL"])
    app.logger.addHandler(get_app_stderr_handler())

def initialize_app(app):
    " Do any one-time initialization of the app prior to serving "
    app.static_folder = app.config['STATIC_DIR']

def register_extensions(app):
    " Configures flask extensions to be used with app"
    assets.register_assets(app)

def register_blueprints(app):
    " Registers blueprint routes on app "
    app.register_blueprint(public.views.blueprint)

def register_errorhandlers(app):
    " Register custom error pages "
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{}.tmpl'.format(error_code)), error_code

    for errcode in [401, 403, 404, 500]:
        app.errorhandler(errcode)(render_error)
