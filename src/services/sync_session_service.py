# app/services/sync_session_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.sync_session_repository import SyncSessionRepository
from src.schemas.sync_session import SyncSessionCreate, SyncSessionUpdate
from src.models.sync_session import SyncSession
from src.core.exceptions import NotFoundException


class SyncSessionService:
    """
    Servicio para gestionar la lógica de negocio de sesiones de sincronización.

    Proporciona una capa de abstracción sobre el repositorio de sesiones de sincronización,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.sync_session_repo = SyncSessionRepository(db)

    async def get_sync_session_by_id(self, sync_session_id: int) -> Optional[SyncSession]:
        """
        Obtiene una sesión de sincronización por su ID.

        Args:
            sync_session_id: ID de la sesión de sincronización a buscar.

        Returns:
            La sesión de sincronización si se encuentra, de lo contrario None.
        """
        return await self.sync_session_repo.get_by_id(sync_session_id)

    async def get_all_sync_sessions(self, skip: int = 0, limit: int = 100) -> List[SyncSession]:
        """
        Obtiene una lista de todas las sesiones de sincronización con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de sesiones de sincronización.
        """
        return await self.sync_session_repo.get_all(skip=skip, limit=limit)

    async def create_sync_session(self, sync_session_data: SyncSessionCreate) -> SyncSession:
        """
        Crea una nueva sesión de sincronización.

        Args:
            sync_session_data: Datos para la creación de la sesión de sincronización.

        Returns:
            La sesión de sincronización recién creada.
        """
        return await self.sync_session_repo.create(sync_session_data.model_dump())

    async def update_sync_session(self, sync_session_id: int, sync_session_data: SyncSessionUpdate) -> Optional[SyncSession]:
        """
        Actualiza una sesión de sincronización existente.

        Args:
            sync_session_id: ID de la sesión de sincronización a actualizar.
            sync_session_data: Datos para la actualización.

        Returns:
            La sesión de sincronización actualizada si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si la sesión de sincronización no se encuentra.
        """
        sync_session = await self.sync_session_repo.update(sync_session_id, sync_session_data.model_dump(exclude_unset=True))
        if not sync_session:
            raise NotFoundException("Sesión de sincronización no encontrada")
        return sync_session

    async def delete_sync_session(self, sync_session_id: int) -> bool:
        """
        Elimina (soft delete) una sesión de sincronización.

        Args:
            sync_session_id: ID de la sesión de sincronización a eliminar.

        Returns:
            True si la sesión de sincronización fue eliminada, False en caso contrario.
        
        Raises:
            NotFoundException: Si la sesión de sincronización no se encuentra.
        """
        success = await self.sync_session_repo.delete(sync_session_id)
        if not success:
            raise NotFoundException("Sesión de sincronización no encontrada")
        return success

    async def get_sync_sessions_by_user_id(self, user_id: int) -> List[SyncSession]:
        """
        Obtiene sesiones de sincronización por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            Una lista de sesiones de sincronización.
        """
        return await self.sync_session_repo.get_by_user_id(user_id)

    async def get_sync_sessions_by_status(self, status: str) -> List[SyncSession]:
        """
        Obtiene sesiones de sincronización por estado.

        Args:
            status: Estado de la sesión de sincronización.

        Returns:
            Una lista de sesiones de sincronización.
        """
        return await self.sync_session_repo.get_by_status(status)

    async def get_sync_sessions_by_user_id_and_status(self, user_id: int, status: str) -> List[SyncSession]:
        """
        Obtiene sesiones de sincronización por ID de usuario y estado.

        Args:
            user_id: ID del usuario.
            status: Estado de la sesión de sincronización.

        Returns:
            Una lista de sesiones de sincronización.
        """
        return await self.sync_session_repo.get_by_user_id_and_status(user_id, status)

    async def get_latest_session_by_user(self, user_id: int) -> Optional[SyncSession]:
        """
        Obtiene la sesión de sincronización más reciente por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            La sesión más reciente si se encuentra, de lo contrario None.
        """
        return await self.sync_session_repo.get_latest_session_by_user(user_id)