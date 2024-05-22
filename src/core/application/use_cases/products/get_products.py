from injector import inject

from src.core.domain.dtos.product.get_products_filters_dto import GetProductsFiltersDto
from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort


class GetProductsUseCase:
    @inject
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    async def execute(
        self, filters: GetProductsFiltersDto | None = None
    ) -> list[Product]:
        return await self.products_repository.find_products(filters=filters)
