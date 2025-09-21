#!/usr/bin/env python3
"""Simple CI tests that don't require a running application"""

import sys
import importlib

def test_imports():
    """Test that all required modules can be imported"""
    required_modules = [
        'fastapi',
        'pydantic',
        'sqlalchemy',
        'supabase',
    ]

    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module} imported successfully")
        except ImportError as e:
            print(f"❌ Failed to import {module}: {e}")
            return False
    return True

def test_app_structure():
    """Test that the app structure is correct"""
    try:
        # Test main app import
        from main import app
        print("✅ Main app imported successfully")

        # Test core config
        from app.core.config import get_settings
        settings = get_settings()
        print("✅ Settings loaded successfully")

        # Test database module
        from app.core.database import Base
        print("✅ Database module imported successfully")

        return True
    except Exception as e:
        print(f"❌ App structure test failed: {e}")
        return False

def test_api_routes():
    """Test that API routes are defined"""
    try:
        from main import app
        routes = [route.path for route in app.routes]

        required_routes = ["/", "/health", "/api"]
        for route in required_routes:
            if route in routes:
                print(f"✅ Route {route} found")
            else:
                print(f"❌ Route {route} missing")
                return False
        return True
    except Exception as e:
        print(f"❌ API routes test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Running CI Tests")
    print("=" * 50)

    all_passed = True

    # Run tests
    tests = [
        ("Imports", test_imports),
        ("App Structure", test_app_structure),
        ("API Routes", test_api_routes),
    ]

    for test_name, test_func in tests:
        print(f"\nTesting {test_name}...")
        if not test_func():
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("✅ All CI tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed")
        sys.exit(1)