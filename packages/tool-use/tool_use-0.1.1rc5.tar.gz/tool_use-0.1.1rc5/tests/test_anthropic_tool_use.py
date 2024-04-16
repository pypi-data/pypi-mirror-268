import os
import unittest
from ast import literal_eval
from typing import Tuple

import pytest
import pytest_asyncio

from tool_use.tools.anthropic_tool_use import AnthropicConnection, anthropic_tool_use

# Run the unit tests
if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    unittest.main()


@pytest_asyncio.fixture
def load_env():
    from dotenv import load_dotenv

    load_dotenv()


@pytest_asyncio.fixture
def my_connection(load_env) -> AnthropicConnection:
    return AnthropicConnection(
        secrets=dict(
            api_key=os.environ.get("ANTHROPIC_API_KEY"),
            api_type="anthropic",
            api_base="https://api.anthropic.com",
            client_key=None,
        ),
    )


@pytest_asyncio.fixture
def my_custom_connection(load_env) -> AnthropicConnection:
    return AnthropicConnection(
        secrets=dict(
            api_key=os.environ.get("ANTHROPIC_API_KEY"),
            api_type="anthropic",
            api_base=os.environ.get("ANTHROPIC_API_BASE"),
        ),
    )


def load_tool_prompts() -> Tuple[str, dict]:
    prompt = ""
    with open(
        os.path.join(os.path.dirname(__file__), "claude_tool_prompt.jinja2")
    ) as f:
        prompt = f.read()
    sample_tool = {}
    with open(os.path.join(os.path.dirname(__file__), "claude_tool.jinja2")) as f:
        sample_tool = f.read()
        sample_tool = literal_eval(sample_tool)
    return prompt, sample_tool


def load_prompt() -> str:
    prompt = ""
    with open(os.path.join(os.path.dirname(__file__), "claude_prompt.jinja2")) as f:
        prompt = f.read()
    return prompt


@pytest.mark.asyncio(scope="class")
class TestTool:
    async def test_anthropic_tool_use(self, my_connection):
        prompt, sample_tool = load_tool_prompts()
        result = await anthropic_tool_use(
            connection=my_connection,
            prompt=prompt,
            model="claude-3-haiku-20240307",
            max_tokens=500,
            tools=[sample_tool],
        )
        assert result is not None
        print(result)

    async def test_anthropic(self, my_connection):
        prompt = load_prompt()
        result = await anthropic_tool_use(
            connection=my_connection,
            prompt=prompt,
            model="claude-3-haiku-20240307",
            max_tokens=500,
            question="I want to make a recipe with chicken.",
        )
        assert result is not None
        print(result)

    async def test_anthropic_stream(self, my_connection):
        prompt = load_prompt()
        result = await anthropic_tool_use(
            connection=my_connection,
            prompt=prompt,
            model="claude-3-haiku-20240307",
            max_tokens=500,
            stream=True,
            question="I want to make a recipe with chicken.",
        )
        chunk_count = 0
        total_result = ""
        async for chunk in result:
            chunk_count += 1
            total_result += chunk
        print(chunk_count)
        print(total_result)

    async def test_anthropic_tool_use_2(self, my_custom_connection):
        prompt, sample_tool = load_tool_prompts()
        result = await anthropic_tool_use(
            connection=my_custom_connection,
            prompt=prompt,
            model="claude-3-haiku-20240307",
            max_tokens=500,
            tools=[sample_tool],
        )
        assert result is not None
        print(result)

    async def test_anthropic_2(self, my_custom_connection):
        prompt = load_prompt()
        result = await anthropic_tool_use(
            connection=my_custom_connection,
            prompt=prompt,
            model="claude-3-haiku-20240307",
            max_tokens=500,
            question="I want to make a recipe with chicken.",
        )
        assert result is not None
        print(result)

    async def test_anthropic_stream_2(self, my_custom_connection):
        prompt = load_prompt()
        result = await anthropic_tool_use(
            connection=my_custom_connection,
            prompt=prompt,
            model="claude-3-haiku-20240307",
            max_tokens=500,
            stream=True,
            question="I want to make a recipe with chicken.",
        )
        chunk_count = 0
        total_result = ""
        async for chunk in result:
            chunk_count += 1
            total_result += chunk
        print(chunk_count)
        print(total_result)


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
