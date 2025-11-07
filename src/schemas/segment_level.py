from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class SegmentLevelCreate(BaseModel):
    """Esquema para crear un nuevo segmento de nivel"""
    level_id: int
    name: str
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None  # Configuración JSON del segmento
    order: Optional[int] = 1
    is_active: Optional[bool] = True


class SegmentLevelUpdate(BaseModel):
    """Esquema para actualizar un segmento de nivel"""
    name: Optional[str] = None
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None  # Configuración JSON del segmento
    order: Optional[int] = None
    is_active: Optional[bool] = None


class SegmentLevel(BaseModel):
    """Esquema para la respuesta de un segmento de nivel"""
    id: int
    level_id: int
    name: str
    description: Optional[str] = None
    config: Optional[Dict[str, Any]] = None
    order: int
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True