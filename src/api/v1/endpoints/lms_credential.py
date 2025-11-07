from fastapi import APIRouter
from datetime import datetime, timedelta
from src.schemas.lms_credential import LMSCredentialCreate, LMSCredentialUpdate, LMSCredentialSchema

router = APIRouter(prefix="/lms/credentials", tags=["LMS Credentials"])


@router.post("/", response_model=LMSCredentialSchema)
async def register_lms_credentials(
    credentials: LMSCredentialCreate
):
    """
    Registrar credenciales del LMS.
    """
    # Datos de prueba
    mock_new_credentials = {
        "id": 100,
        "user_id": credentials.user_id,
        "lms_url": credentials.lms_url,
        "access_token": credentials.access_token,
        "refresh_token": credentials.refresh_token,
        "expires_at": credentials.expires_at,
        "created_at": datetime.now(),
        "updated_at": None
    }
    
    return mock_new_credentials


@router.get("/{user_id}", response_model=LMSCredentialSchema)
async def get_user_credentials(
    user_id: int
):
    """
    Ver credenciales del usuario.
    """
    # Datos de prueba
    mock_credentials = {
        "id": 1,
        "user_id": user_id,
        "lms_url": "https://moodle.example.com",
        "access_token": "mock_access_token_abc123",
        "refresh_token": "mock_refresh_token_xyz789",
        "expires_at": datetime.now() + timedelta(days=30),
        "created_at": datetime.now() - timedelta(days=10),
        "updated_at": None
    }
    
    return mock_credentials


@router.put("/{user_id}", response_model=LMSCredentialSchema)
async def update_credentials(
    user_id: int,
    credentials_update: LMSCredentialUpdate
):
    """
    Actualizar credenciales.
    """
    # Datos de prueba
    mock_updated_credentials = {
        "id": 1,
        "user_id": user_id,
        "lms_url": credentials_update.lms_url or "https://moodle.example.com",
        "access_token": credentials_update.access_token or "mock_access_token_updated",
        "refresh_token": credentials_update.refresh_token or "mock_refresh_token_updated",
        "expires_at": credentials_update.expires_at or (datetime.now() + timedelta(days=30)),
        "created_at": datetime.now() - timedelta(days=10),
        "updated_at": datetime.now()
    }
    
    return mock_updated_credentials


@router.post("/sync", summary="Sincronizar datos entre LMS y plataforma")
async def sync_lms_data():
    """
    Sincronizar datos entre LMS y plataforma.
    """
    # Datos de prueba
    sync_result = {
        "status": "success",
        "message": "Sincronización completada exitosamente",
        "records_synced": {
            "users": 25,
            "courses": 5,
            "grades": 120
        },
        "sync_time": datetime.now(),
        "next_sync_scheduled": datetime.now() + timedelta(hours=24)
    }
    
    return sync_result