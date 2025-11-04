# app/services/game_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.game_repository import GameRepository
from src.schemas.game import GameCreate, GameUpdate
from src.models.game import Game
from src.core.exceptions import NotFoundException


class GameService:
    """
    Servicio para gestionar la lógica de negocio de juegos.

    Proporciona una capa de abstracción sobre el repositorio de juegos,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.game_repo = GameRepository(db)

    async def get_game_by_id(self, game_id: int) -> Optional[Game]:
        """
        Obtiene un juego por su ID.

        Args:
            game_id: ID del juego a buscar.

        Returns:
            El juego si se encuentra, de lo contrario None.
        """
        return await self.game_repo.get_by_id(game_id)

    async def get_all_games(self, skip: int = 0, limit: int = 100) -> List[Game]:
        """
        Obtiene una lista de todos los juegos con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de juegos.
        """
        return await self.game_repo.get_all(skip=skip, limit=limit)

    async def create_game(self, game_data: GameCreate) -> Game:
        """
        Crea un nuevo juego.

        Args:
            game_data: Datos para la creación del juego.

        Returns:
            El juego recién creado.
        """
        return await self.game_repo.create(game_data.model_dump())

    async def update_game(self, game_id: int, game_data: GameUpdate) -> Optional[Game]:
        """
        Actualiza un juego existente.

        Args:
            game_id: ID del juego a actualizar.
            game_data: Datos para la actualización.

        Returns:
            El juego actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el juego no se encuentra.
        """
        game = await self.game_repo.update(game_id, game_data.model_dump(exclude_unset=True))
        if not game:
            raise NotFoundException("Juego no encontrado")
        return game

    async def delete_game(self, game_id: int) -> bool:
        """
        Elimina (soft delete) un juego.

        Args:
            game_id: ID del juego a eliminar.

        Returns:
            True si el juego fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el juego no se encuentra.
        """
        success = await self.game_repo.delete(game_id)
        if not success:
            raise NotFoundException("Juego no encontrado")
        return success

    async def get_game_by_name(self, name: str) -> Optional[Game]:
        """
        Obtiene un juego por nombre.

        Args:
            name: Nombre del juego.

        Returns:
            El juego si se encuentra, de lo contrario None.
        """
        return await self.game_repo.get_by_name(name)

    async def get_game_by_slug(self, slug: str) -> Optional[Game]:
        """
        Obtiene un juego por slug.

        Args:
            slug: Slug del juego.

        Returns:
            El juego si se encuentra, de lo contrario None.
        """
        return await self.game_repo.get_by_slug(slug)

    async def get_games_by_owner_id(self, owner_id: int) -> List[Game]:
        """
        Obtiene juegos por ID del propietario.

        Args:
            owner_id: ID del propietario del juego.

        Returns:
            Una lista de juegos.
        """
        return await self.game_repo.get_by_owner_id(owner_id)