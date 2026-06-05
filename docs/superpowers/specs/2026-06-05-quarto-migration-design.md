# Design: Migrate pyworkflow Website to Quarto

**Date:** 2026-06-05  
**Status:** Approved

## Goal

Replace the current flat HTML/CSS site with a Quarto website where each page is a `.qmd` file (plain Markdown). The professor or any editor can update content without touching HTML, CSS, or JavaScript.

## File Structure

```
pyworkflow/
├── _quarto.yml           ← site config: title, navigation, theme
├── index.qmd             ← home page
├── start.qmd             ← get started / guided walkthrough
├── workflow.qmd
├── ides.qmd
├── ide-vscode.qmd
├── ide-pycharm.qmd
├── ide-cursor.qmd
├── claude-power.qmd
├── tools.qmd
├── level2.qmd            ← level 2 guided walkthrough
├── stacks.qmd
├── styles.css            ← custom styling (later, optional)
└── docs/                 ← design specs and planning docs
```

Old HTML/CSS files remain untouched as reference until migration is confirmed working, then deleted.

## Tool

**Quarto v1.9.38** — installed globally via winget. Available system-wide.

## Day-to-Day Workflow

- Edit any `.qmd` file in plain Markdown
- `quarto preview` — live browser preview, auto-refreshes on save
- `quarto publish gh-pages` — one command deploys to GitHub Pages

## Migration Plan

1. Initialize Quarto project in the repo root (`_quarto.yml`)
2. Extract each HTML page's content into its corresponding `.qmd` file
3. Configure navigation in `_quarto.yml`
4. Preview locally with `quarto preview`
5. Apply content/structural notes to: `start.qmd`, `level2.qmd`, new `level3.qmd`
6. Delete old HTML/CSS files once new site is confirmed working
7. Deploy with `quarto publish gh-pages`

## Pages Needing Content/Structural Updates

- `start.qmd` — guided walkthrough notes to be applied
- `level2.qmd` — content and structural changes pending
- `level3.qmd` — new page, does not exist yet

## Out of Scope (for now)

- Custom styling / visual design
- Interactive components
- Any backend or dynamic functionality
