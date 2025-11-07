# from fastapi import APIRouter, Depends
# from src.core.deps import get_current_user
# from src.models.user import User
# from src.schemas.teacher import (
#     TeacherProfileResponseSchema,
#     TeacherProfileUpdate,
#     TeacherSettingsResponseSchema,
#     TeacherSettingsUpdate,
#     TeacherUpdateResponseSchema
# )

# router = APIRouter(prefix='/teacher', tags=["Teacher"])

# # @router.get("/me", response_model=TeacherProfileResponseSchema)
# # async def get_teacher_profile(
# #     current_user: User = Depends(get_current_user)
# # ):
# #     """
# #     Obtener perfil del profesor autenticado
# #     """
# #     # Datos de prueba
# #     mock_profile = {
# #         "id": current_user.id,
# #         "username": current_user.username,
# #         "name": current_user.name,
# #         "lastname": getattr(current_user, 'lastname', 'Teacher'),
# #         "email": current_user.email,
# #         "department": "Matemáticas",
# #         "contact_phone": "+1234567890",
# #         "avatar_url": "https://example.com/avatar.jpg",
# #         "is_active": True,
# #         "created_at": "2023-01-15T10:30:00",
# #         "updated_at": "2023-01-15T10:30:00"
# #     }
    
# #     return TeacherProfileResponseSchema(
# #         success=True,
# #         message="Perfil obtenido exitosamente",
# #         data=mock_profile
# #     )

# # @router.put("/me", response_model=TeacherUpdateResponseSchema)
# # async def update_teacher_profile(
# #     profile_data: TeacherProfileUpdate,
# #     current_user: User = Depends(get_current_user)
# # ):
# #     """
# #     Actualizar perfil
# #     """
# #     # Datos de prueba
# #     mock_updated_profile = {
# #         "id": current_user.id,
# #         "username": current_user.username,
# #         "name": profile_data.name or current_user.name,
# #         "lastname": profile_data.lastname or getattr(current_user, 'lastname', 'Teacher'),
# #         "email": profile_data.email or current_user.email,
# #         "department": profile_data.department or "Matemáticas",
# #         "contact_phone": profile_data.contact_phone or "+1234567890",
# #         "avatar_url": profile_data.avatar_url or "https://example.com/avatar.jpg",
# #         "is_active": True,
# #         "created_at": "2023-01-15T10:30:00",
# #         "updated_at": "2023-01-15T10:30:00"
# #     }
    
# #     return TeacherUpdateResponseSchema(
# #         success=True,
# #         message="Perfil actualizado exitosamente",
# #         data=mock_updated_profile
# #     )

# # @router.get("/settings", response_model=TeacherSettingsResponseSchema)
# # async def get_teacher_settings(
# #     current_user: User = Depends(get_current_user)
# # ):
# #     """
# #     Obtener configuraciones del dashboard
# #     """
# #     # Datos de prueba
# #     mock_settings = {
# #         "theme": "light",
# #         "notifications_enabled": True,
# #         "notification_frequency": "instant",
# #         "interface_language": "es"
# #     }
    
# #     return TeacherSettingsResponseSchema(
# #         success=True,
# #         message="Configuraciones obtenidas exitosamente",
# #         data=mock_settings
# #     )

# # @router.put("/settings", response_model=TeacherSettingsResponseSchema)
# # async def update_teacher_settings(
# #     settings_data: TeacherSettingsUpdate,
# #     current_user: User = Depends(get_current_user)
# # ):
# #     """
# #     Actualizar configuraciones (tema, notificaciones, etc.)
# #     """
# #     # Datos de prueba
# #     mock_updated_settings = {
# #         "theme": settings_data.theme or "light",
# #         "notifications_enabled": settings_data.notifications_enabled if settings_data.notifications_enabled is not None else True,
# #         "notification_frequency": settings_data.notification_frequency or "instant",
# #         "interface_language": settings_data.interface_language or "es"
# #     }
    
# #     return TeacherSettingsResponseSchema(
# #         success=True,
# #         message="Configuraciones actualizadas exitosamente",
# #         data=mock_updated_settings
# #     )