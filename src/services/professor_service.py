# app/services/professor_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.professor_repository import ProfessorRepository
from src.schemas.professor import ProfessorCreate, ProfessorUpdate
from src.models.professor import Professor
from src.core.exceptions import NotFoundException


class ProfessorService:
    """
    Servicio para gestionar la lógica de negocio de profesores.

    Proporciona una capa de abstracción sobre el repositorio de profesores,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.professor_repo = ProfessorRepository(db)

    async def get_professor_by_id(self, professor_id: int) -> Optional[Professor]:
        """
        Obtiene un profesor por su ID.

        Args:
            professor_id: ID del profesor a buscar.

        Returns:
            El profesor si se encuentra, de lo contrario None.
        """
        return await self.professor_repo.get_by_id(professor_id)

    async def get_all_professors(self, skip: int = 0, limit: int = 100) -> List[Professor]:
        """
        Obtiene una lista de todos los profesores con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de profesores.
        """
        return await self.professor_repo.get_all(skip=skip, limit=limit)

    async def create_professor(self, professor_data: ProfessorCreate) -> Professor:
        """
        Crea un nuevo profesor.

        Args:
            professor_data: Datos para la creación del profesor.

        Returns:
            El profesor recién creado.
        """
        return await self.professor_repo.create(professor_data.model_dump())

    async def update_professor(self, professor_id: int, professor_data: ProfessorUpdate) -> Optional[Professor]:
        """
        Actualiza un profesor existente.

        Args:
            professor_id: ID del profesor a actualizar.
            professor_data: Datos para la actualización.

        Returns:
            El profesor actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el profesor no se encuentra.
        """
        professor = await self.professor_repo.update(professor_id, professor_data.model_dump(exclude_unset=True))
        if not professor:
            raise NotFoundException("Profesor no encontrado")
        return professor

    async def delete_professor(self, professor_id: int) -> bool:
        """
        Elimina (soft delete) un profesor.

        Args:
            professor_id: ID del profesor a eliminar.

        Returns:
            True si el profesor fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el profesor no se encuentra.
        """
        success = await self.professor_repo.delete(professor_id)
        if not success:
            raise NotFoundException("Profesor no encontrado")
        return success

    async def get_professor_by_user_id(self, user_id: int) -> Optional[Professor]:
        """
        Obtiene un profesor por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            El profesor si se encuentra, de lo contrario None.
        """
        return await self.professor_repo.get_by_user_id(user_id)

    async def get_professor_by_professor_id(self, professor_id: str) -> Optional[Professor]:
        """
        Obtiene un profesor por ID de profesor.

        Args:
            professor_id: ID del profesor.

        Returns:
            El profesor si se encuentra, de lo contrario None.
        """
        return await self.professor_repo.get_by_professor_id(professor_id)