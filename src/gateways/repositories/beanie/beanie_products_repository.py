from beanie.operators import In

from src.entities.product import Product
from src.gateways.repositories.beanie.documents.product_document import ProductDocument
from src.interfaces.repositories.products_repository import ProductsRepository
from src.types.dtos.create_product_dto import CreateProductDto
from src.types.dtos.get_products_filters_dto import GetProductsFiltersDto
from src.types.dtos.patch_product_dto import PatchProductDto


class BeanieProductsRepository(ProductsRepository):

    async def find_product_by_id(self, product_id: str) -> Product | None:
        product = await ProductDocument.find_one(
            ProductDocument.id == product_id
        ).project(Product)
        if not product:
            return None
        return product

    async def find_product_by_list_of_ids(
        self, product_ids: list[str]
    ) -> list[Product]:
        products = (
            await ProductDocument.find(
                In(ProductDocument.id, product_ids),  # type: ignore
            )
            .project(Product)
            .to_list()
        )
        return products

    async def find_products(
        self, filters: GetProductsFiltersDto | None = None
    ) -> list[Product]:
        search_filters = []
        if filters is not None:
            if filters.category is not None:
                search_filters.append(ProductDocument.category == filters.category)
            if filters.isActive is not None:
                search_filters.append(ProductDocument.isActive == filters.isActive)
            if filters.onlyInStock is not None and filters.onlyInStock is True:
                search_filters.append(ProductDocument.availableAmount > 0)
        products = (
            await ProductDocument.find(*search_filters).project(Product).to_list()
        )
        return products

    async def create_product(self, product: CreateProductDto) -> Product:
        product_to_create = ProductDocument(**product.model_dump())
        await product_to_create.insert()
        return product_to_create

    async def update_product(
        self, product_id: str, product: PatchProductDto
    ) -> Product | None:
        product_exists = await ProductDocument.find_one(
            ProductDocument.id == product_id
        )
        if not product_exists:
            return None

        for key, value in product.model_dump().items():
            if value is not None:
                setattr(product_exists, key, value)

        await product_exists.save_changes()
        return product_exists
