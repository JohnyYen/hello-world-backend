from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    created_at = Column(DateTime, nullable=False)
    comments = Column(String(255), nullable=True)

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    # Relationships
    student = relationship("Student", back_populates="feedbacks")
