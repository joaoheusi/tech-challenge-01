from injector import inject

from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort


class GetProductsUseCase:
    @inject
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    async def execute(self) -> list[Product]:
        return await self.products_repository.find_products()
