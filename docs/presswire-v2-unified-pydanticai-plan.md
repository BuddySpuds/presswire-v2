# PressWire.ie v2.0 - Unified Implementation with PydanticAI

## Executive Summary

A complete ground-up rebuild using FastAPI, PydanticAI, and Supabase that combines the best of both v1.1 and v2.0 proposals. This creates a modern, type-safe, AI-powered press release platform with hybrid static/dynamic architecture for perfect SEO while eliminating GitHub storage and constant rebuilds.

**Stack:** FastAPI + PydanticAI + Supabase + Digital Ocean
**Timeline:** 1 week development + 1 week deployment
**Cost:** €12-15/month total
**Result:** Private code, no rebuilds, perfect SEO, professional architecture

---

## 🎯 Core Architecture

```
┌─────────────────────────────────────────────┐
│         FastAPI + PydanticAI Core           │
│                                              │
│  • Type-safe with Pydantic V2               │
│  • AI agents for PR generation              │
│  • Async/await throughout                   │
│  • OpenAPI documentation                    │
└──────────────────┬──────────────────────────┘
                   │
         ┌─────────▼─────────┐
         │   Three Layers    │
         ├───────────────────┤
         │ 1. Static HTML     │ ← SEO Perfect
         │ 2. Database Meta  │ ← Searchable
         │ 3. AI Agents      │ ← Intelligent
         └─────────┬─────────┘
                   │
    ┌──────────────┴──────────────┐
    │                              │
┌───▼─────┐              ┌────────▼────────┐
│Supabase │              │  Digital Ocean  │
│Database │              │   Object Store  │
│         │              │  (Static HTML)  │
└─────────┘              └─────────────────┘
```

---

## 📁 Project Structure

```
presswire-v2/
├── app/
│   ├── __init__.py
│   ├── main.py                     # FastAPI application
│   ├── config.py                   # Settings with Pydantic
│   ├── database.py                 # Supabase client
│   │
│   ├── models/                     # Pydantic Models (Type Safety)
│   │   ├── __init__.py
│   │   ├── base.py                # Base model configurations
│   │   ├── press_release.py       # PR models with validation
│   │   ├── user.py                # User models
│   │   ├── payment.py             # Payment models
│   │   └── analytics.py           # Analytics models
│   │
│   ├── agents/                     # PydanticAI Agents
│   │   ├── __init__.py
│   │   ├── pr_agent.py            # PR generation & enhancement
│   │   ├── seo_agent.py           # SEO optimization
│   │   ├── category_agent.py      # Auto-categorization
│   │   ├── validation_agent.py    # Content validation
│   │   └── analytics_agent.py     # Analytics insights
│   │
│   ├── schemas/                    # Request/Response schemas
│   │   ├── __init__.py
│   │   ├── requests.py            # API request models
│   │   ├── responses.py           # API response models
│   │   └── webhooks.py            # Webhook payloads
│   │
│   ├── api/                        # API Routes
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py           # Authentication endpoints
│   │   │   ├── press_releases.py  # PR CRUD operations
│   │   │   ├── payments.py       # Stripe integration
│   │   │   ├── analytics.py      # Analytics endpoints
│   │   │   ├── search.py         # Search & filter
│   │   │   └── public.py         # Public PR viewing
│   │   └── v2/                   # Future API version
│   │
│   ├── core/                      # Core business logic
│   │   ├── __init__.py
│   │   ├── security.py           # Auth & JWT
│   │   ├── dependencies.py       # FastAPI dependencies
│   │   ├── exceptions.py         # Custom exceptions
│   │   └── middleware.py         # Custom middleware
│   │
│   ├── services/                  # External services
│   │   ├── __init__.py
│   │   ├── supabase_service.py  # Database operations
│   │   ├── stripe_service.py    # Payment processing
│   │   ├── resend_service.py    # Email delivery
│   │   ├── cro_service.py       # CRO validation
│   │   ├── static_generator.py  # Static HTML generation
│   │   └── storage_service.py   # DO Spaces/S3 storage
│   │
│   ├── workers/                   # Background tasks
│   │   ├── __init__.py
│   │   ├── email_worker.py      # Async email sending
│   │   ├── analytics_worker.py  # Analytics processing
│   │   └── static_worker.py     # Static file generation
│   │
│   ├── templates/                 # Jinja2 templates
│   │   ├── base.html
│   │   ├── landing.html
│   │   ├── pr_template.html     # Static PR template
│   │   ├── dashboard.html
│   │   └── emails/
│   │       ├── verification.html
│   │       └── notification.html
│   │
│   └── static/                    # Static assets
│       ├── css/
│       │   └── output.css        # Tailwind compiled
│       ├── js/
│       │   └── app.js
│       └── images/
│
├── migrations/                    # Database migrations
│   ├── 001_initial_schema.sql
│   ├── 002_add_search_index.sql
│   └── 003_add_analytics.sql
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── test_models.py
│   ├── test_agents.py
│   ├── test_api.py
│   └── test_services.py
│
├── scripts/
│   ├── migrate_from_v1.py       # Data migration
│   ├── generate_static_all.py   # Bulk static generation
│   └── setup_supabase.py        # Database setup
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .dockerignore
│
├── deploy/
│   ├── digitalocean/
│   │   ├── app.yaml             # DO App Platform
│   │   └── deploy.sh
│   └── nginx/
│       └── nginx.conf
│
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml               # Modern Python packaging
├── README.md
└── LICENSE
```

