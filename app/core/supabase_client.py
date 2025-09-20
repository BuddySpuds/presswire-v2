"""Supabase client configuration and initialization"""

from supabase import create_client, Client
from app.core.config import get_settings
from typing import Optional

settings = get_settings()


class SupabaseClient:
    """Singleton Supabase client"""
    _instance: Optional[Client] = None

    @classmethod
    def get_client(cls) -> Client:
        """Get or create Supabase client instance"""
        if cls._instance is None:
            if not settings.supabase_url or not settings.supabase_key:
                raise ValueError(
                    "Supabase URL and key must be set in environment variables"
                )

            cls._instance = create_client(
                settings.supabase_url,
                settings.supabase_key
            )

        return cls._instance


def get_supabase() -> Client:
    """Dependency to get Supabase client"""
    return SupabaseClient.get_client()


async def test_supabase_connection():
    """Test Supabase connection"""
    try:
        client = get_supabase()

        # Try to fetch from a test table or auth
        response = client.auth.get_session()
        print("✅ Supabase connection successful!")

        # Check if press_releases table exists
        try:
            result = client.table('press_releases').select("*").limit(1).execute()
            print("✅ press_releases table exists")
        except Exception as e:
            print("⚠️  press_releases table not found - will create with migrations")

        return True
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        return False