"""Configuration settings for PressWire v2"""

from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    # Application
    app_name: str = "PressWire.ie"
    app_version: str = "2.0.0"
    app_env: str = "development"
    app_debug: bool = True
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_url: str = "http://localhost:8000"

    # Database
    database_url: Optional[str] = None
    supabase_url: Optional[str] = None
    supabase_key: Optional[str] = None
    supabase_service_key: Optional[str] = None

    # Authentication
    jwt_secret_key: str = "development-secret-key-change-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Stripe
    stripe_secret_key: Optional[str] = None
    stripe_publishable_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None

    # Email (Resend)
    resend_api_key: Optional[str] = None
    email_from: str = "noreply@presswire.ie"

    # AI Configuration
    openrouter_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    pydantic_ai_model: str = "gpt-4o-mini"

    # CRO API
    cro_api_base_url: str = "https://api.vision-net.ie/live"
    cro_api_key: Optional[str] = None

    # Storage
    storage_backend: str = "supabase"
    storage_bucket: str = "press-releases"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Monitoring
    sentry_dsn: Optional[str] = None
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()