from fastapi.routing import APIRouter

from src.api.v1.customers_router import customers_router
from src.api.v1.notifications_router import notifications_router
from src.api.v1.orders_router import orders_router
from src.api.v1.payments_router import payments_router
from src.api.v1.products_router import products_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(products_router)
v1_router.include_router(customers_router)
v1_router.include_router(orders_router)
v1_router.include_router(notifications_router)
v1_router.include_router(payments_router)
