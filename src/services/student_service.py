# app/services/student_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.student_repository import StudentRepository
from src.schemas.student import StudentCreate, StudentUpdate
from src.models.student import Student
from src.core.exceptions import NotFoundException


class StudentService:
    """
    Servicio para gestionar la lógica de negocio de estudiantes.

    Proporciona una capa de abstracción sobre el repositorio de estudiantes,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.student_repo = StudentRepository(db)

    async def get_student_by_id(self, student_id: int) -> Optional[Student]:
        """
        Obtiene un estudiante por su ID.

        Args:
            student_id: ID del estudiante a buscar.

        Returns:
            El estudiante si se encuentra, de lo contrario None.
        """
        return await self.student_repo.get_by_id(student_id)

    async def get_all_students(self, skip: int = 0, limit: int = 100) -> List[Student]:
        """
        Obtiene una lista de todos los estudiantes con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de estudiantes.
        """
        return await self.student_repo.get_all(skip=skip, limit=limit)

    async def create_student(self, student_data: StudentCreate) -> Student:
        """
        Crea un nuevo estudiante.

        Args:
            student_data: Datos para la creación del estudiante.

        Returns:
            El estudiante recién creado.
        """
        return await self.student_repo.create(student_data.model_dump())

    async def update_student(self, student_id: int, student_data: StudentUpdate) -> Optional[Student]:
        """
        Actualiza un estudiante existente.

        Args:
            student_id: ID del estudiante a actualizar.
            student_data: Datos para la actualización.

        Returns:
            El estudiante actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el estudiante no se encuentra.
        """
        student = await self.student_repo.update(student_id, student_data.model_dump(exclude_unset=True))
        if not student:
            raise NotFoundException("Estudiante no encontrado")
        return student

    async def delete_student(self, student_id: int) -> bool:
        """
        Elimina (soft delete) un estudiante.

        Args:
            student_id: ID del estudiante a eliminar.

        Returns:
            True si el estudiante fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el estudiante no se encuentra.
        """
        success = await self.student_repo.delete(student_id)
        if not success:
            raise NotFoundException("Estudiante no encontrado")
        return success

    async def get_student_by_user_id(self, user_id: int) -> Optional[Student]:
        """
        Obtiene un estudiante por ID de usuario.

        Args:
            user_id: ID del usuario.

        Returns:
            El estudiante si se encuentra, de lo contrario None.
        """
        return await self.student_repo.get_by_user_id(user_id)

    async def get_student_by_student_id(self, student_id: str) -> Optional[Student]:
        """
        Obtiene un estudiante por ID de estudiante.

        Args:
            student_id: ID del estudiante.

        Returns:
            El estudiante si se encuentra, de lo contrario None.
        """
        return await self.student_repo.get_by_student_id(student_id)