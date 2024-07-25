from injector import Injector

from src.config.injector.modules import (
    CustomersRepositoryModule,
    OrdersRepositoryModule,
    PaymentsProviderModule,
    PaymentsRepositoryModule,
    ProductsRepositoryModule,
)

container = Injector(
    [
        PaymentsProviderModule,
        ProductsRepositoryModule,
        CustomersRepositoryModule,
        OrdersRepositoryModule,
        PaymentsRepositoryModule,
    ]
)
