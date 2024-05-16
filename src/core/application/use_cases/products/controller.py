from src.config.injector.container import container
from src.core.application.use_cases.products.create_product import CreateProductUseCase
from src.core.application.use_cases.products.get_product import (  # noqa
    GetProductUseCase,
)
from src.core.application.use_cases.products.get_products import GetProductsUseCase
from src.core.application.use_cases.products.update_product import UpdateProductUseCase
from src.core.domain.models.product import Product


class ProductsUseCasesController:
    @staticmethod
    async def get_product_by_id(product_id: str) -> Product | None:
        get_product_use_case = container.get(GetProductUseCase)
        product = await get_product_use_case.execute(product_id)
        return product

    @staticmethod
    async def get_products() -> list[Product]:
        get_products_use_case = container.get(GetProductsUseCase)
        product = await get_products_use_case.execute()
        return product

    @staticmethod
    async def create_product(product: dict) -> Product:
        create_product_use_case = container.get(CreateProductUseCase)
        product = await create_product_use_case.execute(product)
        return product

    @staticmethod
    async def update_product(product_id: str, product: dict) -> Product:
        update_product_use_case = container.get(UpdateProductUseCase)
        product = await update_product_use_case.execute(product_id, product)
        return product
