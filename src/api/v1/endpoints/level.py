from fastapi import APIRouter, Depends, Query
from src.core.deps import get_current_user
from src.models.user import User
from src.schemas.level import LevelCreateSchema, LevelUpdateSchema, LevelSchema

router = APIRouter(prefix="/levels", tags=["Levels"])

@router.get("/{level_id}", response_model=LevelSchema)
async def get_level(
    level_id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Detalles de un nivel.
    """
    # Datos de prueba
    mock_level = {
        "id": level_id,
        "game_id": 1,
        "name": f"Nivel {level_id}",
        "description": f"Descripción del nivel {level_id}",
        "order": level_id,
        "is_active": True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return mock_level

@router.put("/{level_id}", response_model=LevelSchema)
async def update_level(
    level_id: int,
    level: LevelUpdateSchema,
    current_user: User = Depends(get_current_user)
):
    """
    Edita un nivel.
    """
    # Datos de prueba
    mock_updated_level = {
        "id": level_id,
        "game_id": 1,
        "name": level.name or f"Nivel {level_id}",
        "description": level.description or f"Descripción del nivel {level_id}",
        "order": level.order or level_id,
        "is_active": level.is_active if level.is_active is not None else True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T15:45:00"  # Fecha actualizada
    }
    
    return mock_updated_level

@router.delete("/{level_id}")
async def delete_level(
    level_id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Elimina un nivel.
    """
    # Simulación de eliminación
    return {"message": f"Nivel con ID {level_id} eliminado exitosamente"}


# Endpoints para niveles asociados a un juego específico
game_level_router = APIRouter(prefix="/games/{game_id}/levels", tags=["Game Levels"])

@game_level_router.get("/", response_model=list[LevelSchema])
async def get_game_levels(
    game_id: int,
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número de registros a devolver")
):
    """
    Lista los niveles de un juego.
    """
    # Datos de prueba
    mock_levels = [
        {
            "id": 1,
            "game_id": game_id,
            "name": "Nivel 1: Introducción",
            "description": "Nivel introductorio para familiarizarse con el juego",
            "order": 1,
            "is_active": True,
            "created_at": "2023-01-15T10:30:00",
            "updated_at": "2023-01-15T10:30:00"
        },
        {
            "id": 2,
            "game_id": game_id,
            "name": "Nivel 2: Básico",
            "description": "Nivel básico con conceptos fundamentales",
            "order": 2,
            "is_active": True,
            "created_at": "2023-01-16T11:45:00",
            "updated_at": "2023-01-16T11:45:00"
        },
        {
            "id": 3,
            "game_id": game_id,
            "name": "Nivel 3: Intermedio",
            "description": "Nivel intermedio con desafíos más complejos",
            "order": 3,
            "is_active": True,
            "created_at": "2023-01-17T09:30:00",
            "updated_at": "2023-01-17T09:30:00"
        }
    ]
    
    # Aplicar paginación
    start = skip
    end = skip + limit
    paginated_levels = mock_levels[start:end]
    
    return paginated_levels

@game_level_router.post("/", response_model=LevelSchema)
async def create_game_level(
    game_id: int,
    level: LevelCreateSchema,
    current_user: User = Depends(get_current_user)
):
    """
    Crea un nuevo nivel en un juego.
    """
    # Datos de prueba
    mock_new_level = {
        "id": 999,  # ID simulado para el nuevo nivel
        "game_id": game_id,
        "name": level.name,
        "description": level.description,
        "order": level.order or 1,
        "is_active": level.is_active if level.is_active is not None else True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return mock_new_level


# Agregar el router de niveles de juego al router principal
router.include_router(game_level_router)