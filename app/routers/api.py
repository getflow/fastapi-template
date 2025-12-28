from fastapi import APIRouter

from app.schemas.hello import Hello

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/hello")
async def hello() -> Hello:
    return Hello()
