from fastapi.routing import APIRouter

from src.adapters.entrypoints.api.v1.products_router import products_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(products_router)