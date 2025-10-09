from datetime import datetime
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import validates, relationship
from app import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    chat_room_id = db.Column(db.Integer, ForeignKey("chat_rooms.id"), nullable=False)
    sender_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    message_type = db.Column(
        db.String(30),
        nullable=False,
        default="text",
        doc="'text' | 'image' | 'file' | 'system'"
    )
    status = db.Column(
        db.String(20),
        nullable=False,
        default="sent",
        doc="'sent' | 'delivered' | 'read'"
    )
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    chat_room = relationship("ChatRoom", back_populates="messages")
    sender = relationship("User", backref="sent_messages")

    __table_args__ = (
        CheckConstraint(
            "message_type IN ('text', 'image', 'file', 'system')",
            name="valid_message_type_check"
        ),
        CheckConstraint(
            "status IN ('sent', 'delivered', 'read')",
            name="valid_message_status_check"
        ),
    )

    @validates("sender_id")
    def validate_sender(self, key, value):
        from .user import User
        user = db.session.get(User, value)
        if not user:
            raise ValueError(f"Sender (User id={value}) does not exist")
        return value

    @validates("chat_room_id")
    def validate_chat_room(self, key, value):
        from .chat_room import ChatRoom
        room = db.session.get(ChatRoom, value)
        if not room:
            raise ValueError(f"ChatRoom with id {value} does not exist")
        return value

    def to_dict(self):
        return {
            "id": self.id,
            "chat_room_id": self.chat_room_id,
            "sender_id": self.sender_id,
            "content": self.content,
            "message_type": self.message_type,
            "status": self.status,
            "sent_at": self.sent_at.isoformat() if self.sent_at else None
        }

    def __repr__(self):
        return f"<Message {self.id} | Room {self.chat_room_id} | {self.message_type}>"