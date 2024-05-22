from src.core.domain.dtos.product.create_product_dto import CreateProductDto
from src.core.domain.dtos.product.patch_product_dto import PatchProductDto
from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort


class FakeProductsRepository(ProductsPort):
    _products: list[Product] = []

    async def find_product_by_id(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.id == product_id:
                return product

        return None

    async def find_products(self) -> list[Product]:
        return self._products

    async def create_product(self, product: CreateProductDto) -> Product:
        product_to_create = Product(**product.model_dump())
        self._products.append(
            product_to_create,
        )
        return product_to_create

    async def update_product(
        self, product_id: str, patched_product: PatchProductDto
    ) -> Product | None:
        for _, product in enumerate(self._products):
            if product.id == product_id:
                for key, value in patched_product.model_dump().items():
                    if value is not None:
                        setattr(product, key, value)
                return product
        return None
