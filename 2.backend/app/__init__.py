from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    CORS(app)
    db.init_app(app)
    Migrate(app, db)

    from app.models import (
        user,
        project,
        bid,
        chat_room,
        chat_room_member,
        message,
        milestone,
        notification,
        payment,
    )

    from app.routes.main import main

    app.register_blueprint(main)

    return app