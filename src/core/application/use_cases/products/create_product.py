from injector import inject

from src.core.domain.dtos.create_product_dto import CreateProductDto
from src.core.domain.repositories.products_port import ProductsPort


class CreateProductUseCase:
    @inject
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    async def execute(self, product: CreateProductDto):
        return await self.products_repository.create_product(product)
