from datetime import datetime
from sqlalchemy import CheckConstraint, ForeignKey, Numeric
from sqlalchemy.orm import relationship, validates
from . import db

class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    budget = db.Column(db.Numeric, (10,2), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(30), nullable=False, default="open")
    client_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    freelancer_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    selected_bid_id = db.Column(db.Integer, ForeignKey("bids.id"), nullable=True)
    created_at = db.Column(db.Datetime, default=datetime.utcnow)

    #relationships
    client = relationship("User", foreign_keys=[client_id], backref="client_projects")
    freelancer = relationship("User", foreign_keys=[freelancer_id], backref="freelancer_projects")
    milestones = relationship("Milestone", back_populates="project", cascade="all, delete-orphan")
    bids = relationship("Bid", back_populates="project", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("status IN ('open', 'in_progress', 'completed', 'cancelled')", name="valid_status_check"),
    )

    @validates("client_id")
    def validate_client_id(self, key, value):
        from .user import User
        user = db.session.get(User, value)
        if not user:
            raise ValueError("Client ID does not exist")
        if user.role != "client":
            raise ValueError("client_id must belong to a user with role 'client'")
        return value
    
    @validates("freelancer_id")
    def validate_freelancer_id(self, key, value):
        from .user import User
        if value is None:
            return value
        user = db.session.get(User, value)
        if not user:
            raise ValueError("Freelancer ID does not exist")
        if user.role != "freelancer":
            raise ValueError("freelancer_id must belong to a user with role 'freelancer'")
        return value    
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "budget": self.budget,
            "status": self.status,
            "client_id": self.client_id,
            "freelancer_id": self.freelancer_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


    def __repr__(self):
        return f"<Project {self.title} | {self.status}>"