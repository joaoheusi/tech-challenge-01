from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from src.adapters.entrypoints.api.base_router import base_router
from src.config.odm.beanie.configs import DOCUMENT_MODELS, MONGODB_URL


async def start_beanie() -> None:
    print("Starting beanie")
    database = AsyncIOMotorClient(MONGODB_URL).fiap
    await init_beanie(database=database, document_models=DOCUMENT_MODELS)
    print("Finished starting beanie")


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    await start_beanie()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(base_router)


@app.get("/ping")
def ping():
    return {"ping": "pong."}
