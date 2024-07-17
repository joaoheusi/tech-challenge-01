from abc import ABC, abstractmethod

from src.entities.customer import Customer
from src.types.dtos.create_customer_dto import CreateCustomerDto


class CustomersRepository(ABC):

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
