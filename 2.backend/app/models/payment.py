from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, validates
from . import db

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    milestone_id = db.Column(db.Integer, ForeignKey("milestones.id"), nullable = False, unique=True)
    payer_id = db.Column(db.Integer, ForeignKey("users.id"), nullable = False)
    receiver_id = db.Column(db.Integer, ForeignKey("users.id"), nullable = False)
    amount = db.Column(db.Numeric(10, 2), nullable = False)
    status = db.Column(db.String(30), nullable = False)
    created_at = db.Column(db.DateTime, default = db.func.now())

    #relationship
    milestone = relationship("Milestone", back_populates="payment", uselist=False)
    payer = relationship("User", foreign_keys = [payer_id], back_populates="payments_made")
    reciever = relationship("User",foreign_keys=[receiver_id], back_populates="payments_recieved")

    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'processing', 'completed', 'failed', 'refunded', 'partial')",
            name="valid_payment_status_check"
        ),
    )

    @validates("milestone_id")
    def validate_milestone_id(self, key, value):
        from .milestone import Milestone
        milestone = db.session.get(Milestone, value)
        if not milestone:
            raise ValueError("Milestone ID does not exist")
        return value
    
    def to_dict(self):
        return{
            "id": self.id,
            "milestone_id": self.milestone_id,
            "amount": self.amount,
            "status": self.status,
            "created_at":self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f"<Payment for Milestone {self.milestone_id} : {self.status}>"