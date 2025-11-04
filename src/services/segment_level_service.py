# app/services/segment_level_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.segment_level_repository import SegmentLevelRepository
from src.schemas.segment_level import SegmentLevelCreate, SegmentLevelUpdate
from src.models.segment_level import SegmentLevel
from src.core.exceptions import NotFoundException


class SegmentLevelService:
    """
    Servicio para gestionar la lógica de negocio de segmentos de nivel.

    Proporciona una capa de abstracción sobre el repositorio de segmentos de nivel,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.segment_level_repo = SegmentLevelRepository(db)

    async def get_segment_level_by_id(self, segment_level_id: int) -> Optional[SegmentLevel]:
        """
        Obtiene un segmento de nivel por su ID.

        Args:
            segment_level_id: ID del segmento de nivel a buscar.

        Returns:
            El segmento de nivel si se encuentra, de lo contrario None.
        """
        return await self.segment_level_repo.get_by_id(segment_level_id)

    async def get_all_segment_levels(self, skip: int = 0, limit: int = 100) -> List[SegmentLevel]:
        """
        Obtiene una lista de todos los segmentos de nivel con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de segmentos de nivel.
        """
        return await self.segment_level_repo.get_all(skip=skip, limit=limit)

    async def create_segment_level(self, segment_level_data: SegmentLevelCreate) -> SegmentLevel:
        """
        Crea un nuevo segmento de nivel.

        Args:
            segment_level_data: Datos para la creación del segmento de nivel.

        Returns:
            El segmento de nivel recién creado.
        """
        return await self.segment_level_repo.create(segment_level_data.model_dump())

    async def update_segment_level(self, segment_level_id: int, segment_level_data: SegmentLevelUpdate) -> Optional[SegmentLevel]:
        """
        Actualiza un segmento de nivel existente.

        Args:
            segment_level_id: ID del segmento de nivel a actualizar.
            segment_level_data: Datos para la actualización.

        Returns:
            El segmento de nivel actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el segmento de nivel no se encuentra.
        """
        segment_level = await self.segment_level_repo.update(segment_level_id, segment_level_data.model_dump(exclude_unset=True))
        if not segment_level:
            raise NotFoundException("Segmento de nivel no encontrado")
        return segment_level

    async def delete_segment_level(self, segment_level_id: int) -> bool:
        """
        Elimina (soft delete) un segmento de nivel.

        Args:
            segment_level_id: ID del segmento de nivel a eliminar.

        Returns:
            True si el segmento de nivel fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el segmento de nivel no se encuentra.
        """
        success = await self.segment_level_repo.delete(segment_level_id)
        if not success:
            raise NotFoundException("Segmento de nivel no encontrado")
        return success

    async def get_segment_levels_by_level_id(self, level_id: int) -> List[SegmentLevel]:
        """
        Obtiene segmentos de nivel por ID de nivel.

        Args:
            level_id: ID del nivel.

        Returns:
            Una lista de segmentos de nivel.
        """
        return await self.segment_level_repo.get_by_level_id(level_id)

    async def get_segment_level_by_segment_name(self, segment_name: str) -> Optional[SegmentLevel]:
        """
        Obtiene un segmento de nivel por nombre de segmento.

        Args:
            segment_name: Nombre del segmento.

        Returns:
            El segmento de nivel si se encuentra, de lo contrario None.
        """
        return await self.segment_level_repo.get_by_segment_name(segment_name)