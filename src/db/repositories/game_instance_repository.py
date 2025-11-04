from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .base_repository import BaseRepository
from src.models.game_instance import GameInstance


class GameInstanceRepository(BaseRepository[GameInstance]):
    """
    Repositorio específico para el modelo GameInstance.
    
    Hereda todas las operaciones CRUD del BaseRepository.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, GameInstance)

    async def get_by_game_id(self, game_id: int, include_deleted: bool = False) -> List[GameInstance]:
        """
        Obtiene instancias de juego por ID de juego.
        
        Args:
            game_id: ID del juego
            include_deleted: Si True, incluye instancias marcadas como eliminadas
            
        Returns:
            List[GameInstance]: Lista de instancias de juego
        """
        filters = {"game_id": game_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)

    async def get_by_user_id(self, user_id: int, include_deleted: bool = False) -> List[GameInstance]:
        """
        Obtiene instancias de juego por ID de usuario.
        
        Args:
            user_id: ID del usuario
            include_deleted: Si True, incluye instancias marcadas como eliminadas
            
        Returns:
            List[GameInstance]: Lista de instancias de juego
        """
        filters = {"user_id": user_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)

    async def get_by_status(self, status: str, include_deleted: bool = False) -> List[GameInstance]:
        """
        Obtiene instancias de juego por estado.
        
        Args:
            status: Estado de la instancia de juego
            include_deleted: Si True, incluye instancias marcadas como eliminadas
            
        Returns:
            List[GameInstance]: Lista de instancias de juego
        """
        filters = {"status": status}
        return await self.get_by_filters(filters, include_deleted=include_deleted)

    async def get_by_game_and_user(self, game_id: int, user_id: int, include_deleted: bool = False) -> Optional[GameInstance]:
        """
        Obtiene una instancia de juego por ID de juego y ID de usuario.
        
        Args:
            game_id: ID del juego
            user_id: ID del usuario
            include_deleted: Si True, incluye instancias marcadas como eliminadas
            
        Returns:
            GameInstance: Instancia del modelo GameInstance si se encuentra, None en caso contrario
        """
        filters = {"game_id": game_id, "user_id": user_id}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)