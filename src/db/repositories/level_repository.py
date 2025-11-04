from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .base_repository import BaseRepository
from src.models.level import Level


class LevelRepository(BaseRepository[Level]):
    """
    Repositorio específico para el modelo Level.
    
    Hereda todas las operaciones CRUD del BaseRepository.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, Level)

    async def get_by_game_id(self, game_id: int, include_deleted: bool = False) -> List[Level]:
        """
        Obtiene niveles por ID de juego.
        
        Args:
            game_id: ID del juego
            include_deleted: Si True, incluye niveles marcados como eliminados
            
        Returns:
            List[Level]: Lista de niveles
        """
        filters = {"game_id": game_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)

    async def get_by_level_number(self, game_id: int, level_number: int, include_deleted: bool = False) -> Optional[Level]:
        """
        Obtiene un nivel por ID de juego y número de nivel.
        
        Args:
            game_id: ID del juego
            level_number: Número del nivel
            include_deleted: Si True, incluye niveles marcados como eliminados
            
        Returns:
            Level: Instancia del modelo Level si se encuentra, None en caso contrario
        """
        filters = {"game_id": game_id, "level_number": level_number}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)

    async def get_by_name(self, name: str, include_deleted: bool = False) -> Optional[Level]:
        """
        Obtiene un nivel por nombre.
        
        Args:
            name: Nombre del nivel
            include_deleted: Si True, incluye niveles marcados como eliminados
            
        Returns:
            Level: Instancia del modelo Level si se encuentra, None en caso contrario
        """
        filters = {"name": name}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)