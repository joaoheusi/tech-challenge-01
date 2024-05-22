from abc import ABC, abstractmethod

from src.core.domain.dtos.customer.create_customer_dto import CreateCustomerDto
from src.core.domain.models.customer import Customer


class CustomersPort(ABC):

    @abstractmethod
    async def find_customer_by_id(self, customer_id: str) -> Customer | None:
        raise NotImplementedError

    @abstractmethod
    async def find_customer_by_email(self, email: str) -> Customer | None:
        raise NotImplementedError

    @abstractmethod
    async def find_customer_by_cpf(self, cpf: str) -> Customer | None:
        raise NotImplementedError

    @abstractmethod
    async def create_customer(self, customer: CreateCustomerDto) -> Customer:
        raise NotImplementedError
