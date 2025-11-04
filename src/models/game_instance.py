from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base


class GameInstance(Base):
    __tablename__ = "game_instances"

    start_instance = Column(DateTime, nullable=False)
    status = Column(String(255), nullable=True)

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)

    # Relationships
    student = relationship("Student", back_populates="game_instances")
    game = relationship("Game", back_populates="instances")
    sync_sessions = relationship("SyncSession", back_populates="game_instance")
