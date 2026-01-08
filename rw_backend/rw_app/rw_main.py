from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .rw_config import settings
from .rw_routes_generate import router as generate_router

app = FastAPI(title=settings.app_name)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(generate_router, prefix=settings.api_prefix)

@app.get("/")
async def root():
    return {"message": "ReelWriter AI backend is running"}
