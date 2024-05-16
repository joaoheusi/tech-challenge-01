from abc import ABC, abstractmethod

from core.domain.dtos.create_product_dto import CreateProductDto
from core.domain.dtos.patch_product_dto import PatchProductDto
from src.core.domain.models.product import Product


class ProductsPort(ABC):

    @abstractmethod
    async def find_product_by_id(self, product_id: str) -> Product:
        raise NotImplementedError

    @abstractmethod
    async def find_products(self) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    async def create_product(self, product: CreateProductDto) -> Product:
        raise NotImplementedError

    @abstractmethod
    async def update_product(
        self, product_id: str, product: PatchProductDto
    ) -> Product:
        raise NotImplementedError
