# src/main.py
from fastapi import FastAPI
from app.routes import attachment

app = FastAPI(title="Azure File Server API")

app.include_router(attachment.router)
