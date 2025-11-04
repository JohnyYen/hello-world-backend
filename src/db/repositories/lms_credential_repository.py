from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from .base_repository import BaseRepository
from src.models.lms_credential import LMSCredential


class LMSCredentialRepository(BaseRepository[LMSCredential]):
    """
    Repositorio específico para el modelo LMSCredential.
    
    Hereda todas las operaciones CRUD del BaseRepository.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, LMSCredential)

    async def get_by_platform_name(self, platform_name: str, include_deleted: bool = False) -> Optional[LMSCredential]:
        """
        Obtiene una credencial LMS por nombre de plataforma.
        
        Args:
            platform_name: Nombre de la plataforma LMS
            include_deleted: Si True, incluye credenciales marcadas como eliminadas
            
        Returns:
            LMSCredential: Instancia del modelo LMSCredential si se encuentra, None en caso contrario
        """
        filters = {"platform_name": platform_name}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)

    async def get_by_user_id(self, user_id: int, include_deleted: bool = False) -> Optional[LMSCredential]:
        """
        Obtiene una credencial LMS por ID de usuario.
        
        Args:
            user_id: ID del usuario
            include_deleted: Si True, incluye credenciales marcadas como eliminadas
            
        Returns:
            LMSCredential: Instancia del modelo LMSCredential si se encuentra, None en caso contrario
        """
        filters = {"user_id": user_id}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)