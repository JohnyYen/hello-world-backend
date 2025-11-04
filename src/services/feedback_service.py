# app/services/feedback_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.feedback_repository import FeedbackRepository
from src.schemas.feedback import FeedbackCreate, FeedbackUpdate
from src.models.feedback import Feedback
from src.core.exceptions import NotFoundException


class FeedbackService:
    """
    Servicio para gestionar la lógica de negocio de feedback.

    Proporciona una capa de abstracción sobre el repositorio de feedback,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.feedback_repo = FeedbackRepository(db)

    async def get_feedback_by_id(self, feedback_id: int) -> Optional[Feedback]:
        """
        Obtiene un feedback por su ID.

        Args:
            feedback_id: ID del feedback a buscar.

        Returns:
            El feedback si se encuentra, de lo contrario None.
        """
        return await self.feedback_repo.get_by_id(feedback_id)

    async def get_all_feedback(self, skip: int = 0, limit: int = 100) -> List[Feedback]:
        """
        Obtiene una lista de todos los feedback con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de feedback.
        """
        return await self.feedback_repo.get_all(skip=skip, limit=limit)

    async def create_feedback(self, feedback_data: FeedbackCreate) -> Feedback:
        """
        Crea un nuevo feedback.

        Args:
            feedback_data: Datos para la creación del feedback.

        Returns:
            El feedback recién creado.
        """
        return await self.feedback_repo.create(feedback_data.model_dump())

    async def update_feedback(self, feedback_id: int, feedback_data: FeedbackUpdate) -> Optional[Feedback]:
        """
        Actualiza un feedback existente.

        Args:
            feedback_id: ID del feedback a actualizar.
            feedback_data: Datos para la actualización.

        Returns:
            El feedback actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el feedback no se encuentra.
        """
        feedback = await self.feedback_repo.update(feedback_id, feedback_data.model_dump(exclude_unset=True))
        if not feedback:
            raise NotFoundException("Feedback no encontrado")
        return feedback

    async def delete_feedback(self, feedback_id: int) -> bool:
        """
        Elimina (soft delete) un feedback.

        Args:
            feedback_id: ID del feedback a eliminar.

        Returns:
            True si el feedback fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el feedback no se encuentra.
        """
        success = await self.feedback_repo.delete(feedback_id)
        if not success:
            raise NotFoundException("Feedback no encontrado")
        return success

    async def get_feedback_by_user_id(self, user_id: int) -> List[Feedback]:
        """
        Obtiene feedback por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            Una lista de feedback.
        """
        return await self.feedback_repo.get_by_user_id(user_id)

    async def get_feedback_by_game_instance_id(self, game_instance_id: int) -> List[Feedback]:
        """
        Obtiene feedback por ID de instancia de juego.

        Args:
            game_instance_id: ID de la instancia de juego.

        Returns:
            Una lista de feedback.
        """
        return await self.feedback_repo.get_by_game_instance_id(game_instance_id)

    async def get_feedback_by_rating(self, rating: int) -> List[Feedback]:
        """
        Obtiene feedback por calificación.

        Args:
            rating: Calificación del feedback.

        Returns:
            Una lista de feedback.
        """
        return await self.feedback_repo.get_by_rating(rating)