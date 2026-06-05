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

Old HTML/CSS files remain as permanent reference. They are not deleted at any stage.

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
5. Review each `.qmd` file individually — content and structural changes applied per page
6. Review all pages together as a whole — evaluate flow and consistency across the site
7. Repeat steps 5–6 iteratively as changes continue over time
8. Deploy with `quarto publish gh-pages`

## Content Update Process

Updates are iterative and ongoing, not one-time. The cycle is:
1. Review a page's `.qmd` individually, apply changes
2. Once all pages reviewed, evaluate the site as a whole
3. Repeat as needed

Pages with known pending work:
- `start.qmd` — guided walkthrough, content and structural notes
- `level2.qmd` — content and structural changes
- `level3.qmd` — new page, does not exist yet

## Out of Scope (for now)

- Custom styling / visual design (addressed after content is stable)
- Interactive components
- Any backend or dynamic functionality
