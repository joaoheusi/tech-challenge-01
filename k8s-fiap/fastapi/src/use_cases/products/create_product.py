from injector import inject

from src.entities.product import Product
from src.interfaces.repositories.products_repository import ProductsRepository
from src.types.dtos.create_product_dto import CreateProductDto


class CreateProductUseCase:
    @inject
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    async def execute(self, product: CreateProductDto) -> Product:
        return await self.products_repository.create_product(product)
