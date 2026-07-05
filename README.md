# issue-to-plan

A tiny CLI that turns rough GitHub issues into implementation plan markdown.

This is useful when you want to start coding with ChatGPT, Claude, or any AI coding assistant, but your issue is still too vague.

## Example

```bash
echo "Add dark mode to settings page" | python issue_to_plan.py
```

## Output

The tool generates:

- Goal
- Assumptions
- Implementation steps
- Files to inspect
- Questions before implementation
- Test checklist
- Suggested commit message

## Why

Starting is often the hardest part of development.

This tool helps convert vague tasks into a concrete first step.

## Roadmap

- [ ] Support GitHub issue URLs
- [ ] Add custom templates
- [ ] Generate PR descriptions
- [ ] Generate AI coding prompts
- [ ] Add npm package version