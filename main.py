from fastapi import FastAPI
from src.database.db import init_db

app = FastAPI()


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}
