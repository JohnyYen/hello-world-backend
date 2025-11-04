# app/services/level_service.py
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_db
from src.db.repositories.level_repository import LevelRepository
from src.schemas.level import LevelCreate, LevelUpdate
from src.models.level import Level
from src.core.exceptions import NotFoundException


class LevelService:
    """
    Servicio para gestionar la lógica de negocio de niveles.

    Proporciona una capa de abstracción sobre el repositorio de niveles,
    manejando la lógica de negocio antes de interactuar con la base de datos.
    """

    def __init__(self, db: AsyncSession = Depends(get_db)):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de base de datos asíncrona.
        """
        self.level_repo = LevelRepository(db)

    async def get_level_by_id(self, level_id: int) -> Optional[Level]:
        """
        Obtiene un nivel por su ID.

        Args:
            level_id: ID del nivel a buscar.

        Returns:
            El nivel si se encuentra, de lo contrario None.
        """
        return await self.level_repo.get_by_id(level_id)

    async def get_all_levels(self, skip: int = 0, limit: int = 100) -> List[Level]:
        """
        Obtiene una lista de todos los niveles con paginación.

        Args:
            skip: Número de registros a saltar.
            limit: Número máximo de registros a devolver.

        Returns:
            Una lista de niveles.
        """
        return await self.level_repo.get_all(skip=skip, limit=limit)

    async def create_level(self, level_data: LevelCreate) -> Level:
        """
        Crea un nuevo nivel.

        Args:
            level_data: Datos para la creación del nivel.

        Returns:
            El nivel recién creado.
        """
        return await self.level_repo.create(level_data.model_dump())

    async def update_level(self, level_id: int, level_data: LevelUpdate) -> Optional[Level]:
        """
        Actualiza un nivel existente.

        Args:
            level_id: ID del nivel a actualizar.
            level_data: Datos para la actualización.

        Returns:
            El nivel actualizado si se encuentra, de lo contrario None.
        
        Raises:
            NotFoundException: Si el nivel no se encuentra.
        """
        level = await self.level_repo.update(level_id, level_data.model_dump(exclude_unset=True))
        if not level:
            raise NotFoundException("Nivel no encontrado")
        return level

    async def delete_level(self, level_id: int) -> bool:
        """
        Elimina (soft delete) un nivel.

        Args:
            level_id: ID del nivel a eliminar.

        Returns:
            True si el nivel fue eliminado, False en caso contrario.
        
        Raises:
            NotFoundException: Si el nivel no se encuentra.
        """
        success = await self.level_repo.delete(level_id)
        if not success:
            raise NotFoundException("Nivel no encontrado")
        return success

    async def get_levels_by_game_id(self, game_id: int) -> List[Level]:
        """
        Obtiene niveles por ID de juego.

        Args:
            game_id: ID del juego.

        Returns:
            Una lista de niveles.
        """
        return await self.level_repo.get_by_game_id(game_id)

    async def get_level_by_level_number(self, game_id: int, level_number: int) -> Optional[Level]:
        """
        Obtiene un nivel por ID de juego y número de nivel.

        Args:
            game_id: ID del juego.
            level_number: Número del nivel.

        Returns:
            El nivel si se encuentra, de lo contrario None.
        """
        return await self.level_repo.get_by_level_number(game_id, level_number)

    async def get_level_by_name(self, name: str) -> Optional[Level]:
        """
        Obtiene un nivel por nombre.

        Args:
            name: Nombre del nivel.

        Returns:
            El nivel si se encuentra, de lo contrario None.
        """
        return await self.level_repo.get_by_name(name)