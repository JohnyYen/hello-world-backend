from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base


class SyncSession(Base):
    __tablename__ = "sync_sessions"

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)
    status = Column(String(255), nullable=True)

    instance_id = Column(Integer, ForeignKey("game_instances.id"), nullable=False)

    # Relationships
    game_instance = relationship("GameInstance", back_populates="sync_sessions")
    events = relationship("SyncEvent", back_populates="sync_session")
