#!/usr/bin/env python3
"""Set up Supabase database schema for PressWire v2"""

import os
import asyncio
from dotenv import load_dotenv
from supabase import create_client
import sys

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
    sys.exit(1)

# SQL to create tables
SQL_CREATE_TABLES = """
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Companies table
CREATE TABLE IF NOT EXISTS companies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255) UNIQUE NOT NULL,
    registration_number VARCHAR(50) UNIQUE,

    -- Verification
    domain_verified BOOLEAN DEFAULT FALSE,
    cro_verified BOOLEAN DEFAULT FALSE,
    verification_date TIMESTAMPTZ,

    -- Company Details from CRO
    company_type VARCHAR(100),
    incorporation_date DATE,
    status VARCHAR(50),
    address JSONB,

    -- Contact
    primary_email VARCHAR(255),
    billing_email VARCHAR(255),

    -- Subscription
    subscription_tier VARCHAR(50),
    subscription_status VARCHAR(50),
    credits_remaining INTEGER DEFAULT 0,

    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Press Releases table
CREATE TABLE IF NOT EXISTS press_releases (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Company Information
    company_id UUID REFERENCES companies(id),
    company_name VARCHAR(255) NOT NULL,
    company_domain VARCHAR(255) NOT NULL,
    company_email VARCHAR(255) NOT NULL,
    company_registration VARCHAR(50),

    -- Press Release Content
    headline VARCHAR(500) NOT NULL,
    subheadline VARCHAR(500),
    body TEXT NOT NULL,
    boilerplate TEXT,

    -- SEO Metadata
    seo_title VARCHAR(255),
    meta_description VARCHAR(500),
    keywords JSONB,
    schema_markup JSONB,

    -- Media
    featured_image VARCHAR(500),
    image_alt_text VARCHAR(255),
    additional_images JSONB,

    -- Contact Information
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(50),

    -- Publishing Details
    slug VARCHAR(255) UNIQUE,
    status VARCHAR(50) DEFAULT 'draft',
    publish_date TIMESTAMPTZ,
    embargo_date TIMESTAMPTZ,

    -- Pricing & Package
    package_tier VARCHAR(50),
    price_paid NUMERIC(10, 2),
    stripe_payment_id VARCHAR(255),

    -- Verification
    domain_verified BOOLEAN DEFAULT FALSE,
    cro_verified BOOLEAN DEFAULT FALSE,
    moderation_status VARCHAR(50),
    moderation_notes TEXT,

    -- Analytics
    view_count INTEGER DEFAULT 0,
    unique_visitors INTEGER DEFAULT 0,
    social_shares JSONB,

    -- AI Enhancement
    ai_enhanced BOOLEAN DEFAULT FALSE,
    ai_suggestions JSONB,
    ai_score NUMERIC(3, 1),

    -- Timestamps
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Users table (for admin and company accounts)
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    full_name VARCHAR(255),
    company_id UUID REFERENCES companies(id),
    role VARCHAR(50) DEFAULT 'user',
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_press_releases_company_domain ON press_releases(company_domain);
CREATE INDEX IF NOT EXISTS idx_press_releases_slug ON press_releases(slug);
CREATE INDEX IF NOT EXISTS idx_press_releases_status ON press_releases(status);
CREATE INDEX IF NOT EXISTS idx_press_releases_publish_date ON press_releases(publish_date);
CREATE INDEX IF NOT EXISTS idx_companies_domain ON companies(domain);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- Create updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply updated_at triggers
DROP TRIGGER IF EXISTS update_companies_updated_at ON companies;
CREATE TRIGGER update_companies_updated_at
BEFORE UPDATE ON companies
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_press_releases_updated_at ON press_releases;
CREATE TRIGGER update_press_releases_updated_at
BEFORE UPDATE ON press_releases
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_users_updated_at ON users;
CREATE TRIGGER update_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- Enable Row Level Security
ALTER TABLE companies ENABLE ROW LEVEL SECURITY;
ALTER TABLE press_releases ENABLE ROW LEVEL SECURITY;
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Create storage bucket for press releases
INSERT INTO storage.buckets (id, name, public)
VALUES ('press-releases', 'press-releases', true)
ON CONFLICT (id) DO NOTHING;
"""


async def setup_database():
    """Set up Supabase database schema"""
    try:
        # Create Supabase client
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Connected to Supabase")

        # Note: Supabase doesn't allow direct SQL execution through the Python client
        # You'll need to run the SQL in the Supabase dashboard SQL editor

        print("\n📋 Database Setup Instructions:")
        print("=" * 50)
        print("1. Go to your Supabase dashboard:")
        print(f"   {SUPABASE_URL}")
        print("\n2. Navigate to SQL Editor")
        print("\n3. Copy and paste the following SQL:")
        print("-" * 50)
        print(SQL_CREATE_TABLES)
        print("-" * 50)
        print("\n4. Click 'Run' to execute the SQL")

        # Test connection
        try:
            # Try to query a simple table
            result = supabase.auth.get_session()
            print("\n✅ Supabase connection test successful!")
        except Exception as e:
            print(f"\n⚠️  Connection test failed: {e}")

        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


if __name__ == "__main__":
    print("🚀 PressWire v2 - Supabase Database Setup")
    print("=" * 50)

    success = asyncio.run(setup_database())

    if success:
        print("\n✅ Setup instructions generated successfully!")
        print("\nNext steps:")
        print("1. Run the SQL in your Supabase dashboard")
        print("2. Test the connection with: python3 test_supabase.py")