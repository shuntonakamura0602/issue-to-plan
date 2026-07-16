# issue-to-plan

`issue-to-plan` turns vague GitHub issue text into a structured implementation plan you can start from immediately.

It is a small Python CLI for converting rough ideas like "Add dark mode to settings page" into Markdown with a goal, assumptions, implementation steps, files to inspect, questions, tests, and a suggested commit message.

Use normal mode when you want a planning document for yourself. Use `--ai-prompt` when you want a copy-pasteable prompt for AI coding tools such as ChatGPT, Claude, Cursor, Claude Code, or GitHub Copilot.

## Usage

Generate a plan from a command line argument:

```bash
python3 issue_to_plan.py "Add dark mode to settings page"
```

If installed as a package, use the CLI command:

```bash
issue-to-plan "Add dark mode to settings page"
```

Generate a plan from stdin:

```bash
echo "Add dark mode to settings page" | python3 issue_to_plan.py
```

Generate a pasteable AI prompt:

```bash
python3 issue_to_plan.py "Add dark mode to settings page" --ai-prompt
```

Write the output to a file:

```bash
python3 issue_to_plan.py "Add dark mode to settings page" -o examples/dark-mode.md
```

Write an AI prompt to a file:

```bash
python3 issue_to_plan.py "Add dark mode to settings page" --ai-prompt -o examples/dark-mode-ai-prompt.md
```

Show the installed version:

```bash
python3 issue_to_plan.py --version
```

Run the tests:

```bash
python3 -m unittest discover -s tests
```

## Examples

- [Add dark mode](examples/dark-mode.md)
- [Add dark mode AI prompt](examples/dark-mode-ai-prompt.md)
- [Fix a login redirect bug](examples/login-redirect-bug.md)
- [Fix a login redirect bug AI prompt](examples/login-redirect-bug-ai-prompt.md)
- [Refactor a profile card component](examples/refactor-profile-card.md)
- [Add a password reset test case](examples/add-password-reset-test.md)

## Modes

Normal mode generates an implementation plan for the issue:

- Goal
- Assumptions
- Implementation steps
- Files to inspect
- Questions before implementation
- Test checklist
- Suggested commit message

`--ai-prompt` mode generates a prompt you can paste into an AI coding assistant. The prompt asks the assistant to:

- Act as an experienced software engineer
- Clarify the goal
- List assumptions
- Identify files to inspect
- Break the work into small steps
- Suggest a test checklist
- Avoid unnecessary refactoring
- Return the result in Markdown

## Limitations

`issue-to-plan` does not call an AI API yet. It currently generates structured templates and AI-ready prompts from the issue text you provide.

## Why

Starting is often the hardest part of development.

This tool helps convert vague tasks into a concrete first step.

## Roadmap

- [ ] Support GitHub issue URLs
- [ ] Add custom templates
- [ ] Generate PR descriptions
- [x] Generate AI coding prompts
- [ ] Add npm package version
