from fastapi.routing import APIRouter

from src.adapters.entrypoints.api.v1.index import v1_router

base_router = APIRouter()

base_router.include_router(v1_router)
