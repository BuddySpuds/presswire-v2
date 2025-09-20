# PressWire.ie v2.0 - Parallel FastAPI Implementation Plan

## Executive Summary

Build a completely new FastAPI-based system in parallel with the current Netlify deployment, then perform a clean cutover. This approach avoids incremental migration complexity and allows for a modern, optimized architecture from day one.

**Key Benefits:**
- No disruption to current system
- Clean, modern codebase
- Private repository possible
- No more GitHub commits for PRs
- Hybrid static/dynamic for perfect SEO
- Professional Python/FastAPI stack

---

## Phase 1: Local Development Setup (Day 1-2)

### 1.1 Create New Project Structure

```bash
# Create parallel project directory
mkdir ~/presswire-v2
cd ~/presswire-v2
git init
git remote add origin [new-private-repo]
```

### 1.2 Directory Structure

```
presswire-v2/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI application entry
│   │   ├── config.py                  # Environment configuration
│   │   ├── database.py                # Supabase connection
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── press_release.py      # SQLAlchemy/Supabase models
│   │   │   ├── user.py               # User account model
│   │   │   ├── payment.py            # Payment records
│   │   │   └── analytics.py          # Analytics data model
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── pr_schema.py          # Pydantic validation
│   │   │   ├── auth_schema.py        # Auth request/response
│   │   │   └── payment_schema.py     # Payment data
│   │   │
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py               # /api/auth/* endpoints
│   │   │   ├── press_releases.py     # /api/pr/* endpoints
│   │   │   ├── payments.py           # /api/payments/* Stripe
│   │   │   ├── analytics.py          # /api/analytics/*
│   │   │   ├── search.py             # /api/search/*
│   │   │   └── public.py             # Public facing routes
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py         # OpenRouter/Gemini
│   │   │   ├── email_service.py      # Resend integration
│   │   │   ├── cro_service.py        # CRO validation
│   │   │   ├── domain_verifier.py    # Domain verification
│   │   │   ├── static_generator.py   # Static HTML generation
│   │   │   └── stripe_service.py     # Stripe operations
│   │   │
│   │   ├── middleware/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py               # JWT verification
│   │   │   ├── rate_limit.py         # Rate limiting
│   │   │   └── cors.py               # CORS config
│   │   │
│   │   ├── templates/                # Jinja2 templates
│   │   │   ├── base.html
│   │   │   ├── landing.html
│   │   │   ├── pr_detail.html        # Dynamic PR template
│   │   │   ├── pr_static.html        # Static PR template
│   │   │   ├── dashboard.html
│   │   │   ├── generate.html
│   │   │   └── components/
│   │   │       ├── header.html
│   │   │       ├── footer.html
│   │   │       └── share_buttons.html
│   │   │
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── security.py           # Password hashing
│   │       ├── tokens.py             # JWT generation
│   │       └── validators.py         # Input validation
│   │
│   ├── static/                        # Static assets
│   │   ├── css/
│   │   │   └── tailwind.css          # Copy from v1
│   │   ├── js/
│   │   │   └── main.js               # Copy/adapt from v1
│   │   ├── images/
│   │   └── news/                     # Generated static PRs
│   │       └── .gitkeep
│   │
│   ├── migrations/
│   │   ├── 001_initial_schema.sql
│   │   ├── 002_add_indexes.sql
│   │   └── 003_add_search.sql
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_auth.py
│   │   ├── test_pr_generation.py
│   │   └── test_payments.py
│   │
│   ├── scripts/
│   │   ├── migrate_from_v1.py       # Migration script
│   │   ├── generate_static_prs.py   # Bulk static generation
│   │   └── backup_database.py       # Backup utility
│   │
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── .env.example
│   ├── .env.local                   # Local development
│   ├── .env.production              # Production (DO NOT COMMIT)
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── pytest.ini
│
├── deploy/
│   ├── digitalocean/
│   │   ├── app.yaml                 # DO App Platform config
│   │   └── deploy.sh                # Deployment script
│   ├── nginx/
│   │   └── nginx.conf              # Nginx configuration
│   └── cloudflare/
│       └── workers.js              # Edge workers (optional)
│
├── docs/
│   ├── API.md                      # API documentation
│   ├── DEPLOYMENT.md               # Deployment guide
│   └── MIGRATION.md                # Migration from v1
│
├── .github/
│   └── workflows/
│       ├── test.yml                # CI/CD testing
│       └── deploy.yml              # Auto-deploy
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## Phase 2: Files to Copy/Adapt from Current Project

### 2.1 Direct Copy Files

```bash
# From current project to presswire-v2/backend/

