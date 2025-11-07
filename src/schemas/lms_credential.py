from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class LMSCredentialBase(BaseModel):
    user_id: int
    lms_url: str
    access_token: str
    refresh_token: str
    expires_at: datetime


class LMSCredentialCreate(LMSCredentialBase):
    pass


class LMSCredentialUpdate(BaseModel):
    lms_url: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_at: Optional[datetime] = None


class LMSCredentialSchema(LMSCredentialBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True