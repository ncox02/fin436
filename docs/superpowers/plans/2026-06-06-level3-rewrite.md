# level3.qmd Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite level3.qmd to be concept-first and tool-agnostic through most of the page, introducing Claude Code and its seven integrations only after the reader understands the underlying concepts.

**Architecture:** Replace the existing file section-by-section. Task 1 overwrites the file with the new intro. Each subsequent task appends one section. Commit after each task. Use `git add level3.qmd` only — never `git add .`. Do not run `quarto preview`.

**Tech Stack:** Quarto, Markdown.

---

---

## Task 1: New intro — overwrite the file

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Read the current file**

Confirm the file exists at `level3.qmd`. Note the first line so you know what you are replacing.

- [ ] **Step 2: Write the new intro content**

Replace the entire file with exactly this content:

````markdown
---
title: "Level 3: AI in Your Terminal"
---

At Level 3, the AI runs in your terminal. You describe a goal; it reads your files, writes code, runs scripts, and iterates on failures until the task is done. You review the result. What makes this more capable than Level 2 is not that the agent sees more — it only sees what you give it — it is that it can execute. At Level 2, you run the tests and bring errors back to the AI. At Level 3, the agent runs that loop itself.

> **Most terminal AI tools require a paid subscription.** Free tiers typically provide access to web-based chat only — not the terminal agent. Check the pricing for whichever tool you use before getting started.
````

- [ ] **Step 3: Verify**

Read `level3.qmd`. Confirm:
- Title is `"Level 3: AI in Your Terminal"`
- No tagline
- One callout block present (paid subscription, no tool names)
- No content from the old file remains

- [ ] **Step 4: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — new intro"
```

---

## Task 2: Five-steps section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

````markdown

---

## The five steps at Level 3 {#five-steps}

| Step | Level 2 | Level 3 |
|---|---|---|
| **Organize** | Describe the goal in chat; AI proposes structure | Describe the goal; AI reads your existing files and proposes or creates structure |
| **Write** | AI suggests edits inline; you accept or reject | AI writes to files directly; you review what changed |
| **Test** | You run tests and bring failures back to AI | AI runs tests, reads the output, and iterates on failures itself |
| **Share** | AI writes a commit message from your diff; you commit | AI can stage, write the message, and commit — you review before or after |
| **Deploy** | Not covered | Scripted pipelines can be handed to the agent; it runs them and reports the result |

At Level 2, you executed each step. At Level 3, you describe the goal and review the result.
````

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## The five steps at Level 3`
- Table has 5 rows: Organize, Write, Test, Share, Deploy
- Closing sentence present

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — five-steps comparison section"
```

---

## Task 3: Interaction loop section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

````markdown

---

## The interaction loop {#interaction-loop}

Every terminal AI agent works the same way: you describe a goal, the agent reads your files and environment, acts, reads the output, and reports back. You review and continue or redirect.

A typical sequence:

*You:* "Read the files in src/ and tell me what this project does."
*Agent:* Reads the files. Returns a plain-English summary.

*You:* "Write a function in pipeline.py that filters rows by date range, then write a test and run it."
*Agent:* Writes the function. Writes the test. Runs it. Reads the failure. Fixes it. Runs it again. Reports the result.

You review what changed and decide what to do next.

Understanding this loop changes how you write prompts. You are not giving instructions to someone who will ask for clarification — you are describing a goal for an agent that acts immediately. Keep goals narrow enough to review comfortably.
````

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## The interaction loop`
- No mention of Claude or any specific tool
- Example shows the describe → act → review pattern

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — interaction loop section"
```

---

## Task 4: Scope of access section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

````markdown

---

## Scope of access {#scope}

Terminal AI agents operate with whatever access you grant them. Most tools let you configure this: read-only, write access to specific directories, permission to run commands, network access. The defaults vary by tool — some are conservative, some are not.

Start narrow. For most projects, a sensible starting scope:

- Read and write files within the project directory
- Run test and build commands you already use
- No broader filesystem access, no network access beyond what your scripts already use

An agent with write access to your filesystem and permission to run arbitrary commands can make changes you didn't intend. Review what it's done at each step, especially early in a project or with a new tool.
````

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## Scope of access`
- Bullet list of starting scope present
- No mention of Claude or any specific tool

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — scope of access section"
```

---

## Task 5: Project context section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`. The inner code block uses three backticks; the outer fence uses four backticks in the plan document but should be written as a normal three-backtick fence in the actual file.

The section to append to `level3.qmd`:

```
---

## Project context {#project-context}

Every session starts cold. The agent has no memory of previous sessions — no knowledge of your project structure, conventions, or the decisions you made last week. If you establish a rule in one session, it doesn't exist in the next.

Most terminal AI tools solve this with a project context file: a markdown file in your project root that the agent reads at the start of every session. Write your standing instructions there once.

```markdown
# Project context

