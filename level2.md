# Level 2: AI in Your Editor
**pyflow — VS Code Edition**

---

Ignore 80% of the buttons on your screen. For Level 2, you are using exactly two tools: the **Main Editor Window** and the **Copilot Chat Sidebar**. Do not open Claude Code, the terminal, or any external agent panel yet. Those are Level 3.

---

## Standardizing the Workflow

You already know the five-step development workflow. Here is what changes at each step when AI lives inside your editor.

**Organize:** In a browser, you describe your project in a chat window with no file access. In the editor, you open the chat sidebar and describe what you want to build — AI proposes structure and logic before a single file exists.

**Write:** In a browser, you copy code from chat, switch windows, and paste manually. In the editor, ghost text appears inline as you type — press `Tab` to accept, no switching.

**Test:** In a browser, you copy the error message, open a new chat, and re-explain the context. In the editor, you click the Copilot icon next to the terminal error and AI reads the crash log directly.

**Share:** In a browser, you write your own commit message. In the editor, you click the sparkle button in the Source Control panel and AI reads your diff and writes it.

**Deploy:** Out of scope for Level 2.

---

> "Level 2 is not about memorizing syntax — it is about learning how to clearly state your intent to the editor so it does the manual labor."

Level 2 has two keys: `Tab` accepts what AI proposes. `Ctrl+I` opens inline edit on selected code. Everything else is reading and deciding.

---

## The Exercises

Twelve exercises across four phases. Each one proves a specific capability that browser chat cannot match. Do them in order — the compound interest project builds across phases and the terminal does not appear until Exercise 9.

---

## Phase A: Organize & Plan

*Before writing a single line of code, use AI to think through structure. This is the habit that separates organized projects from tangled ones.*

---

### Exercise 1 — Blueprint Prompt
**Phase:** Organize

**Action:**
Open VS Code. Open the Copilot Chat sidebar. Do not open any files. Send this prompt:

```
I want to build a Python project that calculates compound interest
over time for a given principal, rate, and number of years. It
should also compare different compounding frequencies (annual,
monthly, daily). Plan this project for me — describe the logic,
the inputs and outputs, and any edge cases I should think about.
Don't write any code yet.
```

Read the response. If anything is unclear or missing, ask a follow-up before moving on.

**Takeaway:** AI reasons about structure and logic before a single file exists. In a browser, you would have had to re-paste this plan every time you wanted to reference it. Here it stays in context for every exercise that follows.

---

### Exercise 2 — Scaffold Generation
**Phase:** Organize

**Action:**
In the same chat session, send this prompt:

```
Now suggest a folder and file structure for this project. List each
file with a one-line description of its purpose. Then give me the
terminal commands to create the folders and empty files.
Keep it simple — no frameworks, just clean Python modules.
```

Copy the suggested terminal commands. Use them to set up the project before starting the writing exercises.

**Takeaway:** AI generates the skeleton of a project from a plain-English description. You reviewed the plan before committing to any structure — that is the right order of operations.

---

> ### Why this works — and how to scale it
>
> You just described a goal in plain English and got back a structure. That is not a trick — it is a pattern. AI works best as a consumer of structured context, not as a generator of structure from scratch in every new chat.
>
> When you open a new chat and give a vague description, the AI is guessing at your intent. When you open a new chat and hand it a precise spec, the AI is executing against known constraints. Those are completely different quality levels — and the difference compounds over time.
>
> In serious AI-assisted codebases, the folder structure reflects this:
>
> - **`spec/`** — what the thing is: goals, constraints, non-goals
> - **`design/`** — how it is structured: architecture, data model, component map
> - **`context/`** — what AI needs to know each session: current state, decisions made, open questions
> - **`tasks/`** — discrete, completable units of work
>
> You are not there yet — this is Level 2. But the habit starts here: write down what you are building before you ask AI to build it. The documents are the project. The chat is just execution.
>
> If you ever feel like you are constantly backpedaling with AI, or moving in the wrong direction instead of making progress, the cause is almost always the same: you started building before you finished specifying. The fix is not a better prompt — it is better documents.

---

## Phase B: Writing Code

*Three exercises, each demonstrating a different way AI accelerates writing inside the editor. Keep the terminal panel closed for now — you will not need it until Exercise 9.*

---

### Exercise 3 — Comment-Driven Generation
**Phase:** Write

