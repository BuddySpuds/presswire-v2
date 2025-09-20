"""Press Release database models"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class PressRelease(Base):
    __tablename__ = "press_releases"

    id = Column(Integer, primary_key=True, index=True)

    # Company Information
    company_name = Column(String(255), nullable=False, index=True)
    company_domain = Column(String(255), nullable=False, index=True)
    company_email = Column(String(255), nullable=False)
    company_registration = Column(String(50))  # CRO number

    # Press Release Content
    headline = Column(String(500), nullable=False)
    subheadline = Column(String(500))
    body = Column(Text, nullable=False)
    boilerplate = Column(Text)

    # SEO Metadata
    seo_title = Column(String(255))
    meta_description = Column(String(500))
    keywords = Column(JSON)  # Array of keywords
    schema_markup = Column(JSON)  # Structured data

    # Media
    featured_image = Column(String(500))
    image_alt_text = Column(String(255))
    additional_images = Column(JSON)  # Array of image URLs

    # Contact Information
    contact_name = Column(String(255))
    contact_email = Column(String(255))
    contact_phone = Column(String(50))

    # Publishing Details
    slug = Column(String(255), unique=True, index=True)
    status = Column(String(50), default="draft")  # draft, pending, published, archived
    publish_date = Column(DateTime(timezone=True))
    embargo_date = Column(DateTime(timezone=True))

    # Pricing & Package
    package_tier = Column(String(50))  # basic, professional, premium
    price_paid = Column(Float)
    stripe_payment_id = Column(String(255))

    # Verification
    domain_verified = Column(Boolean, default=False)
    cro_verified = Column(Boolean, default=False)
    moderation_status = Column(String(50))  # pending, approved, rejected
    moderation_notes = Column(Text)

    # Analytics
    view_count = Column(Integer, default=0)
    unique_visitors = Column(Integer, default=0)
    social_shares = Column(JSON)  # Platform-specific counts

    # AI Enhancement
    ai_enhanced = Column(Boolean, default=False)
    ai_suggestions = Column(JSON)  # Stored suggestions
    ai_score = Column(Float)  # Content quality score

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<PressRelease {self.headline}>"


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    domain = Column(String(255), unique=True, nullable=False, index=True)
    registration_number = Column(String(50), unique=True)  # CRO number

    # Verification
    domain_verified = Column(Boolean, default=False)
    cro_verified = Column(Boolean, default=False)
    verification_date = Column(DateTime(timezone=True))

    # Company Details from CRO
    company_type = Column(String(100))
    incorporation_date = Column(DateTime)
    status = Column(String(50))  # active, dissolved, etc.
    address = Column(JSON)

    # Contact
    primary_email = Column(String(255))
    billing_email = Column(String(255))

    # Subscription
    subscription_tier = Column(String(50))
    subscription_status = Column(String(50))
    credits_remaining = Column(Integer, default=0)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Company {self.name}>"