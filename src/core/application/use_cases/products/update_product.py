from injector import inject

from src.core.domain.repositories.products_port import ProductsPort


class UpdateProductUseCase:

    @inject
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    async def execute(self, product_id: str, product: dict):
        return await self.products_repository.update_product(product_id, product)
