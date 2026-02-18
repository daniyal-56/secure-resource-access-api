from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, resource, access_request 
from app.routes import auth, resources, access

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Resource Access API",
    description="Backend API for managing temporary protected resource access",
    version="1.0.0"
)
app.include_router(auth.router)
app.include_router(resources.router)
app.include_router(access.router)

@app.get("/", tags=["Health Check"])
def health_check():
    """
    Simple endpoint to verify the server is running.
    """
    return {
        "status": "online",
        "message": "Secure Resource Access API is operational",
        "docs": "/docs"
    }