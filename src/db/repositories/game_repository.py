from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .base_repository import BaseRepository
from src.models.game import Game


class GameRepository(BaseRepository[Game]):
    """
    Repositorio específico para el modelo Game.
    
    Hereda todas las operaciones CRUD del BaseRepository.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, Game)

    async def get_by_name(self, name: str, include_deleted: bool = False) -> Optional[Game]:
        """
        Obtiene un juego por nombre.
        
        Args:
            name: Nombre del juego
            include_deleted: Si True, incluye juegos marcados como eliminados
            
        Returns:
            Game: Instancia del modelo Game si se encuentra, None en caso contrario
        """
        filters = {"name": name}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)

    async def get_by_slug(self, slug: str, include_deleted: bool = False) -> Optional[Game]:
        """
        Obtiene un juego por slug.
        
        Args:
            slug: Slug del juego
            include_deleted: Si True, incluye juegos marcados como eliminados
            
        Returns:
            Game: Instancia del modelo Game si se encuentra, None en caso contrario
        """
        filters = {"slug": slug}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)

    async def get_by_owner_id(self, owner_id: int, include_deleted: bool = False) -> List[Game]:
        """
        Obtiene juegos por ID del propietario.
        
        Args:
            owner_id: ID del propietario del juego
            include_deleted: Si True, incluye juegos marcados como eliminados
            
        Returns:
            List[Game]: Lista de juegos
        """
        filters = {"owner_id": owner_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)