---

## 🚀 Phase 1: Core Setup (Day 1)

### 1.1 Initialize Project

```bash
# Create new project
mkdir presswire-v2 && cd presswire-v2
git init

# Setup Python environment
python3.11 -m venv venv
source venv/bin/activate

# Install core dependencies
pip install fastapi uvicorn pydantic pydantic-settings pydantic-ai
pip install supabase sqlalchemy asyncpg
pip install stripe resend httpx
pip install jinja2 python-multipart
pip install redis celery
pip install pytest pytest-asyncio black ruff
```

### 1.2 Configuration with Pydantic Settings

```python
# app/config.py
from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional
from functools import lru_cache

class AppSettings(BaseSettings):
    """Application settings with validation"""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    # Application
    app_name: str = "PressWire.ie"
    app_version: str = "2.0.0"
    debug: bool = False
    environment: str = Field(default="development", pattern="^(development|staging|production)$")

    # API
    api_v1_prefix: str = "/api/v1"
    api_v2_prefix: str = "/api/v2"

    # Security
    secret_key: SecretStr
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Database
    supabase_url: str
    supabase_anon_key: SecretStr
    supabase_service_key: SecretStr

    # Storage
    storage_backend: str = Field(default="local", pattern="^(local|s3|do_spaces)$")
    do_spaces_key: Optional[SecretStr] = None
    do_spaces_secret: Optional[SecretStr] = None
    do_spaces_bucket: Optional[str] = None

    # Stripe
    stripe_secret_key: SecretStr
    stripe_publishable_key: str
    stripe_webhook_secret: SecretStr

    # Email
    resend_api_key: SecretStr
    from_email: str = "noreply@presswire.ie"
    support_email: str = "support@presswire.ie"

    # AI Configuration
    openrouter_api_key: SecretStr
    ai_model: str = "google/gemini-2.0-flash:free"
    ai_temperature: float = 0.7
    ai_max_tokens: int = 2000

    # CRO API
    cro_api_url: str = "https://services.cro.ie/api/v1"
    cro_api_timeout: int = 5

    # Redis
    redis_url: str = "redis://localhost:6379"
    cache_ttl: int = 300

    # Rate Limiting
    rate_limit_requests: int = 100
    rate_limit_period: int = 60

    # CORS
    allowed_origins: List[str] = ["http://localhost:3000", "https://presswire.ie"]

    # Features
    enable_analytics: bool = True
    enable_ai_enhancement: bool = True
    enable_static_generation: bool = True

    class Config:
        validate_assignment = True

@lru_cache()
def get_settings() -> AppSettings:
    """Get cached settings instance"""
    return AppSettings()

settings = get_settings()
```

### 1.3 Pydantic Models with Full Validation

