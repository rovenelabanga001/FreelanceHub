from datetime import datetime
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, validates
from . import db


class ChatRoomMember(db.Model):
    __tablename__ = "chat_room_members"

    id = db.Column(db.Integer, primary_key=True)
    chat_room_id = db.Column(db.Integer, ForeignKey("chat_rooms.id"), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(30), nullable=True, doc="admin | member | moderator")

    #relationships
    chat_room = relationship("ChatRoom", back_populates="members")
    user = relationship("User", backref="chat_room_memberships")

    @validates("user_id")
    def validate_user(self, key, value):
        from .user import User
        user = db.session.get(User, value)
        if not user:
            raise ValueError(f"User with id {value} does not exist")
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
            "user_id": self.user_id,
            "role": self.role,
            "joined_at": self.joined_at.isoformat() if self.joined_at else None
        }

    def __repr__(self):
        return f"<ChatRoomMember user={self.user_id} room={self.chat_room_id}>"