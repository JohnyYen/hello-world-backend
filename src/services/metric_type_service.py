# app/services/metric_type_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.metric_type_repository import MetricTypeRepository
from src.schemas.metric_type import MetricTypeCreate, MetricTypeUpdate
from src.models.metric_type import MetricType
from src.core.exceptions import NotFoundException


class MetricTypeService:
    """
    Servicio para gestionar la lógica de negocio de tipos de métrica.

    Proporciona una capa de abstracción sobre el repositorio de tipos de métrica,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.metric_type_repo = MetricTypeRepository(db)

    async def get_metric_type_by_id(self, metric_type_id: int) -> Optional[MetricType]:
        """
        Obtiene un tipo de métrica por su ID.

        Args:
            metric_type_id: ID del tipo de métrica a buscar.

        Returns:
            El tipo de métrica si se encuentra, de lo contrario None.
        """
        return await self.metric_type_repo.get_by_id(metric_type_id)

    async def get_all_metric_types(self, skip: int = 0, limit: int = 100) -> List[MetricType]:
        """
        Obtiene una lista de todos los tipos de métrica con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de tipos de métrica.
        """
        return await self.metric_type_repo.get_all(skip=skip, limit=limit)

    async def create_metric_type(self, metric_type_data: MetricTypeCreate) -> MetricType:
        """
        Crea un nuevo tipo de métrica.

        Args:
            metric_type_data: Datos para la creación del tipo de métrica.

        Returns:
            El tipo de métrica recién creado.
        """
        return await self.metric_type_repo.create(metric_type_data.model_dump())

    async def update_metric_type(self, metric_type_id: int, metric_type_data: MetricTypeUpdate) -> Optional[MetricType]:
        """
        Actualiza un tipo de métrica existente.

        Args:
            metric_type_id: ID del tipo de métrica a actualizar.
            metric_type_data: Datos para la actualización.

        Returns:
            El tipo de métrica actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el tipo de métrica no se encuentra.
        """
        metric_type = await self.metric_type_repo.update(metric_type_id, metric_type_data.model_dump(exclude_unset=True))
        if not metric_type:
            raise NotFoundException("Tipo de métrica no encontrado")
        return metric_type

    async def delete_metric_type(self, metric_type_id: int) -> bool:
        """
        Elimina (soft delete) un tipo de métrica.

        Args:
            metric_type_id: ID del tipo de métrica a eliminar.

        Returns:
            True si el tipo de métrica fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el tipo de métrica no se encuentra.
        """
        success = await self.metric_type_repo.delete(metric_type_id)
        if not success:
            raise NotFoundException("Tipo de métrica no encontrado")
        return success

    async def get_metric_type_by_name(self, name: str) -> Optional[MetricType]:
        """
        Obtiene un tipo de métrica por nombre.

        Args:
            name: Nombre del tipo de métrica.

        Returns:
            El tipo de métrica si se encuentra, de lo contrario None.
        """
        return await self.metric_type_repo.get_by_name(name)

    async def get_metric_type_by_code(self, code: str) -> Optional[MetricType]:
        """
        Obtiene un tipo de métrica por código.

        Args:
            code: Código del tipo de métrica.

        Returns:
            El tipo de métrica si se encuentra, de lo contrario None.
        """
        return await self.metric_type_repo.get_by_code(code)