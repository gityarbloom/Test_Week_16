from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import *
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    ping_mongodb()
    load_data_to_mongodb()
    yield
    close_connection()

app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8888, host="127.0.0.1", reload=True)