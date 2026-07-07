# issue-to-plan

A tiny CLI that turns rough GitHub issues into implementation plan markdown.

This is useful when you want to start coding with ChatGPT, Claude, or any AI coding assistant, but your issue is still too vague.

## Usage

Generate a plan from a command line argument:

```bash
python3 issue_to_plan.py "Add dark mode to settings page"
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

## Output

Normal mode generates:

- Goal
- Assumptions
- Implementation steps
- Files to inspect
- Questions before implementation
- Test checklist
- Suggested commit message

`--ai-prompt` mode generates a prompt you can paste into ChatGPT, Claude, Cursor, Claude Code, or another coding assistant. The prompt asks the assistant to:

- Act as an experienced software engineer
- Clarify the goal
- List assumptions
- Identify files to inspect
- Break the work into small steps
- Suggest a test checklist
- Avoid unnecessary refactoring
- Return the result in Markdown

## Why

Starting is often the hardest part of development.

This tool helps convert vague tasks into a concrete first step.

## Roadmap

- [ ] Support GitHub issue URLs
- [ ] Add custom templates
- [ ] Generate PR descriptions
- [x] Generate AI coding prompts
- [ ] Add npm package version
