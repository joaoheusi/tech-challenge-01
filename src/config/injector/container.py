from injector import Injector

from src.config.injector.modules import (
    CustomersRepositoryModule,
    ProductsRepositoryModule,
)

container = Injector(
    [
        ProductsRepositoryModule,
        CustomersRepositoryModule,
    ]
)
