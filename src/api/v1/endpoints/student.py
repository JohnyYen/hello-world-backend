from fastapi import APIRouter, Depends, Query
from src.core.deps import get_current_user
from src.models.user import User
from src.schemas.student import (
    StudentListResponse,
    StudentResponse,
    StudentCreate,
    StudentUpdate,
    StudentProgressResponse,
    StudentReportsResponse
)

router = APIRouter(prefix='/students', tags=["Students"])

@router.get("/", response_model=StudentListResponse)
async def list_students(
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número de registros a devolver"),
    search: str = Query(None, description="Búsqueda por nombre o email"),
    active: bool = Query(None, description="Filtrar por estado activo")
):
    """
    Listar estudiantes (con filtros y paginación)
    """
    # Datos de prueba
    mock_students = [
        {
            "id": 1,
            "username": "juanperez",
            "email": "juan.perez@example.com",
            "name": "Juan",
            "lastname": "Pérez",
            "is_active": True,
            "created_at": "2023-01-15T10:30:00",
            "updated_at": "2023-01-15T10:30:00"
        },
        {
            "id": 2,
            "username": "anagarcia",
            "email": "ana.garcia@example.com",
            "name": "Ana",
            "lastname": "García",
            "is_active": True,
            "created_at": "2023-01-16T11:45:00",
            "updated_at": "2023-01-16T11:45:00"
        }
    ]
    
    return StudentListResponse(
        success=True,
        message="Estudiantes listados exitosamente",
        data=mock_students
    )

@router.get("/{id}", response_model=StudentResponse)
async def get_student(
    id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Obtener detalle de un estudiante
    """
    # Datos de prueba
    mock_student = {
        "id": id,
        "username": f"student{id}",
        "email": f"student{id}@example.com",
        "name": f"Nombre{id}",
        "lastname": f"Apellido{id}",
        "is_active": True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return StudentResponse(
        success=True,
        message="Estudiante obtenido exitosamente",
        data=mock_student
    )

@router.post("/", response_model=StudentResponse)
async def create_student(
    student_data: StudentCreate,
    current_user: User = Depends(get_current_user)
):
    """
    Registrar un nuevo estudiante
    """
    # Datos de prueba
    mock_student = {
        "id": 999,  # ID simulado para el nuevo estudiante
        "username": student_data.username,
        "email": student_data.email,
        "name": student_data.name,
        "lastname": student_data.lastname,
        "is_active": student_data.is_active,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return StudentResponse(
        success=True,
        message="Estudiante creado exitosamente",
        data=mock_student
    )

@router.put("/{id}", response_model=StudentResponse)
async def update_student(
    id: int,
    student_data: StudentUpdate,
    current_user: User = Depends(get_current_user)
):
    """
    Actualizar información del estudiante
    """
    # Datos de prueba
    mock_student = {
        "id": id,
        "username": student_data.username or f"student{id}",
        "email": student_data.email or f"student{id}@example.com",
        "name": student_data.name or f"Nombre{id}",
        "lastname": student_data.lastname or f"Apellido{id}",
        "is_active": student_data.is_active if student_data.is_active is not None else True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return StudentResponse(
        success=True,
        message="Estudiante actualizado exitosamente",
        data=mock_student
    )

@router.delete("/{id}")
async def delete_student(
    id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Eliminar estudiante
    """
    # Simulación de eliminación
    return {"success": True, "message": f"Estudiante con ID {id} eliminado exitosamente"}

@router.get("/{id}/progress", response_model=StudentProgressResponse)
async def get_student_progress(
    id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Obtener progreso del estudiante
    """
    # Datos de prueba
    mock_progress = {
        "student_id": id,
        "completed_levels": 5,
        "total_levels": 10,
        "completion_percentage": 50.0,
        "current_level": "Nivel 6",
        "last_activity": "2023-01-20T14:30:00",
        "total_time_spent": "4h 30m"
    }
    
    return StudentProgressResponse(
        success=True,
        message="Progreso del estudiante obtenido exitosamente",
        data=mock_progress
    )

@router.get("/{id}/reports", response_model=StudentReportsResponse)
async def get_student_reports(
    id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Obtener reportes individuales (desempeño, actividad, etc.)
    """
    # Datos de prueba
    mock_reports = {
        "student_id": id,
        "performance_report": {
            "average_score": 85.5,
            "completed_assignments": 12,
            "passed_assignments": 10,
            "failed_assignments": 2
        },
        "activity_report": {
            "total_sessions": 25,
            "total_time_spent": "20h 45m",
            "last_login": "2023-01-20T14:30:00"
        },
        "engagement_report": {
            "participation_rate": 78.3,
            "completed_activities": 45,
            "total_activities": 58
        }
    }
    
    return StudentReportsResponse(
        success=True,
        message="Reportes del estudiante obtenidos exitosamente",
        data=mock_reports
    )