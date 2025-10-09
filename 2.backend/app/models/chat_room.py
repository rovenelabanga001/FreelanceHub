from datetime import datetime
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import validates, relationship
from app import db

class ChatRoom(db.Model):
    __tablename__ = "chat_rooms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), doc="Optional, used for group rooms")
    type = db.Column(
        db.String(20),
        nullable = False,
        doc = "'direct' | 'group' | 'project'"
    )
    project_id = db.Column(db.Integer, ForeignKey("projects.id"), nullable=True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    #relationships
    project = relationship("Project", backref="chat_rooms")
    members = relationship("ChatRoomMember", back_populates="chat_room", cascade="all, delete-orphan")
    messages = relationship("Message", back_populates="chat_room", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(
            "type IN ('direct', 'group', 'project')"
        ),
    )

    @validates('project_id')
    def validate_project_id(self, key, value):
        if value is None:
            return value #project-less rooms (direct or group) are allowed
        
        from .project import Project
        project = db.session.get(Project, value)
        if not project:
            raise ValueError (f"Project with id {value} does not exist")
        
        return value
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "project_id": self.project_id,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<ChatRoom {self.id} ({self.type})>"