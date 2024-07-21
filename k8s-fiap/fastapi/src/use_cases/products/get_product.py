from injector import inject

from src.entities.product import Product
from src.excecptions.application_exceptions import ApplicationExceptions
from src.interfaces.repositories.products_repository import ProductsRepository


class GetProductUseCase:

    @inject
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    async def execute(self, product_id: str) -> Product:
        product = await self.products_repository.find_product_by_id(
            product_id=product_id
        )
        if not product:
            raise ApplicationExceptions.resource_not_found(
                resource_name="Product",
                identifier=["id"],
                identifier_value=product_id,
            )
        return product
