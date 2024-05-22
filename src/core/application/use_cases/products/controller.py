from src.config.injector.container import container
from src.core.application.use_cases.products.create_product import CreateProductUseCase
from src.core.application.use_cases.products.get_product import (  # noqa
    GetProductUseCase,
)
from src.core.application.use_cases.products.get_products import GetProductsUseCase
from src.core.application.use_cases.products.update_product import UpdateProductUseCase
from src.core.domain.dtos.product.create_product_dto import CreateProductDto
from src.core.domain.dtos.product.get_products_filters_dto import GetProductsFiltersDto
from src.core.domain.dtos.product.patch_product_dto import PatchProductDto
from src.core.domain.models.product import Product


class ProductsUseCasesController:
    @staticmethod
    async def get_product_by_id(product_id: str) -> Product | None:
        get_product_use_case = container.get(GetProductUseCase)
        product = await get_product_use_case.execute(product_id=product_id)
        return product

    @staticmethod
    async def get_products(filters: GetProductsFiltersDto) -> list[Product]:
        get_products_use_case = container.get(GetProductsUseCase)
        product = await get_products_use_case.execute(filters=filters)
        return product

    @staticmethod
    async def create_product(product: CreateProductDto) -> Product:
        create_product_use_case = container.get(CreateProductUseCase)
        created_product = await create_product_use_case.execute(product=product)
        return created_product

    @staticmethod
    async def update_product(
        product_id: str, product: PatchProductDto
    ) -> Product | None:
        update_product_use_case = container.get(UpdateProductUseCase)
        updated_product = await update_product_use_case.execute(
            product_id=product_id, product=product
        )
        return updated_product
