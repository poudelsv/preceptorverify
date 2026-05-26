from fastapi import FastAPI

app = FastAPI(
    title="PreceptorVerify API",
    description = "Backend API for centralized medical license verification platform.",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to PreceptorVerify API",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "PreceptorVerify API"
    }