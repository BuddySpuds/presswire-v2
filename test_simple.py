#!/usr/bin/env python3
"""Minimal CI test - just check basic Python package imports"""

import sys

print("🧪 Running minimal CI tests")
print("=" * 50)

# Test 1: Basic imports
print("\nTest 1: Testing basic package imports...")
try:
    import fastapi
    print("✅ FastAPI imported")
except ImportError:
    print("❌ FastAPI not installed")
    sys.exit(1)

try:
    import pydantic
    print("✅ Pydantic imported")
except ImportError:
    print("❌ Pydantic not installed")
    sys.exit(1)

try:
    import sqlalchemy
    print("✅ SQLAlchemy imported")
except ImportError:
    print("❌ SQLAlchemy not installed")
    sys.exit(1)

# Test 2: Check if main files exist
print("\nTest 2: Checking project structure...")
import os

required_files = [
    'main.py',
    'requirements.txt',
    'Dockerfile',
    'docker-compose.yml',
]

for file in required_files:
    if os.path.exists(file):
        print(f"✅ {file} exists")
    else:
        print(f"❌ {file} missing")
        sys.exit(1)

# Test 3: Check app directory
print("\nTest 3: Checking app directory...")
required_dirs = [
    'app',
    'app/core',
    'app/api',
    'app/models',
    'app/agents',
]

for dir in required_dirs:
    if os.path.isdir(dir):
        print(f"✅ {dir}/ exists")
    else:
        print(f"❌ {dir}/ missing")
        sys.exit(1)

print("\n" + "=" * 50)
print("✅ All minimal CI tests passed!")
print("=" * 50)
sys.exit(0)