# PressWire.ie v2.0 🚀

Ireland's Domain-Verified Press Release Platform - Built with FastAPI, PydanticAI, and Supabase

## 🎯 Overview

PressWire v2 is a complete rebuild of Ireland's leading press release distribution platform:
- **Domain Verification**: Only verified company emails can publish
- **AI-Powered**: PydanticAI 1.0.10 for content generation
- **Modern Stack**: FastAPI + Supabase + Docker
- **SEO Optimized**: Static HTML with schema.org markup

## 🐳 Quick Start with Docker (Recommended)

```bash
# 1. Clone and setup
git clone <your-repo>
cd presswire-v2

# 2. Configure environment
cp .env.example .env
# Edit .env - add your AI API key

# 3. Run with Docker
./docker-setup.sh
```

**App running at**: http://localhost:8000

## 🔧 Alternative: Virtual Environment

```bash
# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

## 🐳 Docker Commands

```bash
docker-compose up -d        # Start services
docker-compose logs -f      # View logs
docker-compose down         # Stop services
docker-compose exec web bash # Shell access
```

## 🗄️ Supabase Setup

1. Run: `docker-compose exec web python setup_supabase.py`
2. Copy the SQL output
3. Go to [Supabase Dashboard](https://supabase.com/dashboard/project/klwyvgraddjrawnbonnd)
4. Paste in SQL Editor and run

## 📁 Project Structure

```
presswire-v2/
├── app/
│   ├── agents/          # PydanticAI agents
│   ├── api/             # API endpoints
│   ├── core/            # Core functionality
│   ├── models/          # Database models
│   └── services/        # External services
├── templates/           # HTML templates
├── docker-compose.yml   # Docker orchestration
└── main.py             # Application entry
```

## 🔑 Environment Variables

Required in `.env`:
- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` - For AI features
- `SUPABASE_URL` - Your Supabase project URL
- `SUPABASE_KEY` - Supabase anon key

## 📚 API Documentation

- **Swagger**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

## 🚢 Deployment

Push to GitHub → Auto-deploy to Digital Ocean

## 📄 License

Copyright © 2024 PressWire.ie

---

See `docs/` for detailed documentation.
