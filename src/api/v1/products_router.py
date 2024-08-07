from typing import Annotated

from fastapi.params import Depends
from fastapi.routing import APIRouter

from src.controllers.products_controller import ProductsUseCasesController
from src.entities.product import Product
from src.types.dtos.create_product_dto import CreateProductDto
from src.types.dtos.get_products_filters_dto import GetProductsFiltersDto
from src.types.dtos.patch_product_dto import PatchProductDto

products_router = APIRouter(prefix="/products", tags=["products"])


@products_router.get("/{product_id}", response_model=Product)
async def get_product_by_id(product_id: str) -> Product | None:
    product = await ProductsUseCasesController.get_product_by_id(product_id)
    return product


@products_router.get("", response_model=list[Product])
async def get_products(
    filters: Annotated[GetProductsFiltersDto, Depends()],
) -> list[Product]:
    print(filters.model_dump())
    products = await ProductsUseCasesController.get_products(filters=filters)
    return products


@products_router.post("", response_model=Product)
async def create_product(product: CreateProductDto) -> Product:
    created_product = await ProductsUseCasesController.create_product(product=product)
    return created_product


@products_router.patch("/{product_id}", response_model=Product)
async def update_product(product_id: str, product: PatchProductDto) -> Product | None:
    updated_product = await ProductsUseCasesController.update_product(
        product_id=product_id, product=product
    )
    return updated_product
