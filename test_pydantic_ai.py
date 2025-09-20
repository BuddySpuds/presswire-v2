#!/usr/bin/env python3
"""Test script to verify PydanticAI v1.0.10 setup"""

import asyncio
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic import BaseModel, Field
from typing import List

# Load environment variables
load_dotenv()


class TestOutput(BaseModel):
    """Simple test output"""
    headline: str = Field(..., description="A test headline")
    summary: str = Field(..., description="A brief summary")
    keywords: List[str] = Field(..., description="3-5 keywords")


async def test_pydantic_ai():
    """Test PydanticAI with a simple agent"""

    # Try to configure model based on available API keys
    api_key = None
    model_name = None
    base_url = None

    if os.getenv("OPENAI_API_KEY"):
        from pydantic_ai.models.openai import OpenAIModel
        print("✅ Using OpenAI API")
        model = OpenAIModel(
            "gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    elif os.getenv("OPENROUTER_API_KEY"):
        from pydantic_ai.models.openai import OpenAIModel
        print("✅ Using OpenRouter API")
        model = OpenAIModel(
            os.getenv("PYDANTIC_AI_MODEL", "gpt-4o-mini"),
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
    elif os.getenv("ANTHROPIC_API_KEY"):
        from pydantic_ai.models.anthropic import AnthropicModel
        print("✅ Using Anthropic API")
        model = AnthropicModel(
            "claude-3-5-haiku-latest",
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
    else:
        print("❌ No API key found! Please set one of:")
        print("   - OPENAI_API_KEY")
        print("   - OPENROUTER_API_KEY")
        print("   - ANTHROPIC_API_KEY")
        return False

    # Create a simple test agent
    agent = Agent(
        model=model,
        result_type=TestOutput,
        system_prompt="You are a helpful assistant that creates test content."
    )

    try:
        # Run a test query
        print("\n📝 Testing PydanticAI agent...")
        result = await agent.run(
            "Create a test press release headline and summary about a new Irish tech startup launching an AI product."
        )

        print("\n✨ Result:")
        print(f"Headline: {result.data.headline}")
        print(f"Summary: {result.data.summary}")
        print(f"Keywords: {', '.join(result.data.keywords)}")

        print("\n✅ PydanticAI v1.0.10 is working correctly!")
        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


if __name__ == "__main__":
    print("🧪 Testing PydanticAI v1.0.10 Setup")
    print("=" * 50)

    success = asyncio.run(test_pydantic_ai())

    if success:
        print("\n🎉 All tests passed! Your PydanticAI setup is ready.")
    else:
        print("\n⚠️  Please check your API keys in the .env file")