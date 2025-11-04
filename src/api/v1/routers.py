from fastapi import APIRouter
from src.api.v1.endpoints import user, auth, lms_credential, student, professor, sync_event, sync_session, progress, segment_level, level, game, game_instance, metric_type, feedback

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users")
api_router.include_router(auth.router)
api_router.include_router(lms_credential.router)
api_router.include_router(student.router)
api_router.include_router(professor.router)
api_router.include_router(sync_event.router)
api_router.include_router(sync_session.router)
api_router.include_router(progress.router)
api_router.include_router(segment_level.router)
api_router.include_router(level.router)
api_router.include_router(game.router)
api_router.include_router(game_instance.router)
api_router.include_router(metric_type.router)
api_router.include_router(feedback.router)
