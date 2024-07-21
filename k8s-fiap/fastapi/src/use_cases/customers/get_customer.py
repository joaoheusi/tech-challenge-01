from injector import inject

from src.entities.customer import Customer
from src.excecptions.application_exceptions import ApplicationExceptions
from src.interfaces.repositories.customers_repository import CustomersRepository


class GetCustomerUseCase:

    @inject
    def __init__(self, customers_repository: CustomersRepository):
        self.customers_repository = customers_repository

    async def execute(self, identifier: str) -> Customer:
        customer_found_by_id = await self.customers_repository.find_customer_by_id(
            customer_id=identifier
        )

        customer_found_by_cpf = await self.customers_repository.find_customer_by_cpf(
            cpf=identifier
        )

        customer_found_by_email = (
            await self.customers_repository.find_customer_by_email(email=identifier)
        )

        if customer_found_by_id:
            return customer_found_by_id

        if customer_found_by_cpf:
            return customer_found_by_cpf

        if customer_found_by_email:
            return customer_found_by_email

        raise ApplicationExceptions.resource_not_found(
            resource_name="Customer",
            identifier=["id", "cpf", "email"],
            identifier_value=identifier,
        )
