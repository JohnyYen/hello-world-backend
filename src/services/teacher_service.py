from typing import Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from src.db.session import get_db
from src.db.repositories.user_repository import UserRepository
from src.db.repositories.professor_repository import ProfessorRepository
from src.schemas.teacher import TeacherProfileUpdate, TeacherSettingsUpdate
from src.models.user import User
from src.models.professor import Professor
from src.models.teacher_settings import TeacherSettings
from src.core.exceptions import NotFoundException


class TeacherService:
    """
    Servicio para gestionar la lógica de negocio del perfil y configuraciones de profesores.

    Proporciona operaciones específicas para el perfil del profesor autenticado
    y sus configuraciones de dashboard.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.db = db
        self.user_repo = UserRepository(db)
        self.professor_repo = ProfessorRepository(db)

    async def get_teacher_profile(self, user_id: int) -> Optional[dict]:
        """
        Obtiene el perfil completo del profesor autenticado.

        Args:
            user_id: ID del usuario autenticado.

        Returns:
            Diccionario con la información del perfil si se encuentra, de lo contrario None.
        """
        # Obtener el usuario con su rol y profesor
        stmt = (
            select(User)
            .options(selectinload(User.role), selectinload(User.professor))
            .where(User.id == user_id)
        )
        
        result = await self.db.execute(stmt)
        user = result.scalar_one_or_none()
        
        if not user or not user.professor:
            raise NotFoundException("Perfil de profesor no encontrado")
        
        # Retornar la combinación de datos de usuario y profesor
        return {
            "id": user.professor.id,
            "username": user.username,
            "name": user.name,
            "lastname": user.lastname,
            "email": user.email,
            "department": user.professor.department,
            "contact_phone": user.professor.contact_phone,
            "avatar_url": user.avatar_url,
            "is_active": user.is_active,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }

    async def update_teacher_profile(self, user_id: int, profile_data: TeacherProfileUpdate) -> Optional[dict]:
        """
        Actualiza el perfil del profesor autenticado.

        Args:
            user_id: ID del usuario autenticado.
            profile_data: Datos para la actualización del perfil.

        Returns:
            Diccionario con la información actualizada del perfil si se encuentra, de lo contrario None.
        """
        # Obtener el usuario con su profesor
        stmt = (
            select(User)
            .options(selectinload(User.professor))
            .where(User.id == user_id)
        )
        
        result = await self.db.execute(stmt)
        user = result.scalar_one_or_none()
        
        if not user or not user.professor:
            raise NotFoundException("Perfil de profesor no encontrado")
        
        # Actualizar los campos del usuario
        if profile_data.name is not None:
            user.name = profile_data.name
        if profile_data.lastname is not None:
            user.lastname = profile_data.lastname
        if profile_data.email is not None:
            user.email = profile_data.email
        if profile_data.avatar_url is not None:
            user.avatar_url = profile_data.avatar_url

        # Actualizar los campos del profesor
        if profile_data.department is not None:
            user.professor.department = profile_data.department
        if profile_data.contact_phone is not None:
            user.professor.contact_phone = profile_data.contact_phone

        # Guardar los cambios
        await self.db.commit()
        await self.db.refresh(user)
        await self.db.refresh(user.professor)
        
        # Retornar la combinación de datos actualizados
        return {
            "id": user.professor.id,
            "username": user.username,
            "name": user.name,
            "lastname": user.lastname,
            "email": user.email,
            "department": user.professor.department,
            "contact_phone": user.professor.contact_phone,
            "avatar_url": user.avatar_url,
            "is_active": user.is_active,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }

    async def get_teacher_settings(self, user_id: int) -> dict:
        """
        Obtiene las configuraciones del dashboard del profesor autenticado.

        Args:
            user_id: ID del usuario autenticado.

        Returns:
            Diccionario con las configuraciones del profesor.
        """
        # Buscar las configuraciones del profesor en la base de datos
        stmt = select(TeacherSettings).where(TeacherSettings.user_id == user_id)
        result = await self.db.execute(stmt)
        teacher_settings = result.scalar_one_or_none()
        
        # Valores por defecto
        settings = {
            "theme": "light",  # light o dark
            "notifications_enabled": True,
            "notification_frequency": "instant",  # instant, daily, weekly
            "interface_language": "es"
        }
        
        if teacher_settings:
            settings.update({
                "theme": teacher_settings.theme,
                "notifications_enabled": teacher_settings.notifications_enabled,
                "notification_frequency": teacher_settings.notification_frequency,
                "interface_language": teacher_settings.interface_language
            })
        
        return settings

    async def update_teacher_settings(self, user_id: int, settings_data: TeacherSettingsUpdate) -> dict:
        """
        Actualiza las configuraciones del dashboard del profesor autenticado.

        Args:
            user_id: ID del usuario autenticado.
            settings_data: Datos para la actualización de configuraciones.

        Returns:
            Diccionario con las configuraciones actualizadas.
        """
        # Buscar las configuraciones existentes del profesor
        stmt = select(TeacherSettings).where(TeacherSettings.user_id == user_id)
        result = await self.db.execute(stmt)
        existing_settings = result.scalar_one_or_none()
        
        # Si no existen configuraciones para este usuario, crearlas
        if not existing_settings:
            existing_settings = TeacherSettings(user_id=user_id)
            self.db.add(existing_settings)
        
        # Actualizar las configuraciones con los nuevos valores
        if settings_data.theme is not None:
            existing_settings.theme = settings_data.theme
        if settings_data.notifications_enabled is not None:
            existing_settings.notifications_enabled = settings_data.notifications_enabled
        if settings_data.notification_frequency is not None:
            existing_settings.notification_frequency = settings_data.notification_frequency
        if settings_data.interface_language is not None:
            existing_settings.interface_language = settings_data.interface_language

        # Guardar los cambios
        await self.db.commit()
        await self.db.refresh(existing_settings)
        
        # Retornar las configuraciones actualizadas
        return {
            "theme": existing_settings.theme,
            "notifications_enabled": existing_settings.notifications_enabled,
            "notification_frequency": existing_settings.notification_frequency,
            "interface_language": existing_settings.interface_language
        }