from injector import inject

from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort
from src.core.excecptions.application_exceptions import ApplicationExceptions


class GetProductUseCase:

    @inject
    def __init__(self, products_repository: ProductsPort):
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
