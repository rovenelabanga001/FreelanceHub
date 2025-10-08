from datetime import datetime
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, validates
from . import db

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(
        db.String(30),
        nullable=False,
        doc=" 'project' | 'payment' | 'message' | 'system' "
    )
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", backref="notifications")

    __table_args__ = (
        CheckConstraint(
            "type IN ('project', 'payment', 'message', 'system')",
            name="valid_notification_type_check"
        ),
    )

    @validates("user_id")
    def validate_user_id(self, key, value):
        """Ensure the user exists before assigning user_id."""
        from .user import User
        user = db.session.get(User, value)
        if not user:
            raise ValueError(f"User with id {value} does not exist")
        return value


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content,
            "type": self.type,
            "is_read": self.is_read,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<Notification {self.id} | User {self.user_id} | {self.type}>"
