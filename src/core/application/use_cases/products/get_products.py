from injector import inject

from src.core.domain.repositories.products_port import ProductsPort


class GetProductsUseCase:
    @inject
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    async def execute(self):
        return await self.products_repository.find_products()
