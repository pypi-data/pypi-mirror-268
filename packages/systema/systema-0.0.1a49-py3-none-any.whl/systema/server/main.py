from contextlib import asynccontextmanager

import trio
from fastapi import FastAPI
from hypercorn.config import Config
from hypercorn.trio import serve as serve_

from systema.__version__ import VERSION
from systema.server.auth.endpoints import router as auth_router
from systema.server.db import create_db_and_tables
from systema.server.project_manager.endpoints.bin import router as bin_router
from systema.server.project_manager.endpoints.card import router as card_router
from systema.server.project_manager.endpoints.event import router as event_router
from systema.server.project_manager.endpoints.item import router as item_router
from systema.server.project_manager.endpoints.project import router as project_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, version=VERSION)

app.include_router(auth_router)
app.include_router(project_router)
app.include_router(item_router)
app.include_router(bin_router)
app.include_router(card_router)
app.include_router(event_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def serve(port: int = 8080, dev: bool = False):
    config = Config()
    config.bind = [f"0.0.0.0:{port}"]
    config.use_reloader = dev

    trio.run(serve_, app, config)
