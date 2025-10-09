import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False