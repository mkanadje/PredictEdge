from fastapi import FastAPI
from backend.app.api import ingest

app = FastAPI()

app.include_router(ingest.router)
