# app/services/lms_credential_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.lms_credential_repository import LMSCredentialRepository
from src.schemas.lms_credential import LMSCredentialCreate, LMSCredentialUpdate
from src.models.lms_credential import LMSCredential
from src.core.exceptions import NotFoundException


class LMSCredentialService:
    """
    Servicio para gestionar la lógica de negocio de credenciales LMS.

    Proporciona una capa de abstracción sobre el repositorio de credenciales LMS,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.lms_credential_repo = LMSCredentialRepository(db)

    async def get_lms_credential_by_id(self, lms_credential_id: int) -> Optional[LMSCredential]:
        """
        Obtiene una credencial LMS por su ID.

        Args:
            lms_credential_id: ID de la credencial LMS a buscar.

        Returns:
            La credencial LMS si se encuentra, de lo contrario None.
        """
        return await self.lms_credential_repo.get_by_id(lms_credential_id)

    async def get_all_lms_credentials(self, skip: int = 0, limit: int = 100) -> List[LMSCredential]:
        """
        Obtiene una lista de todas las credenciales LMS con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de credenciales LMS.
        """
        return await self.lms_credential_repo.get_all(skip=skip, limit=limit)

    async def create_lms_credential(self, lms_credential_data: LMSCredentialCreate) -> LMSCredential:
        """
        Crea una nueva credencial LMS.

        Args:
            lms_credential_data: Datos para la creación de la credencial LMS.

        Returns:
            La credencial LMS recién creada.
        """
        return await self.lms_credential_repo.create(lms_credential_data.model_dump())

    async def update_lms_credential(self, lms_credential_id: int, lms_credential_data: LMSCredentialUpdate) -> Optional[LMSCredential]:
        """
        Actualiza una credencial LMS existente.

        Args:
            lms_credential_id: ID de la credencial LMS a actualizar.
            lms_credential_data: Datos para la actualización.

        Returns:
            La credencial LMS actualizada si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si la credencial LMS no se encuentra.
        """
        lms_credential = await self.lms_credential_repo.update(lms_credential_id, lms_credential_data.model_dump(exclude_unset=True))
        if not lms_credential:
            raise NotFoundException("Credencial LMS no encontrada")
        return lms_credential

    async def delete_lms_credential(self, lms_credential_id: int) -> bool:
        """
        Elimina (soft delete) una credencial LMS.

        Args:
            lms_credential_id: ID de la credencial LMS a eliminar.

        Returns:
            True si la credencial LMS fue eliminada, False en caso contrario.
        
        Raises:
            NotFoundException: Si la credencial LMS no se encuentra.
        """
        success = await self.lms_credential_repo.delete(lms_credential_id)
        if not success:
            raise NotFoundException("Credencial LMS no encontrada")
        return success

    async def get_lms_credential_by_platform_name(self, platform_name: str) -> Optional[LMSCredential]:
        """
        Obtiene una credencial LMS por nombre de plataforma.

        Args:
            platform_name: Nombre de la plataforma LMS.

        Returns:
            La credencial LMS si se encuentra, de lo contrario None.
        """
        return await self.lms_credential_repo.get_by_platform_name(platform_name)