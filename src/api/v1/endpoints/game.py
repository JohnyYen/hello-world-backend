from fastapi import APIRouter, Depends, Query
from src.core.deps import get_current_user
from src.models.user import User
from src.schemas.game import GameCreateSchema, GameUpdateSchema, GameSchema
from src.schemas.level import LevelCreateSchema, LevelUpdateSchema, LevelSchema


router = APIRouter(prefix="/games", tags=["Games"])

@router.get("/", response_model=list[GameSchema])
async def get_games(
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número de registros a devolver")
):
    """
    Lista todos los juegos.
    """
    # Datos de prueba
    mock_games = [
        {
            "id": 1,
            "name": "Juego de Matemáticas Básicas",
            "description": "Un juego para aprender matemáticas básicas",
            "version": "1.0.0",
            "is_active": True,
            "created_at": "2023-01-15T10:30:00",
            "updated_at": "2023-01-15T10:30:00"
        },
        {
            "id": 2,
            "name": "Aventura de Programación",
            "description": "Un juego para aprender conceptos de programación",
            "version": "2.1.0",
            "is_active": True,
            "created_at": "2023-02-20T14:45:00",
            "updated_at": "2023-02-21T09:15:00"
        }
    ]
    
    # Aplicar paginación
    start = skip
    end = skip + limit
    paginated_games = mock_games[start:end]
    
    return paginated_games

@router.post("/", response_model=GameSchema)
async def create_game(
    game: GameCreateSchema,
    current_user: User = Depends(get_current_user)
):
    """
    Crea un nuevo juego.
    """
    # Datos de prueba
    mock_new_game = {
        "id": 999,  # ID simulado para el nuevo juego
        "name": game.name,
        "description": game.description,
        "version": game.version or "1.0.0",
        "is_active": game.is_active if game.is_active is not None else True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return mock_new_game

@router.get("/{game_id}", response_model=GameSchema)
async def get_game(
    game_id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Detalles de un juego específico.
    """
    # Datos de prueba
    mock_game = {
        "id": game_id,
        "name": f"Juego de ejemplo {game_id}",
        "description": f"Descripción del juego {game_id}",
        "version": "1.0.0",
        "is_active": True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return mock_game

@router.put("/{game_id}", response_model=GameSchema)
async def update_game(
    game_id: int,
    game: GameUpdateSchema,
    current_user: User = Depends(get_current_user)
):
    """
    Actualiza un juego.
    """
    # Datos de prueba
    mock_updated_game = {
        "id": game_id,
        "name": game.name or f"Juego de ejemplo {game_id}",
        "description": game.description or f"Descripción del juego {game_id}",
        "version": game.version or "1.0.0",
        "is_active": game.is_active if game.is_active is not None else True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T15:45:00"  # Fecha actualizada
    }
    
    return mock_updated_game

@router.delete("/{game_id}")
async def delete_game(
    game_id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Elimina un juego.
    """
    # Simulación de eliminación
    return {"message": f"Juego con ID {game_id} eliminado exitosamente"}