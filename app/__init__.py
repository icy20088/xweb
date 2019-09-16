from flask import Flask
from config import config
from .models import db
from .routes import main_bp

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    app.register_blueprint(main_bp)

    # db.create_all(app=app)

    return app
