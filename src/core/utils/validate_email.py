import re


async def validate_email(email: str) -> bool:
    email_regex = r"""^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[-a-z0-9]*[a-z0-9])?\.)+[a-z]{2,}$"""  # noqa
    return re.search(email_regex, email.lower()) is not None
