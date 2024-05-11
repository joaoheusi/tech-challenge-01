from injector import Injector

from src.config.injector.modules import ProductsRepositoryModule

container = Injector(
    [
        ProductsRepositoryModule,
    ]
)
