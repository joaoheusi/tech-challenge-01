from src.core.domain.dtos.product.create_product_dto import CreateProductDto
from src.core.domain.dtos.product.get_products_filters_dto import GetProductsFiltersDto
from src.core.domain.dtos.product.patch_product_dto import PatchProductDto
from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsRepository


class FakeProductsRepository(ProductsRepository):
    _products: list[Product] = []

    async def find_product_by_id(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.id == product_id:
                return product

        return None

    async def find_product_by_list_of_ids(
        self, product_ids: list[str]
    ) -> list[Product]:
        return [product for product in self._products if product.id in product_ids]

    async def find_products(
        self, filters: GetProductsFiltersDto | None = None
    ) -> list[Product]:
        result = self._products
        if filters is not None:
            if filters.category is not None:
                result = [
                    product
                    for product in result
                    if product.category == filters.category
                ]
            if filters.isActive is not None:
                result = [
                    product
                    for product in result
                    if product.isActive == filters.isActive
                ]
            if filters.onlyInStock is not None and filters.onlyInStock is True:
                result = [product for product in result if product.availableAmount > 0]

        return result

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