```python
# app/models/press_release.py
from pydantic import BaseModel, Field, validator, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum
import uuid

class PRPackage(str, Enum):
    """PR Package tiers"""
    BASIC = "basic"
    PROFESSIONAL = "professional"
    PREMIUM = "premium"

    @property
    def price(self) -> int:
        return {"basic": 99, "professional": 199, "premium": 399}[self.value]

class PRStatus(str, Enum):
    """PR Status"""
    DRAFT = "draft"
    PUBLISHED = "published"
    UNPUBLISHED = "unpublished"
    ARCHIVED = "archived"

class PRCategory(str, Enum):
    """PR Categories"""
    PRODUCT_LAUNCH = "Product Launch"
    FUNDING = "Funding"
    PARTNERSHIP = "Partnership"
    AWARD = "Award"
    EXPANSION = "Expansion"
    COMPANY_NEWS = "Company News"

class PressReleaseBase(BaseModel):
    """Base PR model with validation"""
    headline: str = Field(..., min_length=10, max_length=200)
    summary: str = Field(..., min_length=50, max_length=500)
    content: str = Field(..., min_length=200, max_length=5000)
    company_name: str = Field(..., min_length=2, max_length=100)
    cro_number: str = Field(..., pattern="^[0-9]{6}$")
    contact_email: str = Field(..., pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$")
    contact_phone: Optional[str] = Field(None, pattern="^[+]?[0-9]{7,15}$")

    @validator('headline')
    def validate_headline(cls, v):
        if not v[0].isupper():
            raise ValueError('Headline must start with capital letter')
        return v.strip()

    @validator('cro_number')
    def validate_cro(cls, v):
        # Could add actual CRO API validation here
        return v

class PressReleaseCreate(PressReleaseBase):
    """PR creation model"""
    package: PRPackage
    key_points: List[str] = Field(..., min_items=3, max_items=5)
    company_website: Optional[HttpUrl] = None

    @validator('key_points')
    def validate_key_points(cls, v):
        for point in v:
            if len(point) < 10 or len(point) > 100:
                raise ValueError('Key points must be 10-100 characters')
        return v

class PressReleaseDB(PressReleaseBase):
    """PR database model"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    user_id: Optional[uuid.UUID] = None
    slug: str
    status: PRStatus = PRStatus.PUBLISHED
    package: PRPackage
    categories: List[PRCategory] = []
    keywords: List[str] = []

    # Metadata
    views: int = 0
    unique_visitors: int = 0
    shares: int = 0

    # AI Enhancement
    ai_enhanced: bool = False
    ai_confidence_score: Optional[float] = None

    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    published_at: Optional[datetime] = None

    # URLs
    static_url: Optional[str] = None
    management_token: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            uuid.UUID: lambda v: str(v)
        }

class PressReleaseResponse(BaseModel):
    """PR API response model"""
    id: str
    headline: str
    summary: str
    company_name: str
    slug: str
    url: str
    status: PRStatus
    categories: List[str]
    published_at: datetime
    views: int

    class Config:
        orm_mode = True
```

---

## 🤖 Phase 2: PydanticAI Agents (Day 2)

### 2.1 PR Generation Agent

```python
# app/agents/pr_agent.py
from pydantic_ai import Agent, ModelRetry
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import json

class PREnhancement(BaseModel):
    """AI-enhanced PR content"""
    headline: str = Field(..., description="SEO-optimized headline")
    summary: str = Field(..., description="Compelling summary")
    content: str = Field(..., description="Full PR content with HTML formatting")
    keywords: List[str] = Field(..., description="SEO keywords")
    categories: List[str] = Field(..., description="Auto-detected categories")
    confidence_score: float = Field(..., ge=0, le=1)

class PRGenerationAgent:
    """Agent for PR generation and enhancement"""

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        self.agent = Agent(
            model=model,
            api_key=api_key,
            system_prompt=self._get_system_prompt()
        )

    def _get_system_prompt(self) -> str:
        return """
        You are an expert press release writer for Irish businesses.
        Your task is to enhance press releases to be:
        1. SEO-optimized for Irish market
        2. Professionally written
        3. Newsworthy and engaging
        4. Compliant with Irish media standards
        5. Include relevant Irish context (mention Ireland, Dublin, EU where relevant)

        Focus on:
        - Clear, compelling headlines
        - Strong opening paragraphs
        - Quotable statements
        - Irish market relevance
        - Professional tone

        Output must be valid JSON with specified fields.
        """

    async def enhance_pr(self, pr_data: Dict[str, Any]) -> PREnhancement:
        """Enhance a press release with AI"""

        prompt = f"""
        Enhance this press release for {pr_data['company_name']} (CRO: {pr_data['cro_number']}):

        Original Headline: {pr_data['headline']}
        Summary: {pr_data['summary']}
        Key Points: {pr_data.get('key_points', [])}

        Create a professional press release with:
        1. SEO-optimized headline (max 70 chars)
        2. Compelling summary (max 160 chars)
        3. Full content (3-5 paragraphs)
        4. 5-7 relevant keywords
        5. 1-3 categories from: Product Launch, Funding, Partnership, Award, Expansion, Company News

        Make it newsworthy and relevant to Irish market.
        """

        try:
            result = await self.agent.run(prompt, result_type=PREnhancement)
            return result.data
        except ModelRetry as e:
            # Handle retries
            print(f"Retrying due to: {e}")
            raise

    async def generate_metadata(self, pr_content: str) -> Dict[str, Any]:
        """Extract metadata from PR content"""

        prompt = f"""
        Analyze this press release and extract:
        1. Main topics/themes
        2. Target audience
        3. Geographic relevance
        4. Industry sector
        5. News value score (1-10)

        Content: {pr_content[:1000]}
        """

        result = await self.agent.run(prompt)
        return result.data
```

