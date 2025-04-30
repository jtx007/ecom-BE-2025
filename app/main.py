from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.models import user
from app.api.v1 import auth, users

# Create database tables
user.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TBA API",
    description="Backend API built with FastAPI, SQLAlchemy, and PostgreSQL",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1") 