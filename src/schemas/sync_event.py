from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SyncEventBase(BaseModel):
    session_id: int
    event_type: str
    event_data: dict


class SyncEventCreate(SyncEventBase):
    pass


class SyncEventUpdate(BaseModel):
    event_data: Optional[dict] = None


class SyncEventSchema(SyncEventBase):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True