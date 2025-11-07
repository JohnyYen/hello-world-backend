from fastapi import APIRouter, Depends, Query
from src.core.deps import get_current_user
from src.models.user import User
from src.schemas.game_instance import GameInstanceCreate, GameInstanceUpdate, GameInstance as GameInstanceSchema

router = APIRouter(prefix="/game-instances", tags=["Game Instances"])

@router.post("/{game_id}/instances", response_model=GameInstanceSchema)
async def create_game_instance(
    game_id: int,
    instance_data: GameInstanceCreate,
    current_user: User = Depends(get_current_user)
):
    """
    Crea una instancia del juego para un estudiante.
    """
    # Datos de prueba
    mock_new_instance = {
        "id": 999,  # ID simulado para la nueva instancia
        "game_id": game_id,
        "student_id": instance_data.student_id,
        "status": "active",
        "started_at": "2023-01-15T10:30:00",
        "ended_at": None,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return mock_new_instance

@router.get("/{game_id}/instances", response_model=list[GameInstanceSchema])
async def list_game_instances(
    game_id: int,
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número de registros a devolver"),
    status: str = Query("active", description="Filtrar por estado (active, completed, abandoned)")
):
    """
    Lista instancias activas.
    """
    # Datos de prueba
    mock_instances = [
        {
            "id": 1,
            "game_id": game_id,
            "student_id": 1,
            "status": status,
            "started_at": "2023-01-15T10:30:00",
            "ended_at": None,
            "created_at": "2023-01-15T10:30:00",
            "updated_at": "2023-01-15T10:30:00"
        },
        {
            "id": 2,
            "game_id": game_id,
            "student_id": 2,
            "status": status,
            "started_at": "2023-01-16T11:45:00",
            "ended_at": None,
            "created_at": "2023-01-16T11:45:00",
            "updated_at": "2023-01-16T11:45:00"
        }
    ]
    
    # Aplicar paginación
    start = skip
    end = skip + limit
    paginated_instances = mock_instances[start:end]
    
    return paginated_instances

@router.get("/{instance_id}", response_model=GameInstanceSchema)
async def get_instance(
    instance_id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Obtiene información de una instancia.
    """
    # Datos de prueba
    mock_instance = {
        "id": instance_id,
        "game_id": 1,
        "student_id": 1,
        "status": "active",
        "started_at": "2023-01-15T10:30:00",
        "ended_at": None,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return mock_instance

@router.put("/{instance_id}/end", response_model=GameInstanceSchema)
async def end_instance(
    instance_id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Marca la instancia como finalizada.
    """
    # Datos de prueba
    mock_updated_instance = {
        "id": instance_id,
        "game_id": 1,
        "student_id": 1,
        "status": "completed",
        "started_at": "2023-01-15T10:30:00",
        "ended_at": "2023-01-15T12:45:00",  # Fecha de finalización actualizada
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T12:45:00"  # Fecha actualizada
    }
    
    return mock_updated_instance
