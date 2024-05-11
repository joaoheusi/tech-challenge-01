from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort


class FakeProductsRepository(ProductsPort):
    _products: list[Product] = []

    async def get_product_by_id(self, product_id: str) -> Product:

        for product in self._products:
            if product.id == product_id:
                return product

        return None