### 2.2 SEO Optimization Agent

```python
# app/agents/seo_agent.py
from pydantic_ai import Agent
from pydantic import BaseModel, Field
from typing import List, Dict

class SEOAnalysis(BaseModel):
    """SEO analysis results"""
    title_tag: str = Field(..., max_length=60)
    meta_description: str = Field(..., max_length=160)
    keywords: List[str] = Field(..., max_items=10)
    h1_tag: str
    h2_tags: List[str]
    slug_suggestion: str
    readability_score: float
    seo_score: int = Field(..., ge=0, le=100)
    improvements: List[str]

class SEOAgent:
    """Agent for SEO optimization"""

    def __init__(self, api_key: str):
        self.agent = Agent(
            model="gemini-2.0-flash",
            api_key=api_key,
            system_prompt="""
            You are an SEO expert specializing in press releases.
            Optimize content for Irish search market and Google News.
            Focus on local SEO signals and Irish search patterns.
            """
        )

    async def optimize_for_seo(self, pr_data: Dict) -> SEOAnalysis:
        """Optimize PR for SEO"""

        prompt = f"""
        Optimize this press release for SEO:

        Headline: {pr_data['headline']}
        Content: {pr_data['content'][:500]}
        Company: {pr_data['company_name']}

        Provide:
        1. SEO-optimized title tag
        2. Meta description
        3. Target keywords for Irish market
        4. URL slug
        5. Content structure recommendations
        """

        result = await self.agent.run(prompt, result_type=SEOAnalysis)
        return result.data

    async def generate_schema_markup(self, pr_data: Dict) -> Dict:
        """Generate Schema.org markup"""

        return {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": pr_data['headline'],
            "description": pr_data['summary'],
            "datePublished": pr_data['published_at'],
            "author": {
                "@type": "Organization",
                "name": pr_data['company_name'],
                "identifier": f"CRO: {pr_data['cro_number']}"
            },
            "publisher": {
                "@type": "Organization",
                "name": "PressWire.ie",
                "url": "https://presswire.ie"
            }
        }
```

---

## 💾 Phase 3: Database & Services (Day 3)

### 3.1 Supabase Integration

