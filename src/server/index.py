from fastapi import FastAPI

from src.adapters.entrypoints.api.index import base_router

app = FastAPI()


app.include_router(base_router)


@app.get("/")
def read_root():

    return {"Olá": "Luciano e Sabrina"}
