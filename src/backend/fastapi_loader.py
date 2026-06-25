from fastapi import FastAPI
from routers import tracker

app = FastAPI()

app.include_router(tracker.router)