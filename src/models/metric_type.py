from sqlalchemy import Column, String
from src.db.base import Base


class MetricType(Base):
    __tablename__ = "metric_types"

    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
