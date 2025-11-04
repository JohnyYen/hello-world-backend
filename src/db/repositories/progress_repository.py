from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .base_repository import BaseRepository
from src.models.progress import Progress


class ProgressRepository(BaseRepository[Progress]):
    """
    Repositorio específico para el modelo Progress.
    
    Hereda todas las operaciones CRUD del BaseRepository.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, Progress)

    async def get_by_user_id(self, user_id: int, include_deleted: bool = False) -> List[Progress]:
        """
        Obtiene progresos por ID de usuario.
        
        Args:
            user_id: ID del usuario
            include_deleted: Si True, incluye progresos marcados como eliminados
            
        Returns:
            List[Progress]: Lista de progresos
        """
        filters = {"user_id": user_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)

    async def get_by_user_and_level(self, user_id: int, level_id: int, include_deleted: bool = False) -> Optional[Progress]:
        """
        Obtiene progreso por ID de usuario y nivel.
        
        Args:
            user_id: ID del usuario
            level_id: ID del nivel
            include_deleted: Si True, incluye progresos marcados como eliminados
            
        Returns:
            Progress: Instancia del modelo Progress si se encuentra, None en caso contrario
        """
        filters = {"user_id": user_id, "level_id": level_id}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)

    async def get_by_level_id(self, level_id: int, include_deleted: bool = False) -> List[Progress]:
        """
        Obtiene progresos por ID de nivel.
        
        Args:
            level_id: ID del nivel
            include_deleted: Si True, incluye progresos marcados como eliminados
            
        Returns:
            List[Progress]: Lista de progresos
        """
        filters = {"level_id": level_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)