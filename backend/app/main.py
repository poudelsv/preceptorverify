from fastapi import FastAPI

from app.api.v1.endpoints import health
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title="PreceptorVerify API",
    description = "Backend API for centralized medical license verification platform.",
    version="0.1.0"
)

app.include_router(health.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to PreceptorVerify API",
        "status": "running",
        "environment": settings.environment
    }