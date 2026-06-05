# Quarto Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the pyworkflow HTML website to a Quarto project where each page is a `.qmd` (Markdown) file, deployable to GitHub Pages with `quarto publish gh-pages`.

**Architecture:** Each HTML page becomes a `.qmd` file at the repo root. A single `_quarto.yml` controls site config, navigation, and theme. The old HTML/CSS files are kept as permanent reference and are never deleted.

**Tech Stack:** Quarto v1.9.38 (installed globally), Markdown (.qmd format), GitHub Pages

---

## File Map

| Create | Source |
|--------|--------|
| `_quarto.yml` | New — site config |
| `index.qmd` | `index.html` |
| `tools.qmd` | `tools.html` |
| `workflow.qmd` | `workflow.html` |
| `ides.qmd` | `ides.html` |
| `ide-vscode.qmd` | `ide-vscode.html` |
| `ide-pycharm.qmd` | `ide-pycharm.html` |
| `ide-cursor.qmd` | `ide-cursor.html` |
| `claude-power.qmd` | `claude-power.html` |
| `start.qmd` | `start.html` |
| `level2.qmd` | `level2.md` (already markdown) |
| `stacks.qmd` | `stacks.html` |
| `level3.qmd` | New — placeholder |

| Modify | Purpose |
|--------|---------|
| `.gitignore` | Exclude Quarto build output |

---

## Task 1: Initialize Quarto Project

**Files:**
- Create: `_quarto.yml`
- Modify: `.gitignore` (create if absent)

- [ ] **Step 1: Create `_quarto.yml`**

  Create `_quarto.yml` at the repo root with this exact content:

  ```yaml
  project:
    type: website

  website:
    title: "PyWorkflow"
    navbar:
      left:
        - href: index.qmd
          text: Overview
        - href: tools.qmd
          text: The Tools
        - href: workflow.qmd
          text: How It Connects
        - text: IDEs
          menu:
            - href: ides.qmd
              text: IDE Overview
            - href: ide-vscode.qmd
              text: VS Code
            - href: ide-pycharm.qmd
              text: PyCharm
            - href: ide-cursor.qmd
              text: Cursor
        - href: claude-power.qmd
          text: Claude Advanced
        - href: stacks.qmd
          text: Choose Your Stack
        - href: start.qmd
          text: Get Started
        - text: Levels
          menu:
            - href: level2.qmd
              text: Level 2
            - href: level3.qmd
              text: Level 3+

  format:
    html:
      theme: cosmo
  ```

