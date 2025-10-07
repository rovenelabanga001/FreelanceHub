from datetime import date
from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy_serializer import SerializerMixin
from . import db

class Milestone(db.Model, SerializerMixin):
    __tablename__ = "milestones"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey("projects.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    amount = db.Column(db.Numeric(10,2), nullable=False)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(30), nullable=False, default="pending")

    project = relationship("Project", back_populates="milestones")

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'in_review', 'paid')",
            name="valid_milestone_status_check"
        )
    )

    @validates(project_id)
    def validate_project_id(self, key, value):
        from .project import Project
        project = db.Session.get(Project, value)
        if not project:
            raise ValueError("Project ID does not exist")
        return value
    
    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
            "amount": float(self.amount),
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "status": self.status,
        }
    
    def __repr__(self):
        return f"<Milestone {self.title} for Project {self.project}>"