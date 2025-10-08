from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy import JSON, CheckConstraint
from . import db

class User(db.Model):
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

    #relationships
    bids = relationship("Bids", back_populates="freelancer", cascade="all, delete-orphan")
    
    payments_made = relationship(
        "Payment",
        foreign_keys="Payment.payer_id",
        back_populates="payer",
        cascade="all, delete-orphan"
    )
    payments_received = relationship(
        "Payment",
        foreign_keys="Payment.receiver_id",
        back_populates="receiver",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'client', 'freelancer')", name="valid_role_check"),
    )

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")
    
    @password.setter
    def password(self, plain_password):
        self._password_hash = generate_password_hash(plain_password)

    def verify_password(self, plain_password):
        return check_password_hash(self._password_hash, plain_password)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "bio": self.bio,
            "skills": self.skills,
            "rating": self.rating,
            "profile_pic": self.profile_pic,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
        
    
    def __repr__(self):
        return f"<User {self.username}>"