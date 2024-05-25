from injector import inject

from src.core.domain.dtos.product.patch_product_dto import PatchProductDto
from src.core.domain.models.product import Product
from src.core.domain.repositories.products_port import ProductsPort
from src.core.excecptions.application_exceptions import ApplicationExceptions


class UpdateProductUseCase:

    @inject
    def __init__(self, products_repository: ProductsPort):
        self.products_repository = products_repository

    async def execute(self, product_id: str, product: PatchProductDto) -> Product:
        updated_product = await self.products_repository.update_product(
            product_id=product_id, product=product
        )
        if not updated_product:
            raise ApplicationExceptions.resource_not_found(
                resource_name="Product",
                identifier=["id"],
                identifier_value=product_id,
            )
        return updated_product
