from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from .base_repository import BaseRepository
from src.models.feedback import Feedback


class FeedbackRepository(BaseRepository[Feedback]):
    """
    Repositorio específico para el modelo Feedback.
    
    Hereda todas las operaciones CRUD del BaseRepository.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, Feedback)

    async def get_by_user_id(self, user_id: int, include_deleted: bool = False) -> List[Feedback]:
        """
        Obtiene feedback por ID de usuario.
        
        Args:
            user_id: ID del usuario
            include_deleted: Si True, incluye feedback marcados como eliminados
            
        Returns:
            List[Feedback]: Lista de feedback
        """
        filters = {"user_id": user_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)

    async def get_by_game_instance_id(self, game_instance_id: int, include_deleted: bool = False) -> List[Feedback]:
        """
        Obtiene feedback por ID de instancia de juego.
        
        Args:
            game_instance_id: ID de la instancia de juego
            include_deleted: Si True, incluye feedback marcados como eliminados
            
        Returns:
            List[Feedback]: Lista de feedback
        """
        filters = {"game_instance_id": game_instance_id}
        return await self.get_by_filters(filters, include_deleted=include_deleted)

    async def get_by_rating(self, rating: int, include_deleted: bool = False) -> List[Feedback]:
        """
        Obtiene feedback por calificación.
        
        Args:
            rating: Calificación del feedback
            include_deleted: Si True, incluye feedback marcados como eliminados
            
        Returns:
            List[Feedback]: Lista de feedback
        """
        filters = {"rating": rating}
        return await self.get_by_filters(filters, include_deleted=include_deleted)