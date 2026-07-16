# issue-to-plan

`issue-to-plan` turns a rough GitHub issue or development task into a structured implementation plan or an AI-ready coding prompt.

## Why this project exists

Starting from a vague issue can be slow. This small Python CLI gives you a concrete first draft: either a human-readable plan template you can work from, or a prompt you can paste into a coding assistant.

## Features

- Generate a structured implementation-plan template for humans.
- Generate an AI-ready prompt for coding tools.
- Read issue text from command-line arguments or stdin.
- Write generated output to a file.
- Run with Python's standard library only.

## Installation

No external dependencies are required. The most reliable way to try the project is to run the script directly from a local checkout:

```bash
cd issue-to-plan
python3 issue_to_plan.py --version
```

The repository includes Python packaging metadata, but this README does not assume a PyPI release.

## Usage

Pass the issue or task text as an argument:

```bash
python3 issue_to_plan.py "Add dark mode to settings page"
```

Or pipe the issue text through stdin:

```bash
echo "Add dark mode to settings page" | python3 issue_to_plan.py
```

Write output to a file:

```bash
python3 issue_to_plan.py "Add dark mode to settings page" -o examples/dark-mode.md
```

Show the current version:

```bash
python3 issue_to_plan.py --version
```

## Normal mode

Normal mode generates a human-readable implementation-plan template:

```bash
python3 issue_to_plan.py "Add dark mode to settings page"
```

Short output example:

```markdown
# Implementation Plan

## Original Issue

Add dark mode to settings page

## Goal

Clarify the goal of this issue and turn it into a small, actionable implementation task.
```

See [examples/dark-mode.md](examples/dark-mode.md) and [examples/login-redirect-bug.md](examples/login-redirect-bug.md) for complete examples.

## AI prompt mode

`--ai-prompt` generates instructions that can be pasted into coding tools such as ChatGPT, Claude, Cursor, Claude Code, Codex, or GitHub Copilot:

```bash
python3 issue_to_plan.py "Add dark mode to settings page" --ai-prompt
```

Short output example:

```markdown
Act as an experienced software engineer.

Turn the following issue into a concrete implementation plan:

> Add dark mode to settings page
```

Write an AI prompt to a file:

```bash
python3 issue_to_plan.py "Add dark mode to settings page" --ai-prompt -o examples/dark-mode-ai-prompt.md
```

See [examples/dark-mode-ai-prompt.md](examples/dark-mode-ai-prompt.md) and [examples/login-redirect-bug-ai-prompt.md](examples/login-redirect-bug-ai-prompt.md) for complete examples.

## Examples

Existing generated examples:

- [Add dark mode](examples/dark-mode.md)
- [Add dark mode AI prompt](examples/dark-mode-ai-prompt.md)
- [Fix a login redirect bug](examples/login-redirect-bug.md)
- [Fix a login redirect bug AI prompt](examples/login-redirect-bug-ai-prompt.md)
- [Refactor a profile card component](examples/refactor-profile-card.md)
- [Add a password reset test case](examples/add-password-reset-test.md)

## Running tests

```bash
python3 -m unittest discover -s tests
```

## Limitations

`issue-to-plan` does not call an AI API and is not AI-powered. It currently generates deterministic templates and AI-ready prompts from the issue text you provide.

The tool does not automatically analyze repository context, inspect your codebase, fetch GitHub issue URLs, or read linked issue metadata.

## Feedback

Please open a GitHub Issue for bug reports, feature requests, installation problems, and workflow feedback.

Feedback is especially useful on whether this tool is more helpful than pasting an issue directly into an LLM.
