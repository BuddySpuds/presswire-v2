"""
PressWire v2.0 - FastAPI Application
Built with FastAPI, PydanticAI, and Supabase
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
import os

# Import API routers
from app.api.v1.press_releases import router as pr_router
from app.core.config import get_settings

settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title="PressWire.ie API",
    description="Ireland's Domain-Verified Press Release Platform",
    version="2.0.0",
    docs_url="/api/docs" if settings.app_debug else None,
    redoc_url="/api/redoc" if settings.app_debug else None,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Include API routers
app.include_router(pr_router)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Serve the landing page"""
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/generate", response_class=HTMLResponse)
async def generate_page(request: Request):
    """Serve the press release generation page"""
    return templates.TemplateResponse("generate.html", {"request": request})

@app.get("/success", response_class=HTMLResponse)
async def success_page(request: Request):
    """Serve the success page"""
    return templates.TemplateResponse("success.html", {"request": request})

@app.get("/api")
async def api_root():
    """API root endpoint"""
    return {
        "name": "PressWire.ie API v2",
        "status": "operational",
        "version": "2.0.0",
        "endpoints": {
            "press_releases": "/api/v1/press-releases",
            "docs": "/api/docs" if settings.app_debug else None,
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
