from src.adapters.repositories.beanie.documents.product_document import ProductDocument
from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort


class BeanieProductsRepository(ProductsPort):

    async def get_product_by_id(self, product_id: str) -> Product:
        product = await ProductDocument.find_one(
            ProductDocument.id == product_id
        ).project(Product)
        if not product:
            return None
        return product
