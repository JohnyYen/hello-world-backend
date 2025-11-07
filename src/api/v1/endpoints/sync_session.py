from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.sync_session import SyncSessionCreate, SyncSessionUpdate, SyncSessionSchema
import datetime

router = APIRouter(prefix="/sync-sessions", tags=["Sync Sessions"])


@router.post("/", response_model=SyncSessionSchema)
async def start_sync_session(
    sync_session: SyncSessionCreate
):
    """
    Inicia una sesión de sincronización.
    """
    # Datos de prueba
    mock_new_session = {
        "id": 101,
        "instance_id": sync_session.instance_id,
        "is_active": True,
        "started_at": datetime.datetime.now(),
        "ended_at": None
    }
    
    return mock_new_session


@router.put("/{session_id}/end", response_model=SyncSessionSchema)
async def end_sync_session(
    session_id: int
):
    """
    Finaliza la sesión.
    """
    # Datos de prueba
    mock_ended_session = {
        "id": session_id,
        "instance_id": 1,  # ID simulado
        "is_active": False,
        "started_at": datetime.datetime.now() - datetime.timedelta(hours=1),
        "ended_at": datetime.datetime.now()
    }
    
    return mock_ended_session


@router.get("/{instance_id}", response_model=List[SyncSessionSchema])
async def get_sessions_by_instance(
    instance_id: int
):
    """
    Obtiene sesiones de una instancia.
    """
    # Datos de prueba
    mock_sessions = [
        {
            "id": 1,
            "instance_id": instance_id,
            "is_active": True,
            "started_at": datetime.datetime.now() - datetime.timedelta(minutes=30),
            "ended_at": None
        },
        {
            "id": 2,
            "instance_id": instance_id,
            "is_active": False,
            "started_at": datetime.datetime.now() - datetime.timedelta(days=1),
            "ended_at": datetime.datetime.now() - datetime.timedelta(days=1, hours=2)
        }
    ]
    
    return mock_sessions