```python
# app/services/supabase_service.py
from supabase import create_client, Client
from typing import Optional, List, Dict, Any
from app.config import settings
from app.models.press_release import PressReleaseDB, PressReleaseCreate
import uuid

class SupabaseService:
    """Supabase database service"""

    def __init__(self):
        self.client: Client = create_client(
            settings.supabase_url,
            settings.supabase_service_key.get_secret_value()
        )

    async def create_pr(self, pr: PressReleaseCreate, user_id: Optional[str] = None) -> PressReleaseDB:
        """Create a press release"""

        pr_data = pr.dict()
        pr_data['id'] = str(uuid.uuid4())
        pr_data['user_id'] = user_id
        pr_data['slug'] = self._generate_slug(pr.headline, pr.cro_number)

        result = self.client.table('press_releases').insert(pr_data).execute()
        return PressReleaseDB(**result.data[0])

    async def get_pr_by_slug(self, slug: str) -> Optional[PressReleaseDB]:
        """Get PR by slug"""

        result = self.client.table('press_releases')\
            .select('*')\
            .eq('slug', slug)\
            .single()\
            .execute()

        return PressReleaseDB(**result.data) if result.data else None

    async def search_prs(
        self,
        query: Optional[str] = None,
        company: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 10,
        offset: int = 0
    ) -> List[PressReleaseDB]:
        """Search press releases"""

        q = self.client.table('press_releases').select('*')

        if query:
            q = q.text_search('headline', query)
        if company:
            q = q.eq('company_name', company)
        if category:
            q = q.contains('categories', [category])

        result = q.order('created_at', desc=True)\
            .limit(limit)\
            .offset(offset)\
            .execute()

        return [PressReleaseDB(**item) for item in result.data]

    async def increment_views(self, pr_id: str, unique: bool = False):
        """Increment PR view count"""

        field = 'unique_visitors' if unique else 'views'

        self.client.rpc('increment', {
            'table_name': 'press_releases',
            'row_id': pr_id,
            'column_name': field
        }).execute()

    def _generate_slug(self, headline: str, cro: str) -> str:
        """Generate SEO-friendly slug"""

        slug_base = headline.lower()\
            .replace(' ', '-')\
            .replace('[^a-z0-9-]', '')\
            [:60]

        return f"{slug_base}-{cro}"
```

### 3.2 Static HTML Generation Service

```python
# app/services/static_generator.py
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from typing import Dict, Any
import boto3
from app.config import settings
from app.models.press_release import PressReleaseDB
import asyncio

class StaticGeneratorService:
    """Generate and store static HTML files"""

    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader('app/templates'),
            autoescape=True
        )
        self.template = self.env.get_template('pr_template.html')

        # Storage backend
        if settings.storage_backend == "do_spaces":
            self.s3 = boto3.client(
                's3',
                endpoint_url='https://nyc3.digitaloceanspaces.com',
                aws_access_key_id=settings.do_spaces_key.get_secret_value(),
                aws_secret_access_key=settings.do_spaces_secret.get_secret_value()
            )

    async def generate_static_html(self, pr: PressReleaseDB) -> str:
        """Generate static HTML for PR"""

        # Render template with all PR data
        html_content = self.template.render(
            pr=pr,
            schema_json=self._generate_schema(pr),
            keywords=', '.join(pr.keywords),
            categories=pr.categories
        )

        # Save to storage
        filename = f"{pr.slug}.html"

        if settings.storage_backend == "local":
            await self._save_local(filename, html_content)
        elif settings.storage_backend == "do_spaces":
            await self._save_to_spaces(filename, html_content)

        return f"/news/{filename}"

    async def _save_local(self, filename: str, content: str):
        """Save to local filesystem"""

        filepath = Path(f"static/news/{filename}")
        filepath.parent.mkdir(parents=True, exist_ok=True)

        await asyncio.to_thread(filepath.write_text, content, encoding='utf-8')

    async def _save_to_spaces(self, filename: str, content: str):
        """Save to Digital Ocean Spaces"""

        self.s3.put_object(
            Bucket=settings.do_spaces_bucket,
            Key=f"news/{filename}",
            Body=content.encode('utf-8'),
            ContentType='text/html',
            ACL='public-read',
            CacheControl='public, max-age=31536000'
        )

    def _generate_schema(self, pr: PressReleaseDB) -> str:
        """Generate Schema.org JSON-LD"""

        import json
        schema = {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": pr.headline,
            "description": pr.summary,
            "datePublished": pr.published_at.isoformat() if pr.published_at else None,
            "author": {
                "@type": "Organization",
                "name": pr.company_name
            }
        }
        return json.dumps(schema, indent=2)
```

---

## 🚦 Phase 4: API Endpoints (Day 4)

### 4.1 PR Generation Endpoint

