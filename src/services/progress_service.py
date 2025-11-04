# app/services/progress_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.progress_repository import ProgressRepository
from src.schemas.progress import ProgressCreate, ProgressUpdate
from src.models.progress import Progress
from src.core.exceptions import NotFoundException


class ProgressService:
    """
    Servicio para gestionar la lógica de negocio de progresos.

    Proporciona una capa de abstracción sobre el repositorio de progresos,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.progress_repo = ProgressRepository(db)

    async def get_progress_by_id(self, progress_id: int) -> Optional[Progress]:
        """
        Obtiene un progreso por su ID.

        Args:
            progress_id: ID del progreso a buscar.

        Returns:
            El progreso si se encuentra, de lo contrario None.
        """
        return await self.progress_repo.get_by_id(progress_id)

    async def get_all_progress(self, skip: int = 0, limit: int = 100) -> List[Progress]:
        """
        Obtiene una lista de todos los progresos con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de progresos.
        """
        return await self.progress_repo.get_all(skip=skip, limit=limit)

    async def create_progress(self, progress_data: ProgressCreate) -> Progress:
        """
        Crea un nuevo progreso.

        Args:
            progress_data: Datos para la creación del progreso.

        Returns:
            El progreso recién creado.
        """
        return await self.progress_repo.create(progress_data.model_dump())

    async def update_progress(self, progress_id: int, progress_data: ProgressUpdate) -> Optional[Progress]:
        """
        Actualiza un progreso existente.

        Args:
            progress_id: ID del progreso a actualizar.
            progress_data: Datos para la actualización.

        Returns:
            El progreso actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el progreso no se encuentra.
        """
        progress = await self.progress_repo.update(progress_id, progress_data.model_dump(exclude_unset=True))
        if not progress:
            raise NotFoundException("Progreso no encontrado")
        return progress

    async def delete_progress(self, progress_id: int) -> bool:
        """
        Elimina (soft delete) un progreso.

        Args:
            progress_id: ID del progreso a eliminar.

        Returns:
            True si el progreso fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el progreso no se encuentra.
        """
        success = await self.progress_repo.delete(progress_id)
        if not success:
            raise NotFoundException("Progreso no encontrado")
        return success

    async def get_progress_by_user_id(self, user_id: int) -> List[Progress]:
        """
        Obtiene progresos por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            Una lista de progresos.
        """
        return await self.progress_repo.get_by_user_id(user_id)

    async def get_progress_by_user_and_level(self, user_id: int, level_id: int) -> Optional[Progress]:
        """
        Obtiene progreso por ID de usuario y nivel.

        Args:
            user_id: ID del usuario.
            level_id: ID del nivel.

        Returns:
            El progreso si se encuentra, de lo contrario None.
        """
        return await self.progress_repo.get_by_user_and_level(user_id, level_id)

    async def get_progress_by_level_id(self, level_id: int) -> List[Progress]:
        """
        Obtiene progresos por ID de nivel.

        Args:
            level_id: ID del nivel.

        Returns:
            Una lista de progresos.
        """
        return await self.progress_repo.get_by_level_id(level_id)