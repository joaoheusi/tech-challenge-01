from injector import Injector

from src.config.injector.modules import (
    CustomersRepositoryModule,
    OrdersRepositoryModule,
    ProductsRepositoryModule,
)

container = Injector(
    [
        ProductsRepositoryModule,
        CustomersRepositoryModule,
        OrdersRepositoryModule,
    ]
)
