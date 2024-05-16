from injector import inject

from src.core.domain.repositories.products_port import ProductsPort


class GetProductUseCase:

    @inject
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    async def execute(self, product_id: str):
        return await self.products_repository.find_product_by_id(product_id)