Python data pipeline. Use pandas for all data work.
Every new function needs a docstring and a pytest test in tests/.
Never modify files in data/raw/.
```

Keep it factual. The context file is for things that are true for every task — project structure, conventions, constraints. Specifics for the current task go in the prompt, not the context file.
```

**Note on the code block:** The `\`\`\`markdown` block inside this section is a real fenced code block in the output file. Write it with three backticks, as shown above.

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## Project context`
- A fenced code block showing example context file content is present
- Final sentence about keeping it factual is present
- No mention of Claude or any specific tool

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — project context section"
```

---

## Task 6: Context window section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

```
---

## The context window {#context-window}

As a session runs, everything accumulates in a context window: your instructions, the files the agent read, the code it wrote, the test output, your feedback. This window has a fixed size, passed back and forth with every message. Once it fills, the agent starts dropping the oldest entries to make room.

In practice: a session that starts well can become unreliable as context fills. The agent forgets constraints you set earlier, duplicates code it already wrote, or loses track of decisions already made. This is a fundamental property of how these models work, not a defect in any specific tool.

The rule: end sessions before context degrades. Most tools display context usage somewhere; for those that don't, it is worth finding a way to make it visible. When context approaches 50%, end the session:

```
Write a summary of what we've done and what's left to progress.md
```

The next session reads that file and continues cleanly.
```

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## The context window`
- The 50% rule is stated
- The `progress.md` prompt example is present as a code block
- No mention of Claude or any specific tool

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — context window section"
```

---

## Task 7: Sessions and compaction section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

````markdown

---

## Sessions and compaction {#sessions}

Most terminal AI tools offer a compaction command — a way to summarize the current context and continue without starting a new session. This sounds useful but usually isn't. Compaction compresses the window, but the degraded reasoning from before the compaction still affects the session. Starting fresh with a written handoff produces better results.

Treat sessions as bounded units of work. End the session when the immediate task is done, not when the window is full. If something needs to carry over, write it to a file. The discipline is keeping tasks small enough to complete within one healthy session.

This also means avoiding open-ended prompts like "clean up the whole codebase." The scope is too large to complete before context degrades. Break large goals into specific, bounded tasks.
````

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## Sessions and compaction`
- Compaction drawback is explained
- Recommendation to use bounded tasks present
- No mention of Claude or any specific tool

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — sessions and compaction section"
```

---

## Task 8: Planning section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

```
---

## Planning {#planning}

Ad-hoc prompts produce worse results than structured ones. "Add a caching layer" leaves the agent guessing at scope, approach, and constraints. The agent makes choices — some of them wrong — and you spend time correcting them.

A structured workflow replaces guessing with agreement: describe the goal and clarify requirements first, then convert those into a specific plan, then execute against the plan. Each phase is short. The execution is faster and produces fewer unintended changes.

This matters more at Level 3 than at Level 2. At Level 2, a wrong direction produces a diff you can reject. At Level 3, a wrong direction can produce changes across multiple files before you notice. Explicit scoping during execution is just as important as upfront planning:

```
Refactor error handling in src/pipeline.py only. Do not change function signatures. Do not touch any other files.
```

Vague scope and broad file access reliably produce unintended changes.
```

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## Planning`
- Three-phase workflow described (clarify → plan → execute)
- Scoped prompt example present as a code block
- Final warning sentence present
- No mention of Claude or any specific tool

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — planning section"
```

---

## Task 9: Reasoning section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

````markdown

---

## Reasoning {#reasoning}

For routine tasks — write this function, run these tests — agents produce good results without additional guidance. For complex tasks — design a data pipeline, debug a subtle failure, choose between approaches with non-obvious trade-offs — the default reasoning is often too shallow.

Structured reasoning changes this: before acting on a complex task, the agent works through an explicit step-by-step process — understand the problem, identify constraints, consider approaches — before writing a line of code. This reasoning is visible. You can catch a wrong premise before it produces wrong code.

Use it selectively. On architectural decisions, multi-step algorithms, or anything where the right answer isn't obvious, structured reasoning is worth the overhead. On routine tasks, it isn't.
````

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## Reasoning`
- Distinction between routine and complex tasks present
- Visibility of reasoning mentioned
- Guidance on when to use it present
- No mention of Claude or any specific tool

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — reasoning section"
```

---

## Task 10: MCP section

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

````markdown

---

## MCP {#mcp}

Model Context Protocol is an open standard for connecting AI agents to external tools. Instead of pasting documentation into a prompt or building a one-off integration script, you configure an MCP server once and the agent can call it in any session.

An MCP server is a small program the agent invokes natively — indistinguishable from a built-in capability once configured. Common uses: pulling current library documentation, querying a database, running a custom analysis, accessing an API. Configure it once; it is available in every session.

The integrations below cover specific MCP servers worth using with Claude Code.
````

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## MCP`
- MCP described as tool-agnostic standard (not Claude-specific)
- Transition sentence to integrations present

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — MCP section"
```

---

## Task 11: Claude Code intro and seven integrations

**Files:**
- Modify: `level3.qmd`

This task adds the Claude Code transition and all seven integrations in one pass. They are homogeneous and short — each integration is 3-5 sentences plus a source line.

- [ ] **Step 1: Append the following content**

Add this content to the end of `level3.qmd`:

```
---

