from injector import Module, provider, singleton

from src.adapters.repositories.beanie.beanie_customers_repository import (
    BeanieCustomersRepository,
)
from src.adapters.repositories.beanie.beanie_orders_repository import (
    BeanieOrdersRepository,
)
from src.adapters.repositories.beanie.beanie_products_repository import (
    BeanieProductsRepository,
)
from src.core.domain.repositories.customers_port import CustomersPort

# from src.adapters.repositories.fake.fake_products_repository import (
#     FakeProductsRepository,
# )
from src.core.domain.repositories.orders_port import OrdersPort
from src.core.domain.repositories.products_port import ProductsPort


class ProductsRepositoryModule(Module):
    @singleton
    @provider
    def provide_products_repository(self) -> ProductsPort:
        return BeanieProductsRepository()


class CustomersRepositoryModule(Module):
    @singleton
    @provider
    def provide_customers_repository(self) -> CustomersPort:
        return BeanieCustomersRepository()


class OrdersRepositoryModule(Module):
    @singleton
    @provider
    def provide_orders_repository(self) -> OrdersPort:
        return BeanieOrdersRepository()
