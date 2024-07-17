from datetime import datetime

from pydantic import BaseModel, field_validator

from src.utils.validate_cpf import validate_cpf
from src.utils.validate_email import validate_email


class CreateCustomerDto(BaseModel):
    firstName: str
    lastName: str
    email: str
    cpf: str
    birthDate: datetime | None = None
    phoneNumber: str | None = None

    @field_validator("cpf")
    def validate_input_cpf(cls, cpf: str) -> str:
        if validate_cpf(cpf) is not True:
            raise ValueError("Invalid CPF.")
        formatted_cpf = cpf.replace(".", "").replace("-", "")
        return formatted_cpf

    @field_validator("email")
    def validate_input_email(cls, email: str) -> str:
        if validate_email(email) is not True:
            raise ValueError("Invalid Email.")

        return email
