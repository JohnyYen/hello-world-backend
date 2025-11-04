from fastapi import APIRouter

router = APIRouter(prefix="/game-instances", tags=["Game Instances"])

router.get("/")  # Example endpoint
async def list_game_instances():
    return {"message": "List of game instances"}