from sqlalchemy import Column, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base


class Progress(Base):
    __tablename__ = "progresses"

    attempt_count = Column(Integer, default=0)
    error_count = Column(Integer, default=0)
    hints_used_count = Column(Integer, default=0)
    errors_details = Column(JSON, nullable=True)
    objectives_completed = Column(Integer, default=0)
    efficiency_rating = Column(Integer, default=0)

    segment_level_id = Column(Integer, ForeignKey("segment_levels.id"), nullable=False)

    # Relationships
    segment_level = relationship("SegmentLevel", back_populates="progresses")
