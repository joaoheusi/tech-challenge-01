from datetime import datetime

from pydantic import BaseModel


class CreateCustomerDto(BaseModel):
    firstName: str
    lastName: str
    email: str
    cpf: str
    birthDate: datetime | None = None
    phoneNumber: str | None = None