- [ ] **Step 2: Update `.gitignore`**

  Add these lines to `.gitignore` (create the file if it doesn't exist):

  ```
  /_site
  /.quarto
  ```

- [ ] **Step 3: Run quarto check**

  ```
  quarto check
  ```

  Expected: No errors. Warnings about missing `.qmd` files are fine at this stage.

- [ ] **Step 4: Commit**

  ```
  git add _quarto.yml .gitignore
  git commit -m "feat: initialize Quarto project with nav config"
  ```

---

## Task 2: Create index.qmd

**Files:**
- Read: `index.html`
- Create: `index.qmd`

- [ ] **Step 1: Read source**

  Read `index.html` in full. The page has these main sections:
  - Hero: title, subtitle, two CTA links
  - "The core idea" — workflow strip (Organize → Write → Test → Share → Deploy)
  - "Five categories" — IDE, AI Assistant, venv, Version Control, Package Management
  - "Three questions" — workflow strip
  - "What level are you at?" — Levels 0–1, 2, 3, 4, 5 descriptions
  - Quote callout: "The tools change. The workflow doesn't."
  - Quick nav cards: The Tools, How It Connects, Get Started

- [ ] **Step 2: Write `index.qmd`**

  Create `index.qmd` with this structure (fill in the actual text from the HTML):

  ```markdown
  ---
  title: "Python & AI — The Modern Workflow"
  ---

  ## How code is actually written, shared, and built.

  [intro paragraph from hero]

  → [Explore the tools](tools.qmd) · [See how they connect](workflow.qmd)

  ---

  ## The core idea

  Before the details, here's the whole picture.

  [workflow strip as a markdown list or table:
  Organize (Env + packages) → Write (IDE + AI) → Test (Run + debug) → Share (Git + GitHub) → Deploy (Ship + iterate)]

  ---

  ## Every tool fits into one of these roles.

  [intro paragraph]

  **01 — The Editor / IDE**
  [description]
  *Examples: VS Code · PyCharm · Cursor*

  **02 — The AI Assistant**
  [description]
  *Examples: Claude · GitHub Copilot · ChatGPT · JetBrains AI*

  **03 — Python Environment (venv)**
  [description]
  *Examples: venv · conda · uv*

  **04 — Version Control**
  [description]
  *Examples: Git · GitHub · GitLab · Bitbucket*

  **05 — Package Management**
  [description]
  *Examples: pip · conda · uv*

  ---

  ## What level are you at?

  [intro paragraph]

  **Level 0–1: Browser chat + copy-paste**
  [description]

  **Level 2: AI in your editor**
  [description] → [Level 2: AI in Your Editor](level2.qmd)

  **Level 3: Dedicated coding agents**
  [description] → [Claude Advanced](claude-power.qmd)

  **Level 4: Connected agents**
  [description]

  **Level 5: Fully autonomous runs**
  [description]

  ---

  > "The tools change. The workflow doesn't."

  [supporting paragraph]

  → [See the full workflow](workflow.qmd)

  ---

  ## Where do you want to start?

  - [The Tools](tools.qmd) — Deep dives into every major tool category
  - [How It Connects](workflow.qmd) — See how the tools map to each workflow step
  - [Get Started](start.qmd) — Step-by-step setup guides
  ```

  Replace all `[bracketed placeholders]` with the actual text from `index.html`. Do not invent content — copy it faithfully.

- [ ] **Step 3: Run quarto check**

  ```
  quarto check
  ```

  Expected: No errors related to `index.qmd`.

- [ ] **Step 4: Commit**

  ```
  git add index.qmd
  git commit -m "feat: add index.qmd from index.html"
  ```

---

## Task 3: Create tools.qmd

**Files:**
- Read: `tools.html`
- Create: `tools.qmd`

- [ ] **Step 1: Read `tools.html` in full**

- [ ] **Step 2: Write `tools.qmd`**

  Create `tools.qmd` with YAML frontmatter and markdown body. Rules:
  - Section headings from `<h2>` and `<h3>` tags → `##` and `###`
  - Paragraphs → plain text
  - Lists → `- item`
  - Internal links: convert `href="page.html"` → `href="page.qmd"` (e.g. `[VS Code](ide-vscode.qmd)`)
  - Strip all HTML tags, class names, inline styles, icon divs, and decorative elements
  - Preserve all actual content text

  ```markdown
  ---
  title: "The Tools"
  ---

  [extracted content]
  ```

- [ ] **Step 3: Commit**

  ```
  git add tools.qmd
  git commit -m "feat: add tools.qmd from tools.html"
  ```

---

## Task 4: Create workflow.qmd

**Files:**
- Read: `workflow.html`
- Create: `workflow.qmd`

- [ ] **Step 1: Read `workflow.html` in full**

- [ ] **Step 2: Write `workflow.qmd`**

  Same extraction rules as Task 3. Frontmatter:

  ```markdown
  ---
  title: "How It Connects"
  ---
  ```

- [ ] **Step 3: Commit**

  ```
  git add workflow.qmd
  git commit -m "feat: add workflow.qmd from workflow.html"
  ```

---

## Task 5: Create ides.qmd

**Files:**
- Read: `ides.html`
- Create: `ides.qmd`

- [ ] **Step 1: Read `ides.html` in full**

  The page has: intro, six capability cards (inline autocomplete, chat panel, inline editing, agentic/multi-file, code explanation, test & doc generation), and three IDE picker cards linking to vscode/pycharm/cursor.

- [ ] **Step 2: Write `ides.qmd`**

  ```markdown
  ---
  title: "IDEs & AI Integration"
  ---

  [extracted content — capability cards become ### subsections, IDE picker cards become links]
  ```

- [ ] **Step 3: Commit**

  ```
  git add ides.qmd
  git commit -m "feat: add ides.qmd from ides.html"
  ```

---

## Task 6: Create ide-vscode.qmd

**Files:**
- Read: `ide-vscode.html`
- Create: `ide-vscode.qmd`

- [ ] **Step 1: Read `ide-vscode.html` in full**

- [ ] **Step 2: Write `ide-vscode.qmd`**

  ```markdown
  ---
  title: "VS Code"
  ---

  [extracted content]
  ```

  Same extraction rules as Task 3.

- [ ] **Step 3: Commit**

  ```
  git add ide-vscode.qmd
  git commit -m "feat: add ide-vscode.qmd from ide-vscode.html"
  ```

---

## Task 7: Create ide-pycharm.qmd

**Files:**
- Read: `ide-pycharm.html`
- Create: `ide-pycharm.qmd`

- [ ] **Step 1: Read `ide-pycharm.html` in full**

- [ ] **Step 2: Write `ide-pycharm.qmd`**

  ```markdown
  ---
  title: "PyCharm"
  ---

  [extracted content]
  ```

- [ ] **Step 3: Commit**

  ```
  git add ide-pycharm.qmd
  git commit -m "feat: add ide-pycharm.qmd from ide-pycharm.html"
  ```

---

## Task 8: Create ide-cursor.qmd

**Files:**
- Read: `ide-cursor.html`
- Create: `ide-cursor.qmd`

- [ ] **Step 1: Read `ide-cursor.html` in full**

- [ ] **Step 2: Write `ide-cursor.qmd`**

  ```markdown
  ---
  title: "Cursor"
  ---

  [extracted content]
  ```

- [ ] **Step 3: Commit**

  ```
  git add ide-cursor.qmd
  git commit -m "feat: add ide-cursor.qmd from ide-cursor.html"
  ```

---

## Task 9: Create claude-power.qmd

**Files:**
- Read: `claude-power.html`
- Create: `claude-power.qmd`

- [ ] **Step 1: Read `claude-power.html` in full**

- [ ] **Step 2: Write `claude-power.qmd`**

  ```markdown
  ---
  title: "Claude Advanced"
  ---

  [extracted content]
  ```

- [ ] **Step 3: Commit**

  ```
  git add claude-power.qmd
  git commit -m "feat: add claude-power.qmd from claude-power.html"
  ```

---

## Task 10: Create start.qmd

**Files:**
- Read: `start.html`
- Create: `start.qmd`

- [ ] **Step 1: Read `start.html` in full**

  The page has: hero with table of contents, OS toggle (Windows/Mac), 5-step walkthrough (Organize, Install, Write, Test, Share), core development loop, and a Level hub with cards for Levels 2, 3, 4.

- [ ] **Step 2: Write `start.qmd`**

  The OS toggle (Windows/Mac) is interactive HTML. In the `.qmd`, present both sets of instructions side by side under clearly labeled subsections:

  ```markdown
  ---
  title: "Get Started"
  ---

  [hero intro]

  ## The 5-step setup

  ### Step 1: Organize

  #### Windows
  [windows instructions]

  #### Mac
  [mac instructions]

  [continue for each step...]

  ## The core development loop
  [extracted content]

  ## What's next?
  [level hub content as links]
  ```

- [ ] **Step 3: Commit**

  ```
  git add start.qmd
  git commit -m "feat: add start.qmd from start.html"
  ```

---

## Task 11: Create level2.qmd

**Files:**
- Read: `level2.md` (already markdown — this is the source of truth, not the HTML)
- Create: `level2.qmd`

- [ ] **Step 1: Read `level2.md` in full**

- [ ] **Step 2: Write `level2.qmd`**

  The `.md` file is already clean markdown. Copy its content directly and add a YAML frontmatter block at the top:

  ```markdown
  ---
  title: "Level 2: AI in Your Editor"
  ---

  [paste full content of level2.md here, starting from the first heading after the # title line]
  ```

  Do not duplicate the `# Level 2: AI in Your Editor` h1 — the frontmatter `title:` field renders it.

- [ ] **Step 3: Commit**

  ```
  git add level2.qmd
  git commit -m "feat: add level2.qmd from level2.md"
  ```

---

## Task 12: Create stacks.qmd

**Files:**
- Read: `stacks.html`
- Create: `stacks.qmd`

- [ ] **Step 1: Read `stacks.html` in full**

- [ ] **Step 2: Write `stacks.qmd`**

  ```markdown
  ---
  title: "Choose Your Stack"
  ---

  [extracted content]
  ```

- [ ] **Step 3: Commit**

  ```
  git add stacks.qmd
  git commit -m "feat: add stacks.qmd from stacks.html"
  ```

---

## Task 13: Create level3.qmd Placeholder

**Files:**
- Create: `level3.qmd`

- [ ] **Step 1: Write `level3.qmd`**

  ```markdown
  ---
  title: "Level 3+: Dedicated Coding Agents"
  ---

  *This section is coming soon.*
  ```

- [ ] **Step 2: Commit**

  ```
  git add level3.qmd
  git commit -m "feat: add level3.qmd placeholder"
  ```

---

## Task 14: Preview and Verify

- [ ] **Step 1: Run quarto check**

  ```
  quarto check
  ```

  Expected: No errors. All `.qmd` files listed as valid.

- [ ] **Step 2: Run quarto preview**

  ```
  quarto preview
  ```

  This opens the site in your browser at `http://localhost:XXXX`. Verify:
  - Every nav link resolves to a page (no 404s)
  - All internal links between pages work (hover over links and verify URLs look correct)
  - Content on each page matches the source HTML page

- [ ] **Step 3: Stop preview**

  Press `Ctrl+C` in the terminal to stop the preview server.

- [ ] **Step 4: Commit any fixes found during preview**

  ```
  git add <changed files>
  git commit -m "fix: correct links and content after preview review"
  ```

---

## Task 15: Deploy to GitHub Pages

- [ ] **Step 1: Publish to GitHub Pages**

  ```
  quarto publish gh-pages
  ```

  When prompted "Publish site to [ncox02/pyworkflow] using gh-pages? (Y/n)" — enter `Y`.

  This command:
  - Builds the site into `_site/`
  - Pushes `_site/` to the `gh-pages` branch on GitHub
  - Your site will be live at `https://ncox02.github.io/pyworkflow/`

- [ ] **Step 2: Verify live site**

  Open `https://ncox02.github.io/pyworkflow/` in a browser. Confirm it loads and navigation works.

- [ ] **Step 3: Commit final state**

  ```
  git add -A
  git commit -m "feat: complete Quarto migration, all pages live"
  git push origin main
  ```