**Action:**
Open your `utils.py` file. Type this comment and press `Enter`:

```python
# Validate that principal, rate, and years are all positive numbers.
# Raise a ValueError with a descriptive message if any are not.
```

Wait. Ghost text should appear suggesting the full function body. Read it carefully before pressing `Tab` to accept.

Fallback — if nothing appears after a few seconds, send this in Copilot Chat:

```
Write a Python function that validates principal, rate, and years
are all positive numbers. Raise a ValueError with a descriptive
message for each invalid case. No external libraries.
```

**Takeaway:** A clear comment is a specification. The more precisely you describe the intent, the more accurately AI executes it. You described what you wanted — AI wrote the syntax. That is the trade at Level 2.

---

### Exercise 4 — Finish Starter Code
**Phase:** Write

**Action:**
Create `compound.py` and paste this starter code:

```python
def calculate_compound_interest(principal: float, rate: float,
                                years: int, n: int = 12) -> float:
    # Calculate compound interest using the standard formula.
    # principal: starting amount
    # rate: annual interest rate as a decimal (e.g. 0.05 for 5%)
    # years: number of years to compound
    # n: compounding frequency per year (default: monthly)
    # Return the final balance after the compounding period.
```

Place your cursor at the end of the last comment line and press `Enter`. Ghost text should suggest the function body. Read it before pressing `Tab`.

Fallback — send this in Copilot Chat:

```
Complete the function body for calculate_compound_interest based
on the comments inside it. Use only the standard library.
Return a float.
```

**Note on the formula:** The function should return the **final balance** — the full amount including the original principal — using the standard compound interest formula: `A = P(1 + r/n)^(nt)`. If AI returns only the interest earned (the growth above the principal), ask it to revise: `"Return the final balance, not just the interest earned."`

**Takeaway:** Writing intention before implementation produces more accurate completions than typing code directly. The comment block is the specification.

---

### Exercise 5 — Cross-File Context
**Phase:** Write

**Action:**
Create a second file called `main.py`. Open Copilot Chat and send:

```
I have a file called #compound.py that contains a function called
calculate_compound_interest. In #main.py, import that function and
call it with a principal of 1000, a rate of 0.05, and 10 years.
Print the result formatted to two decimal places.
```

Review what it generates. Check that the import path is correct and the function call matches the signature in `compound.py`.

**Takeaway:** The `#` symbol pulls a specific file into context mid-conversation. AI sees across files simultaneously. Browser chat would require copy-pasting both files before asking the same question.

---

## Phase C: Understand, Debug & Refactor

*Four exercises that use AI as a reviewer and optimizer. This is where in-editor AI earns its place.*

---

### Exercise 6 — Explain a Block
**Phase:** Understand

**Action:**
Select the entire `calculate_compound_interest` function in `compound.py`. Right-click and choose **Copilot → Explain This**.

Read the explanation. Then send this follow-up in chat:

```
What would happen if rate were passed as 5 instead of 0.05?
Would this function catch that mistake?
```

**Takeaway:** AI as an on-demand explainer for your own code. Works on any code you didn't write too — inherited projects, library internals, examples from online.

---

### Exercise 7 — Spot a Bug
**Phase:** Debug

**Action:**
Add this function to `compound.py`:

```python
def compare_compounding(principal: float, rate: float, years: int) -> dict:
    results = {}
    for label, n in [("annual", 1), ("monthly", 12), ("daily", 365)]:
        results[label] = principal * (1 + rate / n) ** (n * years) - principal
    return results
```

Select the function. Open Copilot Chat and send:

```
Review this function for correctness. Is there any input that would
cause a wrong result or raise an error? Be specific about where the
problem is and why it occurs.
```

**Note on the bug:** This function is intended to compare how much your money grows across different compounding frequencies — it should return the **final balance** for each frequency, just like `calculate_compound_interest`. Instead, it subtracts `principal` at the end, so it returns only the **interest earned** (the growth above what you started with). The formula should be `principal * (1 + rate / n) ** (n * years)` — no subtraction. Beyond the intent mismatch, a negative rate also produces a mathematically nonsensical result with no warning because there is no input validation. See what AI catches and what fix it proposes.

**Takeaway:** AI as a quality check. This kind of structural review would take careful reading and testing to catch manually. It took one prompt.

---

