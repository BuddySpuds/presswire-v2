-- PressWire v2 Database Schema for Supabase
-- Run this in your Supabase SQL Editor

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

-- Create storage bucket for press releases (if not exists)
INSERT INTO storage.buckets (id, name, public)
VALUES ('press-releases', 'press-releases', true)
ON CONFLICT (id) DO NOTHING;