## Claude Code {#claude-code}

The concepts above apply to any terminal AI tool. The rest of this page is specific to Claude Code.

Install Claude Code and find platform-specific setup instructions at the official documentation:

**[code.claude.com/docs/en/terminal-guide#windows](https://code.claude.com/docs/en/terminal-guide#windows)**

Navigate to your project and type `claude` to start a session.

**Example session:**

*You type:*
```
Read my project and summarize what it does and how it's structured.
```

*Claude does:* Reads every file in the directory. Returns a plain-English summary of structure, purpose, and main components.

*You type:*
```
Write a function in analysis.py that groups sales by region and returns a sorted DataFrame. Write a test and run it.
```

*Claude does:* Writes the function, writes the test, runs it, reads the output, fixes any failure, reports the result.

> **Claude Code alongside your IDE.** Many developers keep VS Code open to review files while running Claude Code in a terminal alongside it. Claude makes the changes; the IDE shows you what changed.

---

## 01 — Statusline {#statusline}

*Make context usage visible — the most critical metric in a session*

The statusline adds a persistent bar at the bottom of your terminal showing context window percentage, session cost, model name, elapsed time, and git status. Without it, you notice context degradation when Claude starts making mistakes. With it, you can end sessions before quality drops.

Find install instructions in the Claude Code documentation or by asking Claude: `How do I install the statusline?`

> **Windows note:** The setup wizard sometimes fails on Windows. If the guided setup does not complete, install manually: `npx cc-statusline@latest` in your terminal.

> **On /compact:** As described in the sessions section above, starting fresh with a written summary produces better results than relying on /compact.

---

## 02 — Superpowers {#superpowers}

*Structured sub-agent workflows — the highest-impact single install*

Superpowers is a Claude Code plugin that implements the planning and sub-agent workflow described above. Instead of one session accumulating context until it degrades, your main Claude instance dispatches focused sub-agents — each with its own fresh context window. The orchestrator receives summaries, not full workloads.

Superpowers enforces the brainstorm → plan → execute workflow: clarify requirements before writing anything, produce a spec, execute against it.

Install via the Claude Code plugin menu — type `/plugin` inside a session and find Superpowers in the list.

> If you install one thing from this page, install Superpowers.

---

## 03 — Sequential Thinking {#sequential-thinking}

*Structured reasoning before complex tasks*

Sequential Thinking is an MCP server that adds explicit chain-of-thought reasoning to Claude Code. Before acting on complex tasks, Claude works through a visible step-by-step reasoning process — understand the problem, identify constraints, consider approaches, then implement.

Ask Claude to install it: `Please install the sequential thinking MCP server`

---

## 04 — Context7 {#context7}

*Current library documentation — eliminates hallucinated APIs*

Claude Code's training data has a cutoff date. When you ask it to use a library, it works from training data that may be months out of date — confidently using deprecated methods or renamed APIs. Context7 pulls current, version-specific documentation from live repositories and injects it into Claude's context at prompt time.

Add `use context7` to any prompt involving a library:

```
Build a FastAPI endpoint that validates JSON input. use context7
```

Install via the Claude Code plugin menu — type `/plugin` inside a session and find Context7 in the list.

---

## 05 — Warp {#warp}

*A better terminal for running Claude Code*

Warp is a modern terminal — a replacement for Windows Terminal, Mac Terminal, or the VS Code integrated terminal. You run Claude Code inside Warp.

Split panes let you run Claude on one side and browse your project files on the other. When Claude writes a plan to a file, you can read it while Claude is still working. Each command and its output is a discrete block — no scrolling through walls of output to find what Claude ran.

Download from [warp.dev](https://warp.dev) — available for Mac, Linux, and Windows. Free tier covers standard use.

---

## 06 — Happy Engineering {#mobile}

*Full terminal access from your phone*

Happy Engineering runs a live terminal session on your computer that you control from your phone's browser. When you connect from your phone, you are controlling the actual terminal on your machine — every integration you have configured is available. Tasks you start on your phone continue running on your computer.

Install from [happy.engineering](https://happy.engineering). Free and open source.

---

## 07 — Skills {#skills}

*Reusable workflows for tasks you do repeatedly*

Skills are markdown files in `.claude/skills/` that Claude Code reads when you invoke them. Instead of re-explaining a workflow every session, you encode it once and call it by name.

```
.claude/
  skills/
    add-module.md    ← invoked with /add-module
    run-analysis.md  ← invoked with /run-analysis
```

Describe the repetitive task in detail and ask Claude to build the skill for you. After a few iterations, it becomes a reliable automation available in every session.
```

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- `## Claude Code` section present with example session
- All seven integration sections present (01 through 07)
- No setup code blocks in integrations (except the `npx cc-statusline@latest` Windows fallback and the Context7 usage example)
- No keyboard shortcuts in any integration description
- Superpowers `/compact` note references the sessions section

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — claude code intro and seven integrations"
```

---

## Task 12: Quick Reference table

**Files:**
- Modify: `level3.qmd`

- [ ] **Step 1: Append the following section**

Add this content to the end of `level3.qmd`:

````markdown

---

## Quick Reference {#quick-reference}

| # | Integration | What it adds | Where to get it |
|---|-------------|--------------|-----------------|
| 01 | Statusline | Context %, session cost, model, git branch | Claude Code docs |
| 02 | Superpowers | Sub-agent workflows: brainstorm → plan → execute | `/plugin` inside Claude Code |
| 03 | Sequential Thinking | Chain-of-thought reasoning before complex tasks | Ask Claude: "install the sequential thinking MCP server" |
| 04 | Context7 | Current library docs at prompt time | `/plugin` inside Claude Code |
| 05 | Warp | Split panes, block output | [warp.dev](https://warp.dev) |
| 06 | Happy Engineering | Full terminal access from your phone | [happy.engineering](https://happy.engineering) |
| 07 | Skills | Reusable workflows for repetitive tasks | Create `.claude/skills/skillname.md` |
````

- [ ] **Step 2: Verify**

Read the end of `level3.qmd`. Confirm:
- Section heading is `## Quick Reference` (not "Quick reference — all seven" or any other variant)
- Table has 7 rows, columns: #, Integration, What it adds, Where to get it
- No "How to install" column header

- [ ] **Step 3: Stage and commit**

```bash
git add level3.qmd
git commit -m "feat: level3 — quick reference table"
```

---

## Self-review

### Flow check

The sections follow a question-answer chain:

1. **Intro** — What is Level 3? → establishes scope
2. **Five steps** — How does it change the workflow I know? → uses familiar frame
3. **Interaction loop** — How does it actually work? → explains the mechanics
4. **Scope of access** — What can it see and do? → a decision the reader needs to make early
5. **Project context** — How do I give it standing knowledge? → natural concern after understanding sessions start cold
6. **Context window** — What are the limits? → natural concern after understanding it reads files and accumulates state
7. **Sessions and compaction** — Given the limit, how do I manage sessions? → direct follow-on
8. **Planning** — Given sessions are finite, how do I structure work? → direct follow-on
9. **Reasoning** — How do I get better output on hard problems? → natural question once you're working structured
10. **MCP** — How do I extend what's available? → natural lead-in to integrations
11. **Claude Code + integrations** — Concrete tool that implements all of the above → concepts introduced, tool lands naturally
12. **Quick Reference** — Summary → clean ending

### Spec coverage

- [x] Paid subscription callout — Task 1, tool-agnostic
- [x] Five-step workflow comparison — Task 2
- [x] Interaction loop — Task 3
- [x] Scope of access — Task 4
- [x] Project context files (CLAUDE.md) — Task 5
- [x] Context window / context engineering — Task 6
- [x] Compaction and session management — Task 7
- [x] Planning workflow — Task 8
- [x] Reasoning / chain-of-thought — Task 9
- [x] MCP — Task 10
- [x] Claude Code intro — Task 11
- [x] All seven integrations — Task 11
- [x] Quick Reference — Task 12

### No-placeholder check

All tasks contain the exact markdown content to write. No "TBD", no "add appropriate content", no forward references to undefined sections.

### Content that was cut from the existing file and intentionally not restored

- Setup code blocks for most integrations (npm install, /plugin walkthrough, etc.) — replaced with prose directions to official docs
- Keyboard shortcuts in Warp section (Cmd+D, Ctrl+T) — removed
- "Three core commands" subsection in Superpowers — removed; covered in the planning section
- "What the statusline shows" subsection — removed; described inline
- "Building a skill with Superpowers" subsection — removed; described in one sentence
- Happy Engineering setup code block — removed; replaced with prose
- Context7 "How to use it" subsection — collapsed into the integration section
- Sequential Thinking MCP explanation — moved to the MCP section; integration is now brief
