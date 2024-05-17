from src.adapters.repositories.beanie.documents.product_document import ProductDocument
from src.core.domain.dtos.create_product_dto import CreateProductDto
from src.core.domain.dtos.patch_product_dto import PatchProductDto
from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort


class BeanieProductsRepository(ProductsPort):

    async def find_product_by_id(self, product_id: str) -> Product:
        product = await ProductDocument.find_one(
            ProductDocument.id == product_id
        ).project(Product)
        if not product:
            return None
        return product

    async def find_products(self) -> list[Product]:
        products = await ProductDocument.find().project(Product).to_list()
        return products

    async def create_product(self, product: CreateProductDto) -> Product:
        product_to_create = ProductDocument(**product.model_dump())
        await product_to_create.insert()
        return product_to_create

    async def update_product(
        self, product_id: str, product: PatchProductDto
    ) -> Product:
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