# Static assets (with modifications)
cp /Agentic_NewsWire/index.html → static/templates/landing.html
cp /Agentic_NewsWire/generate.html → static/templates/generate.html
cp /Agentic_NewsWire/manage.html → static/templates/dashboard.html
cp /Agentic_NewsWire/success.html → static/templates/success.html

# CSS (use as-is)
cp -r /Agentic_NewsWire/css/* → static/css/

# Images/assets
cp -r /Agentic_NewsWire/images/* → static/images/
```

### 2.2 Service Logic to Port (Convert JS to Python)

| Current File (JS) | New File (Python) | Purpose |
|------------------|-------------------|---------|
| `api/verify-domain.js` | `services/domain_verifier.py` | Domain verification logic |
| `api/lookup-company.js` | `services/cro_service.py` | CRO validation |
| `api/generate-pr.js` | `services/ai_service.py` | AI generation logic |
| `api/stripe-webhook.js` | `services/stripe_service.py` | Payment processing |
| `api/send-email.js` | `services/email_service.py` | Email sending |
| `api/analytics.js` | `routers/analytics.py` | Analytics tracking |

### 2.3 Configuration to Preserve

```python
# Extract from current .env and api files:

# Email templates (from send-email.js)
EMAIL_TEMPLATES = {
    'verification': '6-digit code template',
    'pr_notification': 'PR published template',
    'payment_success': 'Payment confirmation'
}

# PR Template (from generate-pr.js createPRHTML function)
PR_TEMPLATE_FEATURES = {
    'share_buttons': ['LinkedIn', 'Twitter/X'],
    'meta_tags': 'Open Graph, Twitter Cards',
    'schema_markup': 'NewsArticle schema',
    'analytics': 'Session tracking code'
}

# Pricing tiers (from Stripe configuration)
PRICING = {
    'basic': 99,
    'professional': 199,
    'premium': 399
}
```

---

## Phase 3: Core Implementation Files

### 3.1 Main Application (app/main.py)

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager

from app.routers import auth, press_releases, payments, analytics, search, public
from app.database import init_db
from app.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    pass

app = FastAPI(
    title="PressWire.ie API",
    version="2.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/news", StaticFiles(directory="static/news", html=True), name="news")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(press_releases.router, prefix="/api/pr", tags=["Press Releases"])
app.include_router(payments.router, prefix="/api/payments", tags=["Payments"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(public.router, tags=["Public"])

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})
```

### 3.2 Configuration (app/config.py)

```python
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # App
    APP_NAME: str = "PressWire.ie"
    VERSION: str = "2.0"
    DEBUG: bool = False

    # Database
    SUPABASE_URL: str
    SUPABASE_KEY: str

    # Authentication
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Stripe
    STRIPE_SECRET_KEY: str
    STRIPE_PUBLISHABLE_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    # Email (Resend)
    RESEND_API_KEY: str
    FROM_EMAIL: str = "noreply@presswire.ie"

    # AI (OpenRouter)
    OPENROUTER_API_KEY: str
    AI_MODEL: str = "google/gemini-2.0-flash:free"

    # CRO API
    CRO_API_URL: str = "https://services.cro.ie/api/v1"

    # CORS
    ALLOWED_ORIGINS: List[str] = ["https://presswire.ie"]

    # Static files
    STATIC_DIR: str = "static"
    NEWS_DIR: str = "static/news"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

### 3.3 Database Connection (app/database.py)

```python
from supabase import create_client, Client
from app.config import settings
import logging

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.client: Client = None

    async def init(self):
        """Initialize database connection"""
        try:
            self.client = create_client(
                settings.SUPABASE_URL,
                settings.SUPABASE_KEY
            )
            logger.info("Database connected successfully")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise

    def get_client(self) -> Client:
        if not self.client:
            raise Exception("Database not initialized")
        return self.client

# Global database instance
db = Database()

async def init_db():
    await db.init()

def get_db() -> Client:
    return db.get_client()
```

### 3.4 Static Generator Service (app/services/static_generator.py)

```python
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from typing import Dict, Any
import json

class StaticGenerator:
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader('app/templates'),
            autoescape=True
        )
        self.template = self.env.get_template('pr_static.html')

    async def generate_pr_html(self, pr_data: Dict[str, Any]) -> str:
        """
        Generate static HTML file for PR with all SEO features
        """
        # Enhance data with SEO elements
        enhanced_data = self._enhance_pr_data(pr_data)

        # Render HTML
        html_content = self.template.render(**enhanced_data)

        # Save to static directory
        filename = f"{pr_data['slug']}.html"
        filepath = Path(f"static/news/{filename}")

        # Ensure directory exists
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        filepath.write_text(html_content, encoding='utf-8')

        # Also save metadata for search
        self._save_metadata(pr_data['slug'], enhanced_data)

        return filename

    def _enhance_pr_data(self, pr_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add SEO and social features"""

        # Generate keywords
        keywords = self._generate_keywords(pr_data)

        # Detect categories
        categories = self._detect_categories(pr_data)

        # Format dates
        publish_date = datetime.now().strftime('%B %d, %Y')

        return {
            **pr_data,
            'keywords': keywords,
            'categories': categories,
            'publish_date': publish_date,
            'schema_json': self._generate_schema(pr_data),
            'og_image': f"https://presswire.ie/api/og-image/{pr_data['slug']}"
        }

    def _generate_keywords(self, pr_data: Dict[str, Any]) -> str:
        """Generate SEO keywords"""
        keywords = [
            'Irish Business',
            pr_data.get('company_name', ''),
            'Press Release',
            'Ireland',
            pr_data.get('cro_number', '')
        ]

        # Add words from headline
        headline_words = pr_data.get('headline', '').split()
        keywords.extend([w for w in headline_words if len(w) > 4][:3])

        return ', '.join(filter(None, keywords))

    def _detect_categories(self, pr_data: Dict[str, Any]) -> List[str]:
        """Auto-detect PR categories"""
        categories = []
        content_lower = (pr_data.get('content', '') + ' ' +
                        pr_data.get('headline', '')).lower()

        category_keywords = {
            'Product Launch': ['product', 'launch', 'introducing', 'announces'],
            'Funding': ['funding', 'investment', 'series', 'raises'],
            'Partnership': ['partnership', 'collaboration', 'partners with'],
            'Award': ['award', 'recognition', 'winner', 'awarded'],
            'Expansion': ['expansion', 'opening', 'new location', 'growing']
        }

        for category, keywords in category_keywords.items():
            if any(kw in content_lower for kw in keywords):
                categories.append(category)

        if not categories:
            categories.append('Company News')

        return categories

    def _generate_schema(self, pr_data: Dict[str, Any]) -> str:
        """Generate Schema.org JSON-LD"""
        schema = {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": pr_data.get('headline', ''),
            "description": pr_data.get('summary', ''),
            "datePublished": datetime.now().isoformat(),
            "dateModified": datetime.now().isoformat(),
            "author": {
                "@type": "Organization",
                "name": pr_data.get('company_name', '')
            },
            "publisher": {
                "@type": "Organization",
                "name": "PressWire.ie",
                "url": "https://presswire.ie",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://presswire.ie/static/images/logo.png"
                }
            }
        }
        return json.dumps(schema, indent=2)

    def _save_metadata(self, slug: str, data: Dict[str, Any]):
        """Save PR metadata for search indexing"""
        metadata_file = Path(f"static/news/.metadata/{slug}.json")
        metadata_file.parent.mkdir(parents=True, exist_ok=True)

        metadata = {
            'slug': slug,
            'headline': data.get('headline'),
            'company': data.get('company_name'),
            'cro': data.get('cro_number'),
            'categories': data.get('categories'),
            'published': datetime.now().isoformat(),
            'keywords': data.get('keywords')
        }

        metadata_file.write_text(json.dumps(metadata, indent=2))
```

### 3.5 Requirements.txt

```txt
# Core
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6

# Database
supabase==2.3.0
sqlalchemy==2.0.25
asyncpg==0.29.0

# Authentication
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-decouple==3.8

# Validation
pydantic==2.5.3
pydantic-settings==2.1.0
email-validator==2.1.0

# Templates
jinja2==3.1.3
markdown==3.5.1

# External Services
stripe==7.9.0
resend==0.7.0
httpx==0.26.0

# AI
openai==1.9.0  # For OpenRouter API

# Development
pytest==7.4.4
pytest-asyncio==0.23.3
black==23.12.1
flake8==7.0.0

# Production
gunicorn==21.2.0
redis==5.0.1  # For caching
sentry-sdk[fastapi]==1.39.1  # Error tracking
```

---

## Phase 4: Migration Strategy

### 4.1 Data Migration Script

```python
# scripts/migrate_from_v1.py
import os
import json
import asyncio
from datetime import datetime
from pathlib import Path
import httpx
from supabase import create_client
from bs4 import BeautifulSoup

class V1Migrator:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.github_owner = 'BuddySpuds'
        self.github_repo = 'presswire-ie'
        self.supabase = create_client(
            os.getenv('SUPABASE_URL'),
            os.getenv('SUPABASE_KEY')
        )

    async def migrate_all(self):
        """Complete migration from v1 to v2"""
        print("Starting migration from v1 to v2...")

        # 1. Migrate existing PRs
        await self.migrate_press_releases()

        # 2. Migrate Stripe customers
        await self.migrate_stripe_data()

        # 3. Generate static files
        await self.generate_static_files()

        print("Migration complete!")

    async def migrate_press_releases(self):
        """Fetch PRs from GitHub and migrate to database"""
        print("Migrating press releases...")

        # Fetch list of PR files from GitHub
        async with httpx.AsyncClient() as client:
            headers = {'Authorization': f'token {self.github_token}'}
            response = await client.get(
                f'https://api.github.com/repos/{self.github_owner}/{self.github_repo}/contents/news',
                headers=headers
            )
            files = response.json()

        for file in files:
            if file['name'].endswith('.html') and file['name'] != 'index.html':
                print(f"Migrating {file['name']}...")

                # Fetch HTML content
                response = await client.get(file['download_url'])
                html_content = response.text

                # Parse HTML to extract data
                pr_data = self.parse_pr_html(html_content, file['name'])

                # Insert into database
                self.supabase.table('press_releases').insert(pr_data).execute()

                # Generate new static file
                await self.generate_static_file(pr_data)

    def parse_pr_html(self, html: str, filename: str) -> dict:
        """Extract PR data from HTML"""
        soup = BeautifulSoup(html, 'html.parser')

        # Extract metadata
        headline = soup.find('h1').text if soup.find('h1') else ''
        summary = soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else ''

        # Extract company info from filename or content
        slug = filename.replace('.html', '')

        return {
            'slug': slug,
            'headline': headline,
            'summary': summary,
            'content': str(soup.find('article')) if soup.find('article') else html,
            'status': 'published',
            'created_at': datetime.now().isoformat()
        }

    async def migrate_stripe_data(self):
        """Migrate Stripe customer data"""
        import stripe
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

        # Fetch customers
        customers = stripe.Customer.list(limit=100)

        for customer in customers:
            # Check if customer exists in our system
            customer_data = {
                'stripe_customer_id': customer.id,
                'email': customer.email,
                'created_at': datetime.fromtimestamp(customer.created).isoformat()
            }

            self.supabase.table('customers').insert(customer_data).execute()
```

### 4.2 Docker Configuration

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create directories for static files
RUN mkdir -p static/news static/news/.metadata

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8080"
    env_file:
      - .env.local
    volumes:
      - ./static/news:/app/static/news
      - ./app:/app/app  # For hot reload in development
    command: uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

---

## Phase 5: Deployment to Digital Ocean

### 5.1 Digital Ocean App Platform Configuration

```yaml
# deploy/digitalocean/app.yaml
name: presswire-v2
region: lon1
services:
  - name: api
    github:
      repo: yourusername/presswire-v2
      branch: main
      deploy_on_push: true
    source_dir: /backend
    dockerfile_path: Dockerfile
    http_port: 8080
    instance_count: 1
    instance_size_slug: basic-xxs  # $5/month
    routes:
      - path: /
    envs:
      - key: SUPABASE_URL
        scope: RUN_TIME
        type: SECRET
      - key: SUPABASE_KEY
        scope: RUN_TIME
        type: SECRET
      - key: STRIPE_SECRET_KEY
        scope: RUN_TIME
        type: SECRET
      - key: RESEND_API_KEY
        scope: RUN_TIME
        type: SECRET
      - key: OPENROUTER_API_KEY
        scope: RUN_TIME
        type: SECRET
    health_check:
      http_path: /health
      initial_delay_seconds: 10
      period_seconds: 10
```

### 5.2 Deployment Script

```bash
#!/bin/bash
# deploy/deploy.sh

echo "🚀 Deploying PressWire v2 to Digital Ocean..."

# 1. Run tests
echo "Running tests..."
pytest

# 2. Build Docker image
echo "Building Docker image..."
docker build -t presswire-v2:latest .

# 3. Push to registry
echo "Pushing to registry..."
doctl registry login
docker tag presswire-v2:latest registry.digitalocean.com/presswire/api:latest
docker push registry.digitalocean.com/presswire/api:latest

# 4. Deploy app
echo "Deploying to Digital Ocean..."
doctl apps create --spec deploy/digitalocean/app.yaml

# 5. Run migrations
echo "Running database migrations..."
doctl apps run presswire-v2 -- python scripts/migrate_from_v1.py

echo "✅ Deployment complete!"
```

---

## Phase 6: Testing & Cutover

### 6.1 Testing Checklist

```markdown
## Pre-Cutover Testing

### Core Functionality
- [ ] User registration/login
- [ ] Domain verification
- [ ] CRO validation
- [ ] PR generation with AI
- [ ] Static file generation
- [ ] Payment processing
- [ ] Email notifications
- [ ] Analytics tracking
- [ ] Search functionality

### Performance
- [ ] Page load < 1 second
- [ ] API response < 200ms
- [ ] Static PR serving < 500ms
- [ ] Search results < 100ms

### SEO Validation
- [ ] Static files have all meta tags
- [ ] Schema.org markup present
- [ ] Sitemap.xml generated
- [ ] Robots.txt configured
- [ ] Canonical URLs correct

### Security
- [ ] Authentication working
- [ ] Rate limiting active
- [ ] Input validation
- [ ] CORS configured
- [ ] HTTPS enforced
```

### 6.2 Cutover Plan

```markdown
## Cutover Procedure

### Pre-Cutover (Friday Evening)
1. [ ] Final data export from v1
2. [ ] Run migration script
3. [ ] Generate all static files
4. [ ] Test on staging domain
5. [ ] Backup everything

### Cutover (Saturday Morning)
1. [ ] Put v1 in maintenance mode
2. [ ] Final data sync
3. [ ] Update DNS records:
   - A record: Point to Digital Ocean IP
   - Remove Netlify records
4. [ ] Monitor DNS propagation
5. [ ] Test all critical paths

### Post-Cutover
1. [ ] Monitor error logs
2. [ ] Check analytics
3. [ ] Verify payments working
4. [ ] Test email delivery
5. [ ] Keep v1 available at old.presswire.ie for 30 days
```

---

## Phase 7: Monitoring & Optimization

### 7.1 Monitoring Setup

```python
# app/monitoring.py
from sentry_sdk import init as sentry_init
from sentry_sdk.integrations.fastapi import FastApiIntegration
import logging

def setup_monitoring():
    # Sentry for error tracking
    sentry_init(
        dsn=os.getenv("SENTRY_DSN"),
        integrations=[FastApiIntegration()],
        traces_sample_rate=0.1,
        environment=os.getenv("ENVIRONMENT", "production")
    )

    # Structured logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
```

### 7.2 Performance Optimization

```python
# app/cache.py
import redis
from functools import wraps
import json
import hashlib

redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

def cache_result(expire_seconds=300):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = f"{func.__name__}:{hashlib.md5(str(args).encode()).hexdigest()}"

            # Try to get from cache
            cached = redis_client.get(cache_key)
            if cached:
                return json.loads(cached)

            # Call function
            result = await func(*args, **kwargs)

            # Store in cache
            redis_client.setex(cache_key, expire_seconds, json.dumps(result))

            return result
        return wrapper
    return decorator
```

---

## Appendix A: Environment Variables

```bash
# .env.example

# Application
APP_NAME=PressWire.ie
ENVIRONMENT=development
DEBUG=true
SECRET_KEY=your-secret-key-here

# Database
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-anon-key
SUPABASE_SERVICE_KEY=your-supabase-service-key

# Authentication
JWT_SECRET_KEY=your-jwt-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Email (Resend)
RESEND_API_KEY=re_...
FROM_EMAIL=noreply@presswire.ie
SUPPORT_EMAIL=support@presswire.ie

# AI (OpenRouter)
OPENROUTER_API_KEY=sk-or-v1-...
AI_MODEL=google/gemini-2.0-flash:free

# Redis (optional)
REDIS_URL=redis://localhost:6379

# Sentry (optional)
SENTRY_DSN=https://...@sentry.io/...

# Digital Ocean
DO_SPACES_KEY=...
DO_SPACES_SECRET=...
```

---

## Appendix B: Cost Analysis

### Monthly Costs

| Service | Tier | Cost |
|---------|------|------|
| Digital Ocean App Platform | Basic | €12/month |
| Supabase | Free | €0/month |
| Cloudflare CDN | Free | €0/month |
| Domain | Annual | €1.25/month |
| **Total** | | **€13.25/month** |

### Comparison with Current

| Metric | Current (v1) | New (v2) |
|--------|-------------|----------|
| Monthly Cost | €1.25 | €13.25 |
| Build Minutes | 300+/month | 0 |
| Rebuilds per PR | Yes | No |
| Code Privacy | Public | Private |
| Scalability | Limited | Excellent |
| Performance | Good | Excellent |

---

## Appendix C: Timeline

### Week 1: Development
- Day 1-2: Setup and core structure
- Day 3-4: Service implementation
- Day 5: Testing

### Week 2: Staging
- Day 1-2: Deploy to Digital Ocean staging
- Day 3-4: Migration testing
- Day 5: Performance optimization

### Week 3: Cutover
- Monday-Thursday: Final testing
- Friday: Pre-cutover preparation
- Weekend: Cutover

### Week 4: Monitoring
- Monitor and optimize
- Fix any issues
- Document learnings

---

## Success Metrics

### Technical
- [ ] Zero GitHub commits for PRs
- [ ] Page load < 1 second
- [ ] 99.9% uptime
- [ ] All SEO scores maintained

### Business
- [ ] No service interruption during cutover
- [ ] All existing PRs migrated
- [ ] Payment processing uninterrupted
- [ ] Customer data preserved

### Operational
- [ ] Code repository private
- [ ] Deployment automated
- [ ] Monitoring in place
- [ ] Backup strategy implemented

---

*This document serves as the complete implementation guide for PressWire.ie v2.0*
*Last Updated: December 2024*
*Status: READY FOR IMPLEMENTATION*