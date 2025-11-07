from fastapi import APIRouter
from typing import List
from src.schemas.feedback import FeedbackCreate, FeedbackSchema
import datetime

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.post("/", response_model=FeedbackSchema)
async def submit_feedback(
    feedback: FeedbackCreate
):
    """
    Enviar retroalimentación de un estudiante.
    """
    # Datos de prueba
    mock_new_feedback = {
        "id": 2001,
        "student_id": feedback.student_id,
        "message": feedback.message,
        "rating": feedback.rating if feedback.rating else 5,
        "created_at": datetime.datetime.now(),
        "updated_at": None
    }
    
    return mock_new_feedback


@router.get("/{student_id}", response_model=List[FeedbackSchema])
async def get_student_feedback_history(
    student_id: int
):
    """
    Obtener feedback histórico del estudiante.
    """
    # Datos de prueba
    mock_feedback_list = [
        {
            "id": 1,
            "student_id": student_id,
            "message": "La plataforma es muy útil para aprender a programar",
            "rating": 5,
            "created_at": datetime.datetime.now() - datetime.timedelta(days=7),
            "updated_at": None
        },
        {
            "id": 2,
            "student_id": student_id,
            "message": "Me gustaría más ejercicios interactivos",
            "rating": 4,
            "created_at": datetime.datetime.now() - datetime.timedelta(days=3),
            "updated_at": None
        },
        {
            "id": 3,
            "student_id": student_id,
            "message": "Excelente soporte para principiantes",
            "rating": 5,
            "created_at": datetime.datetime.now() - datetime.timedelta(days=1),
            "updated_at": None
        }
    ]
    
    return mock_feedback_list