### Exercise 8 — Refactor for Performance
**Phase:** Refactor

**Action:**
Create `pipeline.py` and paste this function:

```python
import pandas as pd
import time

def process_sales(df: pd.DataFrame, year: int) -> pd.DataFrame:
    results = []
    for i in range(len(df)):
        row = df.iloc[i]
        if row["year"] == year:
            margin = (row["revenue"] - row["cost"]) / row["revenue"]
            results.append({
                "product": row["product"],
                "revenue": row["revenue"],
                "margin": margin
            })
    summary = pd.DataFrame(results)
    summary = summary.sort_values("margin")
    total = 0
    for i in range(len(summary)):
        total = total + summary.iloc[i]["revenue"]
    summary["revenue_share"] = summary["revenue"] / total
    return summary
```

**Step 1 — Generate test data.** Paste into a new file and run it once:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "product": np.random.choice(["Widget", "Gadget", "Doohickey"], 50000),
    "year": np.random.choice([2022, 2023, 2024], 50000),
    "revenue": np.random.uniform(100, 10000, 50000).round(2),
    "cost": np.random.uniform(50, 8000, 50000).round(2),
})
df.to_csv("sales_data.csv", index=False)
print("sales_data.csv created — 50,000 rows")
```

**Step 2 — Ask AI to refactor.** Select `process_sales` and send:

```
Refactor this function to use vectorized pandas operations instead
of iterating row by row. Fix the division-by-zero bug in the margin
calculation. Name the new function process_sales_fast. Keep the
output identical — same columns, same structure.
```

**Step 3 — Measure the difference.** Add this to the bottom of `pipeline.py` and run the file:

```python
if __name__ == "__main__":
    df = pd.read_csv("sales_data.csv")

    start = time.perf_counter()
    process_sales(df.copy(), 2023)
    t_original = time.perf_counter() - start

    start = time.perf_counter()
    process_sales_fast(df.copy(), 2023)
    t_fast = time.perf_counter() - start

    print(f"Original:   {t_original:.4f}s")
    print(f"Refactored: {t_fast:.4f}s")
    print(f"Speedup:    {t_original / t_fast:.1f}x faster")
```

**Takeaway:** Expect 10–50x faster on 50,000 rows. The terminal prints the proof. AI knows every vectorization idiom in pandas and applies them immediately.

---

### Exercise 9 — Terminal Crash Fix
**Phase:** Debug

**Action:**
This is the first exercise where the terminal appears. Open it in VS Code with `` Ctrl+` ``.

In `main.py`, deliberately introduce a type error by passing a string instead of a number:

```python
result = calculate_compound_interest("1000", 0.05, 10)
```

Run the file. The terminal will show a `TypeError`. Look for the small **Copilot icon** that appears next to the error output in the terminal panel. Click it and select **Explain using Copilot** or **Fix using Copilot**.

Read the explanation before applying any fix.

**Takeaway:** The terminal error hook connects execution failures directly to AI without copy-pasting. AI reads the crash log, the stack trace, and your code simultaneously. This is the first preview of what Level 3 looks like — where AI lives in the terminal full-time.

---

## Phase D: Test, Document & Share

*Three exercises that close the loop — verification, documentation, and version control. Each uses a native VS Code UI element.*

---

### Exercise 10 — Generate a Docstring
**Phase:** Document

**Action:**
Place your cursor inside `calculate_compound_interest` in `compound.py`, on the line just below the `def` line. Open inline edit with `Ctrl+I` and type:

```
/doc
```

A Google-style docstring should be generated and inserted. Review it — does it accurately describe the parameters and return value?

**Takeaway:** Professional documentation in under 5 seconds. `Ctrl+I` plus `/doc` is the full instruction. You described the intent with two keystrokes — AI read the function and wrote the documentation.

---

### Exercise 11 — Generate pytest Cases
**Phase:** Test

**Action:**
Select the `calculate_compound_interest` function. Open Copilot Chat and send:

```
Write pytest functions for calculate_compound_interest. Include:
- A normal case with typical values
- A case where rate is 0
- A case where years is 0
- A case where principal is negative (should raise ValueError)
Use only pytest. No fixtures.
```

Save the output to `test_compound.py`. Read each test before running it. Then run:

```
pytest test_compound.py -v
```

