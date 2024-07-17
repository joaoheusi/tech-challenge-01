from injector import inject

from src.entities.product import Product
from src.excecptions.application_exceptions import ApplicationExceptions
from src.interfaces.repositories.products_repository import ProductsRepository
from src.types.dtos.patch_product_dto import PatchProductDto


class UpdateProductUseCase:

    @inject
    def __init__(self, products_repository: ProductsRepository):
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
