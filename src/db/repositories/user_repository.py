# app/db/repositories/user_repository.py
from typing import Optional, List, Dict, Any
from datetime import datetime
from sqlalchemy import select, update, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from src.core.security import get_password_hash, verify_password
from src.core.exceptions import (
    NotFoundException,
    DuplicateEntryException,
    InvalidCredentialsException
)
from .base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repositorio para operaciones de base de datos relacionadas con usuarios.
    
    Hereda del BaseRepository y provee métodos CRUD con validaciones y manejo de errores específicos.
    También incluye métodos adicionales específicos para la autenticación de usuarios.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, User)

    async def get_by_email(self, email: str, include_deleted: bool = False) -> Optional[User]:
        """Busca un usuario por email.
        
        Args:
            email: Email del usuario a buscar
            include_deleted: Si True, incluye usuarios marcados como eliminados
            
        Returns:
            User: Instancia del modelo User si se encuentra, None en caso contrario
        """
        filters = {"email": email}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)

    async def get_by_username(self, username: str, include_deleted: bool = False) -> Optional[User]:
        """Busca un usuario por nombre de usuario.
        
        Args:
            username: Nombre de usuario a buscar
            include_deleted: Si True, incluye usuarios marcados como eliminados
            
        Returns:
            User: Instancia del modelo User si se encuentra, None en caso contrario
        """
        filters = {"username": username}
        return await self.get_one_by_filters(filters, include_deleted=include_deleted)

    async def create(self, user_data: UserCreate) -> User:
        """Crea un nuevo usuario en la base de datos.
        
        Args:
            user_data: Datos validados para la creación del usuario
            
        Returns:
            User: Instancia del nuevo usuario creado
            
        Raises:
            DuplicateEntryException: Si el email o username ya existen
        """
        # Verifica unicidad de email y username antes de crear
        existing_email = await self.get_by_email(user_data.email)
        if existing_email:
            raise DuplicateEntryException("El email ya está registrado")
            
        if user_data.username:
            existing_username = await self.get_by_username(user_data.username)
            if existing_username:
                raise DuplicateEntryException("El nombre de usuario ya está en uso")

        # Preparar datos para la creación, incluyendo la contraseña hash
        user_dict = user_data.model_dump()
        user_dict['hashed_password'] = get_password_hash(user_data.password)
        # Remover la contraseña original del diccionario
        user_dict.pop('password', None)
        
        # Crear el usuario usando el método del BaseRepository
        return await super().create(user_dict)

    async def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Actualiza un usuario existente.
        
        Solo actualiza los campos que no son None en user_data.
        Verifica unicidad de email y username si son proporcionados.
        
        Args:
            user_id: ID del usuario a actualizar
            user_data: Datos validados para la actualización
            
        Returns:
            User: Instancia del usuario actualizado, None si no se encuentra
            
        Raises:
            DuplicateEntryException: Si el nuevo email o username ya existen
        """
        # Obtener datos no nulos para actualizar
        update_data = user_data.model_dump(exclude_unset=True)
        
        if not update_data:
            return await self.get_by_id(user_id)
            
        # Verificar unicidad si se actualiza email o username
        if 'email' in update_data:
            # Verificar si el email ya existe para otro usuario
            existing_user = await self.get_by_email(update_data['email'])
            if existing_user and existing_user.id != user_id:
                raise DuplicateEntryException("El nuevo email ya está registrado")
                
        if 'username' in update_data and update_data['username'] is not None:
            # Verificar si el username ya existe para otro usuario
            existing_user = await self.get_by_username(update_data['username'])
            if existing_user and existing_user.id != user_id:
                raise DuplicateEntryException("El nuevo nombre de usuario ya está en uso")
        
        # Actualizar contraseña si se proporciona
        if 'password' in update_data:
            update_data['hashed_password'] = get_password_hash(update_data.pop('password'))
        # Si se proporciona password pero no se actualiza, remover del update
        elif 'password' in update_data:
            update_data.pop('password', None)
        
        # Usar el método del BaseRepository para actualizar
        return await super().update(user_id, update_data)

    async def authenticate(self, email: str, password: str) -> Optional[User]:
        """Autentica un usuario verificando email y contraseña.
        
        Args:
            email: Email del usuario
            password: Contraseña en texto plano
            
        Returns:
            User: Instancia del usuario si las credenciales son válidas, None en caso contrario
            
        Raises:
            InvalidCredentialsException: Si las credenciales son inválidas
        """
        user = await self.get_by_email(email, include_deleted=True)
        if not user or user.is_deleted:
            raise InvalidCredentialsException("Credenciales inválidas")
            
        if not verify_password(password, user.hashed_password):
            raise InvalidCredentialsException("Credenciales inválidas")
            
        return user