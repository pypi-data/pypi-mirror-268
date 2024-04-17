import os
import unittest

import pytest
import pytest_asyncio
from promptflow.connections import OpenAIConnection

from tool_use.tools.openai_tool_use import openai_tool_use


@pytest_asyncio.fixture
def load_env():
    from dotenv import load_dotenv

    load_dotenv()


@pytest_asyncio.fixture
def my_connection(load_env) -> OpenAIConnection:
    return OpenAIConnection(
        api_key=os.environ.get("OPENAI_API_KEY"),
        organization=os.environ.get("OPENAI_ORG_ID"),
    )


@pytest.mark.asyncio(scope="class")
class TestTool:
    async def test_openai_tool_use(self, my_connection):
        prompt = ""
        with open(os.path.join(os.path.dirname(__file__), "openai_prompt.jinja2")) as f:
            prompt = f.read()
        result = await openai_tool_use(
            connection=my_connection,
            prompt=prompt,
            model="gpt-4-0125-preview",
        )
        assert result is not None
        print(result)


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