```python
# app/api/v1/press_releases.py
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from typing import List, Optional
from app.models.press_release import PressReleaseCreate, PressReleaseResponse
from app.services.supabase_service import SupabaseService
from app.services.static_generator import StaticGeneratorService
from app.agents.pr_agent import PRGenerationAgent
from app.agents.seo_agent import SEOAgent
from app.core.dependencies import get_current_user
from app.core.security import verify_domain
from app.config import settings

router = APIRouter()

@router.post("/generate", response_model=PressReleaseResponse)
async def generate_press_release(
    pr_data: PressReleaseCreate,
    background_tasks: BackgroundTasks,
    user = Depends(get_current_user),
    db: SupabaseService = Depends(),
    pr_agent: PRGenerationAgent = Depends(),
    seo_agent: SEOAgent = Depends(),
    static_gen: StaticGeneratorService = Depends()
):
    """Generate a new press release with AI enhancement"""

    # 1. Verify domain ownership
    if not await verify_domain(pr_data.contact_email, pr_data.company_name):
        raise HTTPException(400, "Domain verification failed")

    # 2. Enhance with AI
    enhanced = await pr_agent.enhance_pr(pr_data.dict())

    # 3. SEO optimization
    seo_data = await seo_agent.optimize_for_seo(enhanced.dict())

    # 4. Save to database
    pr_db = await db.create_pr(
        pr_data,
        user_id=user.id if user else None
    )

    # 5. Generate static HTML (async in background)
    background_tasks.add_task(
        static_gen.generate_static_html,
        pr_db
    )

    # 6. Send email notification (async)
    background_tasks.add_task(
        send_pr_notification,
        pr_data.contact_email,
        pr_db.slug
    )

    return PressReleaseResponse(
        id=str(pr_db.id),
        headline=pr_db.headline,
        summary=pr_db.summary,
        company_name=pr_db.company_name,
        slug=pr_db.slug,
        url=f"https://presswire.ie/news/{pr_db.slug}",
        status=pr_db.status,
        categories=pr_db.categories,
        published_at=pr_db.published_at,
        views=pr_db.views
    )

@router.get("/search", response_model=List[PressReleaseResponse])
async def search_press_releases(
    q: Optional[str] = None,
    company: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    db: SupabaseService = Depends()
):
    """Search press releases"""

    results = await db.search_prs(
        query=q,
        company=company,
        category=category,
        limit=limit,
        offset=offset
    )

    return [
        PressReleaseResponse(
            id=str(pr.id),
            headline=pr.headline,
            summary=pr.summary,
            company_name=pr.company_name,
            slug=pr.slug,
            url=f"https://presswire.ie/news/{pr.slug}",
            status=pr.status,
            categories=pr.categories,
            published_at=pr.published_at,
            views=pr.views
        ) for pr in results
    ]

@router.get("/{slug}", response_model=PressReleaseResponse)
async def get_press_release(
    slug: str,
    db: SupabaseService = Depends()
):
    """Get a press release by slug"""

    pr = await db.get_pr_by_slug(slug)

    if not pr:
        raise HTTPException(404, "Press release not found")

    # Increment view count
    await db.increment_views(str(pr.id))

    return PressReleaseResponse(
        id=str(pr.id),
        headline=pr.headline,
        summary=pr.summary,
        company_name=pr.company_name,
        slug=pr.slug,
        url=f"https://presswire.ie/news/{pr.slug}",
        status=pr.status,
        categories=pr.categories,
        published_at=pr.published_at,
        views=pr.views + 1
    )
```

---

## 🚀 Phase 5: Deployment (Day 5)

### 5.1 Docker Configuration

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create static directories
RUN mkdir -p static/news

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### 5.2 Digital Ocean App Platform

```yaml
# deploy/digitalocean/app.yaml
name: presswire-v2
region: lon1

services:
  - name: api
    github:
      repo: your-private-repo/presswire-v2
      branch: main
      deploy_on_push: true

    dockerfile_path: Dockerfile
    http_port: 8080

    instance_size_slug: professional-xs  # $12/month
    instance_count: 1

    routes:
      - path: /

    envs:
      # Supabase
      - key: SUPABASE_URL
        scope: RUN_TIME
        type: SECRET
      - key: SUPABASE_SERVICE_KEY
        scope: RUN_TIME
        type: SECRET

      # Stripe
      - key: STRIPE_SECRET_KEY
        scope: RUN_TIME
        type: SECRET

      # AI
      - key: OPENROUTER_API_KEY
        scope: RUN_TIME
        type: SECRET

      # Storage
      - key: DO_SPACES_KEY
        scope: RUN_TIME
        type: SECRET
      - key: DO_SPACES_SECRET
        scope: RUN_TIME
        type: SECRET

static_sites:
  - name: frontend
    github:
      repo: your-private-repo/presswire-v2
      branch: main
      deploy_on_push: true

    source_dir: /static

    routes:
      - path: /static
```

