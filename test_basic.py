#!/usr/bin/env python3
"""Ultra-basic CI test - just verify Python works"""

print("Starting basic CI test...")

# Test 1: Python is working
print("✅ Python interpreter is working")

# Test 2: Can do basic operations
result = 2 + 2
assert result == 4
print("✅ Basic math works")

# Test 3: Can import standard library
import sys
import os
print("✅ Standard library imports work")

# Test 4: Print Python version
print(f"✅ Python version: {sys.version}")

# Test 5: Check current directory
print(f"✅ Current directory: {os.getcwd()}")

# Success
print("\n✅ All basic tests passed!")
print("CI test completed successfully")