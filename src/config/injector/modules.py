from injector import Module, provider, singleton

from src.adapters.repositories.beanie.beanie_products_repository import (
    BeanieProductsRepository,
)

# from src.adapters.repositories.fake.fake_products_repository import (
#     FakeProductsRepository,
# )

from src.core.domain.repositories.products_port import ProductsPort


class ProductsRepositoryModule(Module):
    @singleton
    @provider
    def provide_products_repository(self) -> ProductsPort:
        return BeanieProductsRepository()