---

## 📊 Migration from V1

### Migration Script

```python
# scripts/migrate_from_v1.py
import asyncio
import httpx
from supabase import create_client
from pathlib import Path
import json

async def migrate_v1_to_v2():
    """Migrate all data from v1 to v2"""

    print("🚀 Starting migration from v1 to v2...")

    # 1. Connect to Supabase
    supabase = create_client(
        os.getenv('SUPABASE_URL'),
        os.getenv('SUPABASE_SERVICE_KEY')
    )

    # 2. Fetch PRs from GitHub
    github_prs = await fetch_github_prs()

    # 3. Migrate each PR
    for pr in github_prs:
        print(f"Migrating: {pr['filename']}")

        # Parse HTML
        pr_data = parse_v1_html(pr['content'])

        # Insert to database
        supabase.table('press_releases').insert({
            'headline': pr_data['headline'],
            'summary': pr_data['summary'],
            'content': pr_data['content'],
            'company_name': pr_data['company'],
            'cro_number': pr_data['cro'],
            'slug': pr_data['slug'],
            'status': 'published',
            'created_at': pr_data['published_date']
        }).execute()

        # Generate new static file
        await generate_static_file(pr_data)

    # 4. Migrate Stripe customers
    await migrate_stripe_customers()

    print("✅ Migration complete!")

async def fetch_github_prs():
    """Fetch all PRs from GitHub"""
    # Implementation here
    pass

def parse_v1_html(html_content: str):
    """Parse v1 HTML to extract data"""
    # BeautifulSoup parsing here
    pass

async def generate_static_file(pr_data):
    """Generate new static file in v2 format"""
    # Implementation here
    pass

if __name__ == "__main__":
    asyncio.run(migrate_v1_to_v2())
```

---

## 📋 Implementation Checklist

### Week 1: Development
- [ ] Day 1: Project setup, configuration, models
- [ ] Day 2: PydanticAI agents implementation
- [ ] Day 3: Database and services
- [ ] Day 4: API endpoints
- [ ] Day 5: Testing and refinement

### Week 2: Deployment
- [ ] Day 1: Docker setup and testing
- [ ] Day 2: Digital Ocean deployment
- [ ] Day 3: Data migration from v1
- [ ] Day 4: DNS cutover preparation
- [ ] Day 5: Go live and monitor

---

## 🎯 Key Benefits of This Architecture

1. **Type Safety Throughout** - Pydantic models ensure data integrity
2. **AI-Powered** - PydanticAI agents for intelligent content
3. **Perfect SEO** - Static HTML files with all meta tags
4. **No Rebuilds** - Static files generated on-demand
5. **Private Code** - Repository can be fully private
6. **Professional Stack** - Modern Python with best practices
7. **Scalable** - Can handle 100,000+ PRs
8. **Cost Effective** - €12-15/month total

---

## 📚 Required Dependencies

```txt
# requirements.txt
# Core
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.5.3
pydantic-settings==2.1.0
pydantic-ai==0.0.12

# Database
supabase==2.3.0
asyncpg==0.29.0

# AI & External Services
openai==1.9.0
stripe==7.9.0
resend==0.7.0
httpx==0.26.0

# Storage
boto3==1.34.0  # For S3/Spaces

# Templates & Static
jinja2==3.1.3
python-multipart==0.0.6

# Background Tasks
celery==5.3.4
redis==5.0.1

# Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-decouple==3.8

# Testing
pytest==7.4.4
pytest-asyncio==0.23.3

# Dev Tools
black==23.12.1
ruff==0.1.9
```

---

## 🚀 Quick Start Commands

```bash
# Clone and setup
git clone [your-private-repo]/presswire-v2
cd presswire-v2
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Environment setup
cp .env.example .env
# Edit .env with your credentials

# Database setup
python scripts/setup_supabase.py

# Run locally
uvicorn app.main:app --reload

# Run tests
pytest

# Deploy to Digital Ocean
doctl apps create --spec deploy/digitalocean/app.yaml

# Migrate from v1
python scripts/migrate_from_v1.py
```

---

*This unified plan combines the incremental improvements of v1.1 with the clean architecture of v2.0, leveraging PydanticAI for intelligent features and maintaining perfect SEO through hybrid static/dynamic architecture.*