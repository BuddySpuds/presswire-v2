"""Press Release API endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from pydantic import BaseModel, EmailStr

from app.core.database import get_db
from app.agents.pr_generator_mock import (
    generate_press_release,
    enhance_press_release,
    PRContent,
    PREnhancement
)

router = APIRouter(prefix="/api/v1/press-releases", tags=["Press Releases"])


class GeneratePRRequest(BaseModel):
    company_name: str
    announcement: str
    company_info: str
    contact_email: EmailStr
    target_audience: Optional[str] = "Irish media and business community"


class EnhancePRRequest(BaseModel):
    content: str


@router.post("/generate", response_model=PRContent)
async def generate_pr(
    request: GeneratePRRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate a new press release using AI"""
    try:
        pr_content = await generate_press_release(
            company_name=request.company_name,
            announcement=request.announcement,
            company_info=request.company_info,
            target_audience=request.target_audience
        )
        return pr_content
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating press release: {str(e)}"
        )


@router.post("/enhance", response_model=PREnhancement)
async def enhance_pr(
    request: EnhancePRRequest,
    db: AsyncSession = Depends(get_db)
):
    """Enhance an existing press release"""
    try:
        enhancement = await enhance_press_release(request.content)
        return enhancement
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error enhancing press release: {str(e)}"
        )


@router.get("/")
async def list_press_releases(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db)
):
    """List published press releases"""
    # TODO: Implement database query
    return {
        "total": 0,
        "items": [],
        "skip": skip,
        "limit": limit
    }


@router.get("/{pr_id}")
async def get_press_release(
    pr_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific press release"""
    # TODO: Implement database query
    return {
        "id": pr_id,
        "message": "Press release retrieval not yet implemented"
    }