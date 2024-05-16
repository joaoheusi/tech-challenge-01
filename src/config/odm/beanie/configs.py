from typing import Any

from src.adapters.repositories.beanie.documents.product_document import ProductDocument

MONGODB_URL = "mongodb://localhost:27017"

DOCUMENT_MODELS: list[Any] = [
    ProductDocument,
]
