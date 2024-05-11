from src.config.injector.container import container
from src.core.application.use_cases.products.get_product import (  # noqa
    GetProductUseCase,
)
from src.core.domain.models.product import Product


class ProductsUseCasesController:

    async def get_products(product_id: str) -> Product | None:
        get_product_use_case = container.get(GetProductUseCase)
        product = await get_product_use_case.execute(product_id)
        return product
