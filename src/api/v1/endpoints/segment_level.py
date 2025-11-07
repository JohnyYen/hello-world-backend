from fastapi import APIRouter, Depends, Query
from src.core.deps import get_current_user
from src.models.user import User
from src.schemas.segment_level import SegmentLevelCreate, SegmentLevelUpdate, SegmentLevel as SegmentLevelSchema

router = APIRouter(prefix="/segments", tags=["Segments"])

@router.get("/{level_id}/segments", response_model=list[SegmentLevelSchema])
async def get_level_segments(
    level_id: int,
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número de registros a devolver")
):
    """
    Lista los segmentos de un nivel.
    """
    # Datos de prueba
    mock_segments = [
        {
            "id": 1,
            "level_id": level_id,
            "name": "Segmento 1: Conceptos básicos",
            "description": "Introducción a los conceptos básicos del nivel",
            "config": {"type": "instruction", "duration": 300},
            "order": 1,
            "is_active": True,
            "created_at": "2023-01-15T10:30:00",
            "updated_at": "2023-01-15T10:30:00"
        },
        {
            "id": 2,
            "level_id": level_id,
            "name": "Segmento 2: Ejercicio práctico",
            "description": "Ejercicio práctico para aplicar conceptos",
            "config": {"type": "exercise", "complexity": "easy", "expected_time": 600},
            "order": 2,
            "is_active": True,
            "created_at": "2023-01-16T11:45:00",
            "updated_at": "2023-01-16T11:45:00"
        },
        {
            "id": 3,
            "level_id": level_id,
            "name": "Segmento 3: Evaluación",
            "description": "Evaluación para verificar comprensión",
            "config": {"type": "evaluation", "questions": 5, "passing_score": 80},
            "order": 3,
            "is_active": True,
            "created_at": "2023-01-17T09:30:00",
            "updated_at": "2023-01-17T09:30:00"
        }
    ]
    
    # Aplicar paginación
    start = skip
    end = skip + limit
    paginated_segments = mock_segments[start:end]
    
    return paginated_segments

@router.post("/{level_id}/segments", response_model=SegmentLevelSchema)
async def create_level_segment(
    level_id: int,
    segment: SegmentLevelCreate,
    current_user: User = Depends(get_current_user)
):
    """
    Agrega un segmento a un nivel.
    """
    # Datos de prueba
    mock_new_segment = {
        "id": 999,  # ID simulado para el nuevo segmento
        "level_id": level_id,
        "name": segment.name,
        "description": segment.description or f"Descripción para {segment.name}",
        "config": segment.config or {"type": "default", "properties": {}},
        "order": segment.order or 1,
        "is_active": segment.is_active if segment.is_active is not None else True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T10:30:00"
    }
    
    return mock_new_segment

@router.put("/{segment_id}", response_model=SegmentLevelSchema)
async def update_segment(
    segment_id: int,
    segment: SegmentLevelUpdate,
    current_user: User = Depends(get_current_user)
):
    """
    Actualiza configuración JSON del segmento.
    """
    # Datos de prueba
    mock_updated_segment = {
        "id": segment_id,
        "level_id": 1,  # Valor simulado
        "name": segment.name or f"Segmento {segment_id}",
        "description": segment.description or f"Descripción del segmento {segment_id}",
        "config": segment.config or {"type": "default", "properties": {}},
        "order": segment.order or 1,
        "is_active": segment.is_active if segment.is_active is not None else True,
        "created_at": "2023-01-15T10:30:00",
        "updated_at": "2023-01-15T15:45:00"  # Fecha actualizada
    }
    
    return mock_updated_segment

@router.delete("/{segment_id}")
async def delete_segment(
    segment_id: int,
    current_user: User = Depends(get_current_user)
):
    """
    Elimina un segmento.
    """
    # Simulación de eliminación
    return {"message": f"Segmento con ID {segment_id} eliminado exitosamente"}