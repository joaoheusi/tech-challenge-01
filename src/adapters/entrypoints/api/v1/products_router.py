from fastapi.routing import APIRouter

from src.core.application.use_cases.products.controller import (
    ProductsUseCasesController,
)
from src.core.domain.dtos.product.create_product_dto import CreateProductDto
from src.core.domain.dtos.product.patch_product_dto import PatchProductDto
from src.core.domain.models.product import Product

products_router = APIRouter(prefix="/products", tags=["products"])


@products_router.get("/{product_id}", response_model=Product)
async def get_product_by_id(product_id: str) -> Product | None:
    product = await ProductsUseCasesController.get_product_by_id(product_id)
    return product


@products_router.get("/", response_model=list[Product])
async def get_products() -> list[Product]:
    products = await ProductsUseCasesController.get_products()
    return products


@products_router.post("/", response_model=Product)
async def create_product(product: CreateProductDto) -> Product:
    created_product = await ProductsUseCasesController.create_product(product=product)
    return created_product


@products_router.patch("/{product_id}", response_model=Product)
async def update_product(product_id: str, product: PatchProductDto) -> Product | None:
    updated_product = await ProductsUseCasesController.update_product(
        product_id=product_id, product=product
    )
    return updated_product
