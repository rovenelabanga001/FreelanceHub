from datetime import date
from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, validates
from app import db

class Milestone(db.Model):
    __tablename__ = "milestones"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey("projects.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Numeric(10,2), nullable=False)
    start_date = db.Column(db.Date)
    completed_date = db.Column(db.Date)
    approved_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(30), nullable=False, default="pending")

    #relationships
    project = relationship("Project", back_populates="milestones")
    payment = relationship("Payment", back_populates="milestone", uselist=False, cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'in_progress', 'submitted', 'approved', 'rejected', 'completed')",
            name="valid_milestone_status_check"
        ),
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