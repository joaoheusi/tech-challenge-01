FROM python:3.11

RUN apt-get update && apt-get install -y \
    gcc \
    unixodbc-dev \
    gpg \
    vim \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /code

COPY ./pyproject.toml /code/
COPY ./poetry.lock /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 80
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]ddd
CMD ["uvicorn", "src.index:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
