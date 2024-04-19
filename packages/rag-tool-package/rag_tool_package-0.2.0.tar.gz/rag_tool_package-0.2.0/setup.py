from setuptools import find_packages, setup

PACKAGE_NAME = "rag_tool_package"

setup(
    name=PACKAGE_NAME,
    version="0.2.0",
    description="This is my tools package. Rag tool for now. Initial version with dynamic lists",
    packages=find_packages(),
    entry_points={
        "package_tools": ["rag_tool = rag_tool_package.tools.utils:list_package_tools"],
    },
    include_package_data=True,   # This line tells setuptools to include files from MANIFEST.in
)