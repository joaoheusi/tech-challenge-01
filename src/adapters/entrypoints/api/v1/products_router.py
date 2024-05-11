from fastapi.routing import APIRouter

from src.core.application.use_cases.products.controller import (
    ProductsUseCasesController,
)

products_router = APIRouter(prefix="/products")


@products_router.get("/{product_id}")
async def get_product_by_id(product_id: str):
    product = await ProductsUseCasesController.get_products(product_id)
    return product
