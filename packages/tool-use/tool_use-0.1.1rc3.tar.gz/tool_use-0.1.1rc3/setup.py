from setuptools import find_packages, setup

PACKAGE_NAME = "tool_use"

setup(
    name=PACKAGE_NAME,
    version="0.1.1rc3",
    description="Promptflow tool package for OpenAI/Anthropic",
    packages=find_packages(),
    entry_points={
        "package_tools": [
            "openai_tool_use = tool_use.tools.utils:list_package_tools",
            "anthropic_tool_use = tool_use.tools.utils:list_package_tools",
        ],
    },
    include_package_data=True,  # This line tells setuptools to include files from MANIFEST.in
)
