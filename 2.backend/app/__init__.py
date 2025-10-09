# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    
    from app.models import(
        bid,
        chat_room_member,
        chat_room,
        message,
        milestone,
        notification,
        payment,
        project,
        user
    )  

    
    from app.routes.main import main
    from app.routes.user import user_bp

    app.register_blueprint(main)
    app.register_blueprint(user_bp)

    return app
