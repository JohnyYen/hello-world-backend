from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class FeedbackBase(BaseModel):
    student_id: int
    message: str
    rating: Optional[int] = None  # Rating from 1 to 5


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(BaseModel):
    message: Optional[str] = None
    rating: Optional[int] = None


class FeedbackSchema(FeedbackBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True