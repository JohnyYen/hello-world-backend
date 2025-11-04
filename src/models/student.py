from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base


class Student(Base):
    __tablename__ = "students"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="student")
    game_instances = relationship("GameInstance", back_populates="student")
    feedbacks = relationship("Feedback", back_populates="student")
