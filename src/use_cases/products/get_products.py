from injector import inject

from src.entities.product import Product
from src.interfaces.repositories.products_repository import ProductsRepository
from src.types.dtos.get_products_filters_dto import GetProductsFiltersDto


class GetProductsUseCase:
    @inject
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    async def execute(
        self, filters: GetProductsFiltersDto | None = None
    ) -> list[Product]:
        return await self.products_repository.find_products(filters=filters)
