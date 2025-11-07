from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GameInstanceCreate(BaseModel):
    """Esquema para crear una nueva instancia de juego"""
    game_id: int
    student_id: int
    status: Optional[str] = "active"  # active, completed, abandoned
    started_at: Optional[datetime] = None


class GameInstanceUpdate(BaseModel):
    """Esquema para actualizar una instancia de juego"""
    status: Optional[str] = None
    ended_at: Optional[datetime] = None


class GameInstance(BaseModel):
    """Esquema para la respuesta de una instancia de juego"""
    id: int
    game_id: int
    student_id: int
    status: str
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True