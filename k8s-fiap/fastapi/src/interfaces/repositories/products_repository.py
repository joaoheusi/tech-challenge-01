from abc import ABC, abstractmethod

from src.entities.product import Product
from src.types.dtos.create_product_dto import CreateProductDto
from src.types.dtos.get_products_filters_dto import GetProductsFiltersDto
from src.types.dtos.patch_product_dto import PatchProductDto


class ProductsRepository(ABC):

    @abstractmethod
    async def find_product_by_id(self, product_id: str) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    async def find_product_by_list_of_ids(
        self, product_ids: list[str]
    ) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    async def find_products(
        self, filters: GetProductsFiltersDto | None = None
    ) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    async def create_product(self, product: CreateProductDto) -> Product:
        raise NotImplementedError

    @abstractmethod
    async def update_product(
        self, product_id: str, product: PatchProductDto
    ) -> Product | None:
        raise NotImplementedError
