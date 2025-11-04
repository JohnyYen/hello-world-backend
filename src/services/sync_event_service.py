# app/services/sync_event_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.sync_event_repository import SyncEventRepository
from src.schemas.sync_event import SyncEventCreate, SyncEventUpdate
from src.models.sync_event import SyncEvent
from src.core.exceptions import NotFoundException


class SyncEventService:
    """
    Servicio para gestionar la lógica de negocio de eventos de sincronización.

    Proporciona una capa de abstracción sobre el repositorio de eventos de sincronización,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.sync_event_repo = SyncEventRepository(db)

    async def get_sync_event_by_id(self, sync_event_id: int) -> Optional[SyncEvent]:
        """
        Obtiene un evento de sincronización por su ID.

        Args:
            sync_event_id: ID del evento de sincronización a buscar.

        Returns:
            El evento de sincronización si se encuentra, de lo contrario None.
        """
        return await self.sync_event_repo.get_by_id(sync_event_id)

    async def get_all_sync_events(self, skip: int = 0, limit: int = 100) -> List[SyncEvent]:
        """
        Obtiene una lista de todos los eventos de sincronización con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de eventos de sincronización.
        """
        return await self.sync_event_repo.get_all(skip=skip, limit=limit)

    async def create_sync_event(self, sync_event_data: SyncEventCreate) -> SyncEvent:
        """
        Crea un nuevo evento de sincronización.

        Args:
            sync_event_data: Datos para la creación del evento de sincronización.

        Returns:
            El evento de sincronización recién creado.
        """
        return await self.sync_event_repo.create(sync_event_data.model_dump())

    async def update_sync_event(self, sync_event_id: int, sync_event_data: SyncEventUpdate) -> Optional[SyncEvent]:
        """
        Actualiza un evento de sincronización existente.

        Args:
            sync_event_id: ID del evento de sincronización a actualizar.
            sync_event_data: Datos para la actualización.

        Returns:
            El evento de sincronización actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el evento de sincronización no se encuentra.
        """
        sync_event = await self.sync_event_repo.update(sync_event_id, sync_event_data.model_dump(exclude_unset=True))
        if not sync_event:
            raise NotFoundException("Evento de sincronización no encontrado")
        return sync_event

    async def delete_sync_event(self, sync_event_id: int) -> bool:
        """
        Elimina (soft delete) un evento de sincronización.

        Args:
            sync_event_id: ID del evento de sincronización a eliminar.

        Returns:
            True si el evento de sincronización fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el evento de sincronización no se encuentra.
        """
        success = await self.sync_event_repo.delete(sync_event_id)
        if not success:
            raise NotFoundException("Evento de sincronización no encontrado")
        return success

    async def get_sync_events_by_session_id(self, session_id: int) -> List[SyncEvent]:
        """
        Obtiene eventos de sincronización por ID de sesión.

        Args:
            session_id: ID de la sesión de sincronización.

        Returns:
            Una lista de eventos de sincronización.
        """
        return await self.sync_event_repo.get_by_session_id(session_id)

    async def get_sync_events_by_user_id(self, user_id: int) -> List[SyncEvent]:
        """
        Obtiene eventos de sincronización por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            Una lista de eventos de sincronización.
        """
        return await self.sync_event_repo.get_by_user_id(user_id)

    async def get_sync_events_by_event_type(self, event_type: str) -> List[SyncEvent]:
        """
        Obtiene eventos de sincronización por tipo de evento.

        Args:
            event_type: Tipo de evento de sincronización.

        Returns:
            Una lista de eventos de sincronización.
        """
        return await self.sync_event_repo.get_by_event_type(event_type)