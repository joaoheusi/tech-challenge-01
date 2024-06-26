from typing import Any

from src.adapters.repositories.beanie.documents.customer_document import (
    CustomerDocument,
)
from src.adapters.repositories.beanie.documents.order_document import OrderDocument
from src.adapters.repositories.beanie.documents.product_document import ProductDocument

MONGODB_URL_DOCKER = "mongodb://mongo:27017"

DOCUMENT_MODELS: list[Any] = [
    ProductDocument,
    CustomerDocument,
    OrderDocument,
]
