# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PressWire.ie v2 is a complete rebuild of Ireland's domain-verified press release platform, transitioning from static architecture to a modern FastAPI + PydanticAI implementation. Currently in early development with foundational structure in place.

## Tech Stack

- **Backend**: FastAPI 0.115.0 with async Python
- **AI**: PydanticAI 0.0.15 for type-safe AI agents (https://ai.pydantic.dev/)
- **Database**: Supabase with SQLAlchemy 2.0.36 and AsyncPG
- **Auth**: JWT with python-jose and passlib
- **Payments**: Stripe 11.0.0
- **Email**: Resend 2.5.0
- **Testing**: Playwright (via MCP) for end-to-end testing
- **Containerization**: Docker for consistent environments
- **Deployment**: Digital Ocean App Platform
- **CI/CD**: GitHub Actions → Digital Ocean

## Development Environment

### Local Setup (Mac M4)
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env

# Run with Docker
docker compose up -d

# Run locally
python main.py

# Database migrations
alembic upgrade head
alembic revision --autogenerate -m "description"
```

### MCP (Model Context Protocol) Integration

**Digital Ocean MCP**: Control and deploy apps directly
```bash
# Deploy to Digital Ocean
mcp digitalocean deploy --app presswire-v2

# Check deployment status
mcp digitalocean status --app presswire-v2

# View logs
mcp digitalocean logs --app presswire-v2
```

**GitHub MCP**: Repository management and CI/CD triggers
```bash
# Push to trigger deployment
git push origin main

# Create PR for review
gh pr create --title "Feature: ..." --body "..."
```

**Playwright MCP**: Automated testing
```bash
# Run E2E tests
playwright test

# Run specific test suite
playwright test tests/e2e/domain-verification.spec.ts

# Debug mode
playwright test --debug
```

## Docker Configuration

### Development Container
```dockerfile
# Dockerfile.dev
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Container
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose (Local Development)
```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    env_file:
      - .env
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

## CI/CD Pipeline

### GitHub Actions → Digital Ocean
```yaml
# .github/workflows/deploy.yml
name: Deploy to Digital Ocean
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          pip install -r requirements.txt
          pytest

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: digitalocean/action-doctl@v2
        with:
          token: ${{ secrets.DIGITALOCEAN_ACCESS_TOKEN }}
      - run: doctl apps create-deployment ${{ secrets.APP_ID }}
```

### Deployment Workflow
1. **Local Development** (Mac M4) → Test with Docker
2. **Git Push** → GitHub repository
3. **GitHub Actions** → Run tests
4. **Digital Ocean** → Auto-deploy on main branch
5. **MCP Monitoring** → Check deployment status

## Architecture

### Current Structure
```
presswire-v2/
├── main.py               # FastAPI entry point
├── templates/            # HTML templates
├── static/              # Static assets
├── docs/                # Documentation
├── Dockerfile           # Production container
├── Dockerfile.dev       # Development container
├── docker-compose.yml   # Local orchestration
├── .github/workflows/   # CI/CD pipelines
└── requirements.txt     # Dependencies
```

### Planned Implementation
```
app/
├── models/              # Pydantic data models
├── agents/              # PydanticAI agents
├── schemas/             # API schemas
├── api/v1/             # API endpoints
├── core/               # Core functionality
├── services/           # External integrations
└── tests/
    ├── unit/           # Unit tests
    ├── integration/    # Integration tests
    └── e2e/           # Playwright E2E tests
```

## Core Business Logic

### Domain Verification System
- Company domain email verification
- CRO (Companies Registration Office) integration
- Automatic company validation

### PydanticAI Agent Architecture
```python
# Example agent structure
from pydantic_ai import Agent
from pydantic import BaseModel

class PRContent(BaseModel):
    headline: str
    body: str
    seo_title: str
    meta_description: str

pr_agent = Agent(
    "openai:gpt-4",
    result_type=PRContent,
    system_prompt="Generate optimized press release content"
)
```

## Development Commands

### Code Quality
```bash
black .                    # Format code
ruff check .              # Lint
mypy .                    # Type check
```

### Testing
```bash
pytest                    # Run all tests
pytest -v                 # Verbose
pytest tests/unit/        # Unit tests only
playwright test           # E2E tests
```

### Docker Operations
```bash
docker compose up         # Start services
docker compose down       # Stop services
docker compose logs -f    # View logs
docker compose exec web bash  # Shell access
```

### Digital Ocean Deployment
```bash
# Manual deployment via MCP
mcp digitalocean deploy --app presswire-v2

# Check app status
doctl apps list
doctl apps get <app-id>

# View deployment logs
doctl apps logs <app-id> --type deploy
```

## Environment Configuration

Required environment variables (see .env.example):
- **Database**: `DATABASE_URL`, `SUPABASE_URL`, `SUPABASE_KEY`
- **Auth**: `SECRET_KEY`, `JWT_SECRET_KEY`
- **Stripe**: `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`
- **Email**: `RESEND_API_KEY`
- **AI**: `OPENROUTER_API_KEY` or `OPENAI_API_KEY`
- **CRO**: `CRO_API_KEY`, `CRO_API_URL`
- **Digital Ocean**: `DIGITALOCEAN_ACCESS_TOKEN`, `APP_ID`

## Key Implementation Patterns

### FastAPI Best Practices
- Dependency injection for database sessions
- Proper async/await patterns
- Pydantic for all data validation
- Background tasks for webhooks

### PydanticAI Integration
- Type-safe agent definitions with result_type
- Structured outputs with Pydantic models
- Cost tracking and retry logic
- System prompts for consistent behavior

### Database Patterns
- Async SQLAlchemy with connection pooling
- Alembic for migrations
- Transaction management
- Optimistic locking

### Testing Strategy
- Unit tests for business logic
- Integration tests for API endpoints
- Playwright E2E tests for user flows
- Mock external services (Stripe, OpenAI)

## Deployment Considerations

### Digital Ocean App Platform
- Auto-scaling based on traffic
- Managed database connections
- Environment variable management
- SSL/TLS certificates handled automatically

### Performance Optimization
- Static file CDN delivery
- Database connection pooling
- Redis caching for frequent queries
- Background job processing with Celery

## Current Development State

**Early Stage** - Foundation in place:
1. Basic FastAPI structure exists
2. Templates and static assets ready
3. Docker configuration needed
4. CI/CD pipeline to be implemented
5. MCP integrations to be configured
6. Core features to be built

## Important Business Context

- **Target Market**: 500,000+ Irish companies
- **Pricing**: €99/€199/€399 tiers
- **Compliance**: CRO verification required
- **SEO**: Static HTML generation critical
- **Scale**: Handle burst traffic during announcements
- **Security**: Domain verification prevents spam