**Takeaway:** AI generates the edge cases you might not think to write yourself. Read them before trusting them — AI-generated tests occasionally test the wrong thing.

---

### Exercise 12 — Git Commit via Sparkle Button
**Phase:** Share

**Action:**
Stage all your changes using the Source Control panel in VS Code (the branch icon in the left sidebar).

In the commit message input box at the top of the Source Control panel, look for the **sparkle / Copilot icon**. Click it. AI reads your staged diff and generates a commit message.

Review the message, edit if needed, then commit.

**Takeaway:** AI writes the commit message by reading what actually changed — not what you tell it changed. This is the native UI doing what browser chat cannot: reading your diff directly without you copying it out first.

---

## Prompting Well

AI matches whatever scope you give it. These four principles separate productive sessions from overwhelming ones.

### 1. Give context before the ask
Describe what the project does and what role this code plays before making the request. Without context, AI fills gaps with assumptions.

- **Too thin:** "Write a function that validates input."
- **With context:** "I'm building a compound interest calculator. Write a function that validates that principal, rate, and years are all positive numbers and raises a ValueError with a descriptive message for each invalid case."

### 2. Constrain the scope explicitly
Without limits, AI defaults to comprehensive — more than you need, more than you can review. Explicit constraints keep the output manageable.

- **Too open:** "Add error handling."
- **Constrained:** "Add a try/except block to the calculate_compound_interest call in main.py only. Catch ValueError and print the message. Don't touch anything else."

### 3. Ask for a plan before you ask for code
For anything larger than a single function, ask AI to describe its approach first. Exercise 1 does this explicitly — it is the right habit for any new project.

- "Before writing any code, describe how you'd structure a function that compares compounding frequencies. What edge cases would you handle?"

### 4. Tell it your level and what you want to learn
"I'm new to pandas" produces simpler methods and more explanation. "Explain your reasoning alongside the code" gets you something to learn from, not just copy.

- "I'm learning pandas. Write this using basic operations and add a comment on each line explaining what it does."

### Example prompt combining all four

```
// context
I'm building a compound interest calculator in Python. I have a
function called calculate_compound_interest that takes principal,
rate, years, and n (compounding frequency). I need a function that
compares the final balance across annual, monthly, and daily
compounding for the same inputs.

// constraints
Keep it under 15 lines. Use only the standard library.
Return a plain dictionary with frequency labels as keys.

// plan before code
Before writing the function, describe how the outputs will differ
across compounding frequencies and what edge cases exist.
Then write the code.

// level
I'm comfortable with Python basics but newer to financial math.
Add a comment explaining the compound interest formula.
```

---

## When You Feel Lost

A response that's too long or too complex is feedback about the prompt — not your ability to code.

**The response is more complex than expected.**
Push back in the same chat: *"That's more than I need — simplify it. Just the core logic, no extra abstractions."*

**You've lost the thread mid-conversation.**
Long conversations accumulate context that works against you. Start fresh: *"Ignore the previous approach. Let's start over — I need something simpler."*

**It looks right but might not be.**
Confidence is not correctness. Running the code is always the check. When something fails, paste the exact error back into the chat.

---

## Editor & Context

### Your editor, your choice
VS Code with GitHub Copilot and PyCharm with JetBrains AI Assistant are the most common starting points. Cursor is a fork of VS Code rebuilt with in-context, inline AI editing as its core purpose rather than a plugin — popular and worth a look. Zed, Windsurf, and others follow the same idea. The capability matters; the specific tool is secondary.

### How file context works
When you open a file and open the Copilot Chat sidebar, the AI has already read your open file. You can also reference files explicitly:

- Type `#filename.py` in your chat message to pull a specific file into context
- AI sees across files simultaneously — something browser chat cannot do without copy-pasting each one

File context becomes meaningful starting at Exercise 5. The earlier exercises work from plain-English descriptions alone — no files need to be open for AI to reason about structure and generate code.

---

## What Comes Next: Level 3

Level 2 keeps AI inside the editor. It reads your files and proposes changes — but it cannot run anything. You still execute code in the terminal and carry results back into the chat manually.

Level 3 removes that constraint. A terminal agent like Claude Code has access to your full computing environment: it executes scripts, reads the output, installs packages, modifies files, and iterates until a task is complete. Exercise 9 above was the first preview of that boundary. Level 3 is what happens when you remove it entirely.