from datetime import datetime
from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, validates
from . import db
from sqlalchemy_serializer import SerializerMixin

class Bid(db.Model, SerializerMixin):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey("projects.id"), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    message = db.Column(db.Text)
    status = db.Column(
        db.String(30),
        nullable=False,
        default="pending"
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #relationships
    project = relationship("Project", back_populates="bids")
    freelancer = relationship("User", back_populates="bids")

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'accepted', 'rejected')",
            name='valid_bid_status_check'
        ),
    )


    @validates("user_id")
    def validate_user_role(self, key, value):
        """Ensure only a freelancer can place a bid"""
        from models.user import User
        user = db.session.get(User, value)
        if not user:
            raise ValueError("User does not exist")
        if user.role != "freelancer":
            raise ValueError("Only users with role 'freelancer' can place a bid")
        return value
    
    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "user_id": self.user_id,
            "amount": float(self.amount),
            "message": self.message,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f"<Bid {self.id} - Project {self.project_id} by User {self.user_id}>"