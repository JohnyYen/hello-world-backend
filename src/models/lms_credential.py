from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from src.db.base import Base


class LMSCredential(Base):
    __tablename__ = "lms_credentials"

    lms_email = Column(String(255), unique=True, nullable=False)
    lms_password = Column(String(255), nullable=False)
    lms_provider = Column(String(255), nullable=False)
    acces_token = Column(String(255), nullable=True)
    expire_at = Column(DateTime, nullable=True)

    # Relationship with User
    user = relationship("User", back_populates="lms_credential", uselist=False)
