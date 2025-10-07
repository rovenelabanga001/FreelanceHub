from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import JSON, CheckConstraint
from sqlalchemy_serializer import SerializerMixin
from . import db

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    _password_hash = db.Column("password_hash", db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    bio = db.Column(db.Text)
    skills = db.Column(JSON)
    profile_pic = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float)
    created_at = db.Column(db.Datetime, default = datetime.utcnow)

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'client', 'freelancer')", name="valid_role_check")
    )

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")
    
    @password.setter
    def password(self, plain_password):
        self._password_hash = generate_password_hash(plain_password)

    def verify_password(self, plain_password):
        return check_password_hash(self._password_hash, plain_password)
    
    def __repr__(self):
        return f"<User {self.username}>"