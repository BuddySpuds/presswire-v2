"""PydanticAI Agent for Press Release Generation and Enhancement"""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic import BaseModel, Field
from typing import Optional, List, Union
from datetime import datetime
from app.core.config import get_settings

settings = get_settings()


class PRContent(BaseModel):
    """Structured output for press release content"""
    headline: str = Field(..., description="Compelling headline (max 100 chars)", max_length=100)
    subheadline: Optional[str] = Field(None, description="Supporting subheadline", max_length=150)
    body: str = Field(..., description="Main press release body with proper formatting")
    boilerplate: str = Field(..., description="Company boilerplate text")

    # SEO Fields
    seo_title: str = Field(..., description="SEO-optimized title (max 60 chars)", max_length=60)
    meta_description: str = Field(..., description="Meta description (max 160 chars)", max_length=160)
    keywords: List[str] = Field(..., description="Relevant keywords for SEO")

    # Suggestions
    suggested_improvements: List[str] = Field(default_factory=list)
    readability_score: float = Field(..., ge=0, le=100)


class PREnhancement(BaseModel):
    """Suggestions for improving existing press release"""
    improved_headline: Optional[str] = None
    improved_body: Optional[str] = None
    seo_suggestions: List[str] = Field(default_factory=list)
    grammar_corrections: List[str] = Field(default_factory=list)
    style_improvements: List[str] = Field(default_factory=list)
    overall_score: float = Field(..., ge=0, le=100)


# Configure the model based on available API keys
def get_ai_model():
    """Get the appropriate AI model based on configuration"""
    if settings.openai_api_key:
        return OpenAIModel(
            "gpt-4o-mini",
            api_key=settings.openai_api_key
        )
    elif settings.openrouter_api_key:
        # OpenRouter uses OpenAI-compatible API
        return OpenAIModel(
            settings.pydantic_ai_model,
            api_key=settings.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1"
        )
    else:
        # Default to Anthropic if available
        return AnthropicModel(
            "claude-3-5-haiku-latest",
            api_key=settings.anthropic_api_key if hasattr(settings, 'anthropic_api_key') else None
        )


# Initialize PR Generation Agent
pr_generator = Agent(
    model=get_ai_model(),
    result_type=PRContent,
    system_prompt="""You are an expert press release writer for Irish businesses.
    Create compelling, newsworthy press releases that follow AP style guidelines.
    Focus on:
    - Clear, impactful headlines
    - Inverted pyramid structure (most important info first)
    - Professional tone suitable for journalists
    - Irish market context and relevance
    - SEO optimization for Irish search terms
    Include relevant Irish media angles where appropriate.
    """
)


# Initialize PR Enhancement Agent
pr_enhancer = Agent(
    model=get_ai_model(),
    result_type=PREnhancement,
    system_prompt="""You are an expert press release editor and SEO specialist.
    Analyze and enhance press releases for Irish businesses to maximize their impact.
    Focus on:
    - Improving headline impact and newsworthiness
    - Ensuring proper press release structure
    - Enhancing SEO for Irish search queries
    - Fixing grammar and style issues
    - Making content more appealing to Irish journalists
    Provide specific, actionable improvements.
    """
)


async def generate_press_release(
    company_name: str,
    announcement: str,
    company_info: str,
    target_audience: str = "Irish media and business community"
) -> PRContent:
    """Generate a complete press release using AI"""

    prompt = f"""
    Company: {company_name}
    Announcement: {announcement}
    Company Info: {company_info}
    Target Audience: {target_audience}

    Create a professional press release following standard format:
    1. Compelling headline
    2. Location and date line
    3. Lead paragraph with who, what, when, where, why
    4. Supporting paragraphs with details and quotes
    5. Company boilerplate
    6. Contact information placeholder

    Optimize for Irish media distribution.
    """

    result = await pr_generator.run(prompt)
    return result.data


async def enhance_press_release(existing_content: str) -> PREnhancement:
    """Enhance an existing press release"""

    prompt = f"""
    Please analyze and enhance this press release:

    {existing_content}

    Provide specific improvements for:
    1. Headline impact
    2. Content structure and flow
    3. SEO optimization for Irish market
    4. Grammar and style
    5. Overall newsworthiness

    Score the content quality from 0-100.
    """

    result = await pr_enhancer.run(prompt)
    return result.data


class SEOMetadata(BaseModel):
    """SEO metadata for press releases"""
    seo_title: str = Field(..., max_length=60)
    meta_description: str = Field(..., max_length=160)
    keywords: List[str] = Field(..., min_items=5, max_items=10)
    og_title: str = Field(...)
    og_description: str = Field(...)
    og_type: str = Field(default="article")
    schema_markup: dict = Field(...)


async def generate_seo_metadata(headline: str, body: str, company: str) -> SEOMetadata:
    """Generate SEO metadata for a press release"""

    seo_agent = Agent(
        model=get_ai_model(),
        result_type=SEOMetadata,
        system_prompt="Generate SEO metadata optimized for Irish search queries and news distribution."
    )

    prompt = f"""
    Headline: {headline}
    Company: {company}
    Content: {body[:500]}...

    Generate comprehensive SEO metadata including:
    - SEO title (max 60 chars)
    - Meta description (max 160 chars)
    - 5-10 relevant keywords for Irish market
    - Open Graph tags
    - Schema.org NewsArticle markup structure
    """

    result = await seo_agent.run(prompt)
    return result.data