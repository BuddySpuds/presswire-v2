"""Mock PR Generator for testing without PydanticAI"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


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


async def generate_press_release(
    company_name: str,
    announcement: str,
    company_info: str,
    target_audience: str = "Irish media and business community"
) -> PRContent:
    """Mock function to generate a press release"""

    return PRContent(
        headline=f"{company_name} Announces {announcement[:50]}...",
        subheadline=f"Leading Irish company makes significant announcement for {target_audience}",
        body=f"""
{company_name} today announced {announcement}

Dublin, Ireland - {datetime.now().strftime('%B %d, %Y')} - {company_name}, {company_info}, today announced {announcement}. This significant development demonstrates the company's commitment to innovation and growth in the Irish market.

"This announcement represents an important milestone for our company," said a spokesperson for {company_name}. "We are excited to share this news with our customers, partners, and the wider Irish business community."

The announcement is expected to have positive implications for {target_audience} and reinforces {company_name}'s position in the market.

About {company_name}:
{company_info}

For more information, please contact:
[Contact information to be added]

###
        """.strip(),
        boilerplate=f"{company_name} is {company_info}",
        seo_title=f"{company_name} News: {announcement[:25]}",
        meta_description=f"{company_name} announces {announcement[:100]}... Learn more about this development.",
        keywords=[
            company_name.lower().replace(" ", "-"),
            "irish business",
            "announcement",
            "news",
            "ireland"
        ],
        suggested_improvements=[
            "Consider adding specific metrics or numbers to strengthen impact",
            "Include a relevant quote from company leadership",
            "Add context about market positioning"
        ],
        readability_score=75.5
    )


async def enhance_press_release(existing_content: str) -> PREnhancement:
    """Mock function to enhance an existing press release"""

    return PREnhancement(
        improved_headline="[Enhanced] " + existing_content.split('\n')[0][:80],
        improved_body=f"Enhanced version:\n\n{existing_content}\n\n[This is a mock enhancement]",
        seo_suggestions=[
            "Add location-specific keywords for Irish market",
            "Include industry-relevant terms",
            "Optimize headline for search engines"
        ],
        grammar_corrections=[
            "Check for proper Irish English spelling",
            "Ensure consistent tense throughout"
        ],
        style_improvements=[
            "Use more active voice",
            "Strengthen the opening paragraph",
            "Add more specific details"
        ],
        overall_score=82.0
    )