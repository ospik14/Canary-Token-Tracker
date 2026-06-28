from fastapi import FastAPI
from backend.routers import tracker

app = FastAPI()

app.include_router(tracker.router)