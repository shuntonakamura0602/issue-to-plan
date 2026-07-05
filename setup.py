from setuptools import setup

setup(
    name="issue-to-plan",
    version="0.1.0",
    description="A tiny CLI that turns rough GitHub issues into implementation plan markdown.",
    py_modules=["issue_to_plan"],
    entry_points={
        "console_scripts": [
            "issue-to-plan=issue_to_plan:main",
        ],
    },
)