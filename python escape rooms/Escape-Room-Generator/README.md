# 🔐 Python Escape Room Builder

A browser-based tool for generating Python coding escape rooms as Google Colab notebooks. No installation required — open the HTML file, configure your settings, and download ready-to-use `.ipynb` files for your class.

Built for teachers running Python courses in grades 3–11.

---

## What It Does

Teachers configure:

- **Grade** (3–11, automatically grouped into Primary / Middle / High)
- **Skill level** (Beginner or Intermediate)
- **Format** (Solo notebook, or Team Chain — one notebook per student with a handoff mechanism)
- **Topics** from a 13-concept library aligned to the course curriculum

The tool generates Google Colab notebooks where students solve coding puzzles to unlock fragments, then assemble a final password. Each lock follows the same structure: instructions → starter code with TODOs → an auto-checking assert cell.

---

## Two Generation Modes

### 📚 Library Mode (no account needed)

Draws from a hand-written library of **3 distinct challenge variants per topic/group/skill combination**. A random variant is selected on each generate, so the same settings produce different notebooks each time.

- Works offline
- No API key or account required
- Assert checks are hand-verified
- Reliable for classroom use without pre-checking

### ✦ AI Mode (requires Anthropic API key)

Uses Claude to generate a unique scenario, instructions, starter code, and assert checks every time. Themes can be specified — "underwater research station", "medieval castle", whatever fits your class.

**⚠️ Important:** AI-generated assert checks can occasionally contain logic errors that either pass incorrect student code or reject correct solutions. Always run through the notebook yourself before giving it to students. This takes about 5 minutes and prevents a broken lock from stalling a class.

Get an API key at [console.anthropic.com](https://console.anthropic.com). Your key is sent directly to Anthropic and is never stored or logged by this tool.

---

## Topics Covered

| Session | Topic | Groups | Skills |
|---------|-------|--------|--------|
| S1 | Variables & Print | Primary, Middle | Beginner |
| S2 | Input & Data Types | Primary, Middle | Beginner |
| S3 | Conditionals | Primary, Middle, High | Beginner, Intermediate |
| S4 | For Loops | Primary, Middle, High | Beginner, Intermediate |
| S5 | While Loops | Middle, High | Beginner, Intermediate |
| S5 | Error Handling | Middle, High | Intermediate |
| S6 | Lists | Middle, High | Beginner, Intermediate |
| S6 | Tuples | Middle, High | Intermediate |
| S7 | Lists Deep Dive | Middle, High | Intermediate |
| S8 | Dictionaries | Middle, High | Intermediate |
| S9 | String Methods | High | Intermediate |
| S10 | Functions | Middle, High | Intermediate |
| S11 | Random Library | Middle, High | Intermediate |

Topics incompatible with the selected grade/skill are greyed out automatically. A **Suggest** button fills in the recommended sequence for the selected combination.

---

## Formats

### Solo
One `.ipynb` file. The student solves all locks in sequence. Each correct solution appends a fragment to a running list. The final cell assembles the password.

### Team Chain
One `.ipynb` file per student. The chain works as follows:

- **Student A** has no entry code. Solves their lock, passes their fragment verbally to Student B.
- **Student B** enters A's fragment as an entry code to unlock their notebook. Solves their lock, passes to C.
- Continues until the last student assembles the final password from all fragments.

Topics are distributed across the chain. If there are more students than topics, topics cycle.

---

## How to Use

1. Download `escape_room_builder.html`
2. Open it in any modern browser (Chrome, Firefox, Safari, Edge)
3. Select grade, skill level, and format
4. Choose topics — click **Suggest** for a recommended sequence, or pick manually
5. Click **Generate Escape Room**
6. Download the `.ipynb` file(s)
7. Upload to Google Drive and open with Google Colab, or share the link directly with students

No server, no login, no dependencies.

---

## Notebook Structure

Each generated notebook contains:

| Cell | Type | Purpose |
|------|------|---------|
| Intro | Markdown | Scenario, rules, how it works |
| Setup | Code | Initialises `_frags = []` |
| Lock header | Markdown | Concept label, lock number, instructions |
| Student work | Code | Starter code with TODO markers |
| Check cell | Code | Assert statements — appends fragment on pass |
| Final lock | Code | Assembles password from all fragments |
| Bonus | Markdown + Code | Optional extension challenge |

Students are instructed to use index cards for syntax reference and ask a classmate before the teacher — friction is intentional.

---

## Pedagogical Design

- One new concept per lock
- Output variables are always declared upfront so students can see what they're working toward
- Assert messages explain what went wrong without giving away the solution
- The bonus challenge is optional and does not affect the password
- Difficulty comes from thinking, not from structural complexity

---

## Repo Structure

```
escape-room-builder/
├── escape_room_builder.html   # The complete tool — open this in a browser
└── README.md
```

Everything runs inside the single HTML file. There are no dependencies, build steps, or server requirements.

---

## Related Projects

- [micro:bit Challenge Generator](../microbit-challenge-generator) — browser-based tool generating standards-aligned micro:bit challenges for grades 4–6

---

## Notes

- Tested in Chrome, Firefox, and Safari
- Team Chain notebooks use `input()` for entry codes — this works in Google Colab but will block execution in some other environments
- AI mode uses `claude-sonnet-4-20250514` via the Anthropic API
- Library mode works fully offline once the HTML file is downloaded
