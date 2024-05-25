from injector import inject

from src.core.domain.dtos.customer.create_customer_dto import CreateCustomerDto
from src.core.domain.models.customer import Customer
from src.core.domain.repositories.customers_port import CustomersPort
from src.core.excecptions.application_exceptions import ApplicationExceptions


class CreateCustomerUseCase:

    @inject
    def __init__(self, customers_repository: CustomersPort):
        self.customers_repository = customers_repository

    async def execute(self, customer: CreateCustomerDto) -> Customer:

        existing_customer_with_email = (
            await self.customers_repository.find_customer_by_email(email=customer.email)
        )

        if existing_customer_with_email:
            raise ApplicationExceptions.resource_already_exists(
                resource_name="Customer",
                identifier=["email"],
                identifier_value=customer.email,
            )

        existing_customer_with_cpf = (
            await self.customers_repository.find_customer_by_cpf(cpf=customer.cpf)
        )
        if existing_customer_with_cpf:
            raise ApplicationExceptions.resource_already_exists(
                resource_name="Customer",
                identifier=["cpf"],
                identifier_value=customer.cpf,
            )

        return await self.customers_repository.create_customer(customer)
