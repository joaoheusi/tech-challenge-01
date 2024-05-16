from fastapi.routing import APIRouter

from src.core.application.use_cases.products.controller import (
    ProductsUseCasesController,
)
from src.core.domain.dtos.create_product_dto import CreateProductDto
from src.core.domain.dtos.patch_product_dto import PatchProductDto

products_router = APIRouter(prefix="/products")


@products_router.get("/{product_id}")
async def get_product_by_id(product_id: str):
    product = await ProductsUseCasesController.get_product_by_id(product_id)
    return product


@products_router.get("/")
async def get_products():
    products = await ProductsUseCasesController.get_products()
    return products


@products_router.post("/")
async def create_product(product: CreateProductDto):
    product = await ProductsUseCasesController.create_product(product)
    return product


@products_router.patch("/{product_id}")
async def update_product(product_id: str, product: PatchProductDto):
    product = await ProductsUseCasesController.update_product(product_id, product)
    return product
