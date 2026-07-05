# Example: Add Dark Mode

## Input Issue

Add dark mode to settings page

## Generated Implementation Plan

# Implementation Plan

## Original Issue

Add dark mode to settings page

## Goal

Add a dark mode option to the settings page so users can switch between light and dark themes.

## Assumptions

- The project already has a settings page.
- The project has some existing styling system.
- The dark mode setting should be easy to find and change.
- The user's preference should be preserved after refreshing the page.

## Steps

1. Find the settings page component.
2. Check how the project currently handles styles and themes.
3. Add a dark mode toggle to the settings page.
4. Store the user's theme preference.
5. Apply dark mode styles to the application.
6. Make sure the selected theme persists after reload.
7. Test both light mode and dark mode manually.

## Files to Inspect

- Settings page component
- Global style files
- Theme configuration files
- Layout or app root component
- Existing local storage or user settings logic

## Questions Before Implementation

- Does the app already support multiple themes?
- Should the theme preference be stored locally or in the user's account?
- Should dark mode apply immediately after toggling?
- Should the system preference be used as the default?
- Are there existing design tokens or CSS variables?

## Test Checklist

- The dark mode toggle appears on the settings page.
- Switching to dark mode updates the UI immediately.
- Switching back to light mode works.
- The selected theme remains after refreshing the page.
- Text remains readable in both themes.
- Existing settings page behavior is not broken.

## Suggested Commit Message

Implement dark mode toggle on settings page

## AI Coding Prompt

You are helping me implement this GitHub issue:

"Add dark mode to settings page"

Please inspect the existing settings page, theme-related files, and global styles. Then propose the smallest safe implementation plan before editing code.

Focus on:
- Finding the existing settings page
- Understanding the current styling system
- Adding a simple dark mode toggle
- Persisting the user's preference
- Avoiding unnecessary refactors