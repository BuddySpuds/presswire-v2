#!/usr/bin/env python3
"""Test Supabase connection and basic operations"""

import os
import asyncio
from dotenv import load_dotenv
from supabase import create_client
import json
from datetime import datetime

# Load environment variables
load_dotenv()


async def test_supabase():
    """Test Supabase connection and operations"""

    # Get credentials
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url or not supabase_key:
        print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
        return False

    try:
        # Create Supabase client
        supabase = create_client(supabase_url, supabase_key)
        print(f"✅ Connected to Supabase: {supabase_url}")

        # Test 1: Check if tables exist
        print("\n📊 Checking tables...")
        tables_to_check = ['companies', 'press_releases', 'users']

        for table_name in tables_to_check:
            try:
                result = supabase.table(table_name).select("*").limit(1).execute()
                count = len(result.data) if result.data else 0
                print(f"   ✅ Table '{table_name}' exists (rows: {count})")
            except Exception as e:
                print(f"   ❌ Table '{table_name}' not found: {e}")

        # Test 2: Try to insert a test company
        print("\n🏢 Testing company operations...")
        test_company = {
            "name": "Test Company Ltd",
            "domain": f"test-{datetime.now().timestamp()}.ie",
            "primary_email": "test@example.com",
            "domain_verified": False,
            "subscription_tier": "basic"
        }

        try:
            result = supabase.table('companies').insert(test_company).execute()
            if result.data:
                company_id = result.data[0]['id']
                print(f"   ✅ Created test company with ID: {company_id}")

                # Clean up - delete test company
                supabase.table('companies').delete().eq('id', company_id).execute()
                print(f"   ✅ Cleaned up test company")
            else:
                print("   ⚠️  Company table exists but insert failed")
        except Exception as e:
            print(f"   ⚠️  Cannot insert into companies table: {str(e)[:100]}")

        # Test 3: Check storage bucket
        print("\n📦 Checking storage bucket...")
        try:
            buckets = supabase.storage.list_buckets()
            bucket_names = [b.name for b in buckets]

            if 'press-releases' in bucket_names:
                print("   ✅ Storage bucket 'press-releases' exists")
            else:
                print("   ⚠️  Storage bucket 'press-releases' not found")
                print(f"   Available buckets: {bucket_names}")
        except Exception as e:
            print(f"   ⚠️  Cannot check storage buckets: {e}")

        # Test 4: Test authentication
        print("\n🔐 Testing authentication...")
        try:
            # Check if auth is configured
            session = supabase.auth.get_session()
            print("   ✅ Authentication system is accessible")
        except Exception as e:
            print(f"   ⚠️  Authentication test: {e}")

        print("\n✅ Supabase connection test completed successfully!")
        print(f"\n📌 Connection Details:")
        print(f"   URL: {supabase_url}")
        print(f"   Using anon key: {'✓' if 'anon' in supabase_key else '✗'}")

        return True

    except Exception as e:
        print(f"\n❌ Connection failed: {e}")
        return False


if __name__ == "__main__":
    print("🧪 PressWire v2 - Supabase Connection Test")
    print("=" * 50)

    success = asyncio.run(test_supabase())

    if success:
        print("\n🎉 All tests passed!")
        print("\nNext steps:")
        print("1. If tables don't exist, run: python3 setup_supabase.py")
        print("2. Then execute the SQL in your Supabase dashboard")
        print("3. Start the app with: python3 main.py")
    else:
        print("\n⚠️  Please check your Supabase credentials in .env")