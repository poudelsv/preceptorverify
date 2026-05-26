from fastapi import FastAPI

from app.api.v1.endpoints import health

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
        "status": "running"
    }