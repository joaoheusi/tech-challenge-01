from injector import Module, provider, singleton

from src.gateways.providers.fake.fake_payments_provider import FakePaymentProvider
from src.gateways.providers.mercado_pago.mercado_pago_payments_provider import (
    MercadoPagoPaymentsProvider,
)
from src.gateways.repositories.beanie.beanie_customers_repository import (
    BeanieCustomersRepository,
)
from src.gateways.repositories.beanie.beanie_orders_repository import (
    BeanieOrdersRepository,
)
from src.gateways.repositories.beanie.beanie_payments_repository import (
    BeaniePaymentsRepository,
)
from src.gateways.repositories.beanie.beanie_products_repository import (
    BeanieProductsRepository,
)
from src.interfaces.providers.payments_provider import PaymentsProvider
from src.interfaces.repositories.customers_repository import CustomersRepository

# from src.adapters.repositories.fake.fake_products_repository import (
#     FakeProductsRepository,
# )
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.interfaces.repositories.payments_repository import PaymentsRepository
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


class PaymentsProviderModule(Module):
    @singleton
    @provider
    def provide_payment_provider(self) -> PaymentsProvider:
        # To enable MercadoPago payment gateway, uncomment line 56
        # return MercadoPagoPaymentsProvider()
        return FakePaymentProvider()


class PaymentsRepositoryModule(Module):
    @singleton
    @provider
    def provide_payments_repository(self) -> PaymentsRepository:
        return BeaniePaymentsRepository()
