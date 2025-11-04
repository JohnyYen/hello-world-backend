# app/services/game_instance_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.game_instance_repository import GameInstanceRepository
from src.schemas.game_instance import GameInstanceCreate, GameInstanceUpdate
from src.models.game_instance import GameInstance
from src.core.exceptions import NotFoundException


class GameInstanceService:
    """
    Servicio para gestionar la lógica de negocio de instancias de juego.

    Proporciona una capa de abstracción sobre el repositorio de instancias de juego,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.game_instance_repo = GameInstanceRepository(db)

    async def get_game_instance_by_id(self, game_instance_id: int) -> Optional[GameInstance]:
        """
        Obtiene una instancia de juego por su ID.

        Args:
            game_instance_id: ID de la instancia de juego a buscar.

        Returns:
            La instancia de juego si se encuentra, de lo contrario None.
        """
        return await self.game_instance_repo.get_by_id(game_instance_id)

    async def get_all_game_instances(self, skip: int = 0, limit: int = 100) -> List[GameInstance]:
        """
        Obtiene una lista de todas las instancias de juego con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de instancias de juego.
        """
        return await self.game_instance_repo.get_all(skip=skip, limit=limit)

    async def create_game_instance(self, game_instance_data: GameInstanceCreate) -> GameInstance:
        """
        Crea una nueva instancia de juego.

        Args:
            game_instance_data: Datos para la creación de la instancia de juego.

        Returns:
            La instancia de juego recién creada.
        """
        return await self.game_instance_repo.create(game_instance_data.model_dump())

    async def update_game_instance(self, game_instance_id: int, game_instance_data: GameInstanceUpdate) -> Optional[GameInstance]:
        """
        Actualiza una instancia de juego existente.

        Args:
            game_instance_id: ID de la instancia de juego a actualizar.
            game_instance_data: Datos para la actualización.

        Returns:
            La instancia de juego actualizada si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si la instancia de juego no se encuentra.
        """
        game_instance = await self.game_instance_repo.update(game_instance_id, game_instance_data.model_dump(exclude_unset=True))
        if not game_instance:
            raise NotFoundException("Instancia de juego no encontrada")
        return game_instance

    async def delete_game_instance(self, game_instance_id: int) -> bool:
        """
        Elimina (soft delete) una instancia de juego.

        Args:
            game_instance_id: ID de la instancia de juego a eliminar.

        Returns:
            True si la instancia de juego fue eliminada, False en caso contrario.
        
        Raises:
            NotFoundException: Si la instancia de juego no se encuentra.
        """
        success = await self.game_instance_repo.delete(game_instance_id)
        if not success:
            raise NotFoundException("Instancia de juego no encontrada")
        return success

    async def get_game_instances_by_game_id(self, game_id: int) -> List[GameInstance]:
        """
        Obtiene instancias de juego por ID de juego.

        Args:
            game_id: ID del juego.

        Returns:
            Una lista de instancias de juego.
        """
        return await self.game_instance_repo.get_by_game_id(game_id)

    async def get_game_instances_by_user_id(self, user_id: int) -> List[GameInstance]:
        """
        Obtiene instancias de juego por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            Una lista de instancias de juego.
        """
        return await self.game_instance_repo.get_by_user_id(user_id)

    async def get_game_instances_by_status(self, status: str) -> List[GameInstance]:
        """
        Obtiene instancias de juego por estado.

        Args:
            status: Estado de la instancia de juego.

        Returns:
            Una lista de instancias de juego.
        """
        return await self.game_instance_repo.get_by_status(status)

    async def get_game_instance_by_game_and_user(self, game_id: int, user_id: int) -> Optional[GameInstance]:
        """
        Obtiene una instancia de juego por ID de juego y ID de usuario.

        Args:
            game_id: ID del juego.
            user_id: ID del usuario.

        Returns:
            La instancia de juego si se encuentra, de lo contrario None.
        """
        return await self.game_instance_repo.get_by_game_and_user(game_id, user_id)