#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys


def generate_plan(issue: str) -> str:
    issue = issue.strip()

    return f"""# Implementation Plan

## Original Issue

{issue}

## Goal

Clarify the goal of this issue and turn it into a small, actionable implementation task.

## Assumptions

- The project already has an existing codebase.
- The issue can be implemented in small steps.
- The developer will inspect the relevant files before editing.

## Steps

1. Understand the expected behavior.
2. Find the relevant files.
3. Identify the smallest possible code change.
4. Implement the change.
5. Add or update tests if needed.
6. Manually verify the behavior.
7. Write a concise commit message.

## Files to Inspect

- Relevant components
- Related tests
- Configuration files
- Documentation

## Questions Before Implementation

- What is the current behavior?
- What is the expected behavior?
- Are there edge cases?
- Is this a bug fix, feature, or refactor?

## Test Checklist

- The main behavior works.
- Existing behavior is not broken.
- Error cases are handled.
- The implementation is simple enough.

## Suggested Commit Message

Implement: {issue[:60]}
"""


def generate_ai_prompt(issue: str) -> str:
    issue = issue.strip()

    return f"""Act as an experienced software engineer.

Turn the following issue into a concrete implementation plan:

> {issue}

Please return the result in Markdown and include:

## Goal

Clarify the goal in practical engineering terms.

## Assumptions

List reasonable assumptions, and call out anything that needs confirmation.

## Files to Inspect

Identify likely files, directories, tests, configuration, and documentation to inspect before editing.

## Implementation Steps

Break the work into small, ordered steps.

## Test Checklist

Suggest focused automated and manual checks for the change.

## Constraints

- Avoid unnecessary refactoring.
- Prefer the smallest clear change that satisfies the issue.
- Preserve existing behavior unless the issue requires changing it.
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Turn a rough GitHub issue into an implementation plan markdown."
    )

    parser.add_argument(
        "issue",
        nargs="*",
        help="Issue description. If omitted, input is read from stdin.",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Write the generated plan to a file.",
    )

    parser.add_argument(
        "--ai-prompt",
        action="store_true",
        help="Generate a pasteable prompt for an AI coding assistant.",
    )

    args = parser.parse_args()

    if args.issue:
        issue = " ".join(args.issue)
    else:
        issue = sys.stdin.read()

    if not issue.strip():
        print("Please provide an issue description.")
        print()
        print("Examples:")
        print('  python3 issue_to_plan.py "Add dark mode to settings page"')
        print('  echo "Add dark mode to settings page" | python3 issue_to_plan.py')
        return

    result = generate_ai_prompt(issue) if args.ai_prompt else generate_plan(issue)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(result, encoding="utf-8")
        if args.ai_prompt:
            print(f"Prompt written to {output_path}")
        else:
            print(f"Plan written to {output_path}")
    else:
        print(result)


if __name__ == "__main__":
    main()
