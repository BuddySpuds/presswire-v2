"""Database connection and session management"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import AsyncGenerator
from app.core.config import get_settings

settings = get_settings()

# Create async engine
# Use SQLite for local development if DATABASE_URL contains placeholder
database_url = settings.database_url
if database_url and "your-db-password" in database_url:
    database_url = None  # Fall back to SQLite

engine = create_async_engine(
    database_url or "sqlite+aiosqlite:///./presswire.db",
    echo=settings.app_debug,
    future=True
)

# Create session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get database session"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()