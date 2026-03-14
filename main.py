from fastapi import FastAPI
from api.routes import router

# Initialize FastAPI application
app = FastAPI(
    title="CodeGuard",
    description="Automated Code Review and Bug Detection API",
    version="1.0.0"
)

# Include API routes
app.include_router(router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to CodeGuard - Automated Code Review System"}
