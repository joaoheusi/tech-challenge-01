from abc import ABC, abstractmethod

from src.core.domain.models.product import Product


class ProductsPort(ABC):

    @abstractmethod
    async def get_product_by_id(self, product_id: str) -> Product:
        raise NotImplementedError
