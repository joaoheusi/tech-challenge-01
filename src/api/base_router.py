from fastapi.routing import APIRouter

from src.api.v1.v1_router import v1_router

base_router = APIRouter()

base_router.include_router(v1_router)
