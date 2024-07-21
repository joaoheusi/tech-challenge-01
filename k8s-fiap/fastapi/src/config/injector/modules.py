from injector import Module, provider, singleton

from src.gateways.repositories.beanie.beanie_customers_repository import (
    BeanieCustomersRepository,
)
from src.gateways.repositories.beanie.beanie_orders_repository import (
    BeanieOrdersRepository,
)
from src.gateways.repositories.beanie.beanie_products_repository import (
    BeanieProductsRepository,
)
from src.interfaces.repositories.customers_repository import CustomersRepository

# from src.adapters.repositories.fake.fake_products_repository import (
#     FakeProductsRepository,
# )
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.interfaces.repositories.products_repository import ProductsRepository


class ProductsRepositoryModule(Module):
    @singleton
    @provider
    def provide_products_repository(self) -> ProductsRepository:
        return BeanieProductsRepository()


class CustomersRepositoryModule(Module):
    @singleton
    @provider
    def provide_customers_repository(self) -> CustomersRepository:
        return BeanieCustomersRepository()


class OrdersRepositoryModule(Module):
    @singleton
    @provider
    def provide_orders_repository(self) -> OrdersRepository:
        return BeanieOrdersRepository()
