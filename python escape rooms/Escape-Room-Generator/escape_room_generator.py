"""
Escape Room Generator
=====================
Generates Python escape room notebooks (.ipynb) for Google Colab.

Usage:
    python escape_room_generator.py --grade 7 --skill intermediate --format solo
    python escape_room_generator.py --grade 5 --skill beginner --format team --team-size 4

Arguments:
    --grade       3-11
    --skill       beginner | intermediate
    --format      solo | team
    --team-size   number of students in team chain (team format only, default 3)
    --output      output folder (default: current directory)

Grade groups:
    Primary = 3-5   Middle = 6-8   High = 9-11
"""

import json
import random
import os
import argparse


# ---------------------------------------------------------------------------
# Grade → group
# ---------------------------------------------------------------------------
def get_group(grade):
    if 3 <= grade <= 5:
        return "primary"
    elif 6 <= grade <= 8:
        return "middle"
    elif 9 <= grade <= 11:
        return "high"
    else:
        raise ValueError(f"Grade {grade} is outside the supported range (3-11).")


# ---------------------------------------------------------------------------
# Random code fragment generator
# ---------------------------------------------------------------------------
def make_code(n=5):
    """Returns a random alphanumeric code (no ambiguous chars 0/O, 1/I/l)."""
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "".join(random.choices(chars, k=n))


# ---------------------------------------------------------------------------
# Notebook cell helpers
# ---------------------------------------------------------------------------
def md_cell(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src}


def code_cell(src):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": src,
    }


def build_notebook(cells):
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.10.0"},
            "colab": {"provenance": []},
        },
        "cells": cells,
    }


# ---------------------------------------------------------------------------
# Lock definitions
# Each lock has: title, groups, skills, instructions, starter, check
# All three have variants keyed by group (primary/middle/high)
# ---------------------------------------------------------------------------
LOCKS = {
    "variables": {
        "title": "Lock — Store the Clue",
        "groups": ["primary", "middle"],
        "skills": ["beginner"],
        "instructions": {
            "primary": (
                "A secret agent left behind three clues.\n\n"
                "Assign a short string to each variable: `clue1`, `clue2`, `clue3`.\n\n"
                "Then print all three."
            ),
            "middle": (
                "Store three pieces of mission intelligence: `location`, `suspect`, `time`.\n\n"
                "Each must be a non-empty string.\n\n"
                "Print a summary using an f-string."
            ),
        },
        "starter": {
            "primary": (
                '# TODO: assign string values to clue1, clue2, clue3 then print each\n'
                'clue1 = ""\n'
                'clue2 = ""\n'
                'clue3 = ""\n\n'
                'print(clue1)\n'
                'print(clue2)\n'
                'print(clue3)'
            ),
            "middle": (
                '# TODO: assign string values then print the f-string\n'
                'location = ""\n'
                'suspect  = ""\n'
                'time     = ""\n\n'
                'print(f"The suspect is {suspect}, last seen at {location} at {time}.")'
            ),
        },
        "check": {
            "primary": (
                'assert isinstance(clue1, str) and len(clue1) > 0, "clue1 must be a non-empty string"\n'
                'assert isinstance(clue2, str) and len(clue2) > 0, "clue2 must be a non-empty string"\n'
                'assert isinstance(clue3, str) and len(clue3) > 0, "clue3 must be a non-empty string"'
            ),
            "middle": (
                'assert isinstance(location, str) and len(location) > 0, "location must be a non-empty string"\n'
                'assert isinstance(suspect,  str) and len(suspect)  > 0, "suspect must be a non-empty string"\n'
                'assert isinstance(time,     str) and len(time)     > 0, "time must be a non-empty string"'
            ),
        },
    },

    "conditionals": {
        "title": "Lock — The Access Gate",
        "groups": ["primary", "middle", "high"],
        "skills": ["beginner", "intermediate"],
        "instructions": {
            "primary": (
                "Set `access_level` to any integer.\n\n"
                "- If it is **greater than 5**, set `door` to `'open'`\n"
                "- Otherwise set `door` to `'locked'`"
            ),
            "middle": (
                "Set `access_level` to an integer. Write an if/elif/else:\n\n"
                "- `>= 8` → `clearance = 'high'`\n"
                "- `4 to 7` → `clearance = 'medium'`\n"
                "- below 4 → `clearance = 'low'`"
            ),
            "high": (
                "Given `access_level` (int) and `has_badge` (bool):\n\n"
                "- Set `clearance = 'granted'` **only if** level >= 7 AND has_badge is True\n"
                "- All other combinations → `clearance = 'denied'`"
            ),
        },
        "starter": {
            "primary": (
                '# TODO: set access_level then write your if/else\n'
                'access_level = 0\n'
                'door = ""\n\n'
                '# your if/else here\n\n'
                'print(f"Door: {door}")'
            ),
            "middle": (
                '# TODO: set access_level then write your if/elif/else\n'
                'access_level = 0\n'
                'clearance = ""\n\n'
                '# your if/elif/else here\n\n'
                'print(f"Clearance: {clearance}")'
            ),
            "high": (
                '# TODO: set both variables then write your combined condition\n'
                'access_level = 0\n'
                'has_badge = False\n'
                'clearance = ""\n\n'
                '# your if/else here\n\n'
                'print(f"Access: {clearance}")'
            ),
        },
        "check": {
            "primary": (
                'assert door in ("open", "locked"), "door must be \'open\' or \'locked\'"\n'
                'assert (access_level > 5 and door == "open") or (access_level <= 5 and door == "locked"), "Check your condition"'
            ),
            "middle": (
                'assert clearance in ("high", "medium", "low"), "clearance must be high, medium or low"\n'
                'assert (access_level >= 8 and clearance == "high") or \\\n'
                '       (4 <= access_level <= 7 and clearance == "medium") or \\\n'
                '       (access_level < 4 and clearance == "low"), "Check your elif chain"'
            ),
            "high": (
                'assert clearance in ("granted", "denied"), "clearance must be granted or denied"\n'
                'assert (access_level >= 7 and has_badge and clearance == "granted") or \\\n'
                '       (not (access_level >= 7 and has_badge) and clearance == "denied"), \\\n'
                '       "Check your combined condition"'
            ),
        },
    },

    "for_loops": {
        "title": "Lock — Scan the Cargo",
        "groups": ["primary", "middle", "high"],
        "skills": ["beginner", "intermediate"],
        "instructions": {
            "primary": (
                "The cargo hold has four items.\n\n"
                "Use a **for loop** to print each item.\n\n"
                "Count them in `total_items`."
            ),
            "middle": (
                "Loop through `cargo`.\n\n"
                "Count how many items contain the word `'classified'` and store the count in `classified_count`."
            ),
            "high": (
                "Loop through `cargo` using `enumerate()`.\n\n"
                "Build a list called `manifest` where each entry is a string like:\n\n"
                "`'Item 1: food supplies'`\n\n"
                "Labels start at **1**, not 0."
            ),
        },
        "starter": {
            "primary": (
                'cargo = ["food supplies", "medical kits", "classified documents", "tools"]\n'
                'total_items = 0\n\n'
                '# TODO: loop through cargo, print each item, increment total_items\n'
                'for item in cargo:\n'
                '    print("")  # replace "" with the variable\n'
                '    total_items += 1\n\n'
                'print(f"Total items scanned: {total_items}")'
            ),
            "middle": (
                'cargo = ["food supplies", "classified files", "medical kits", "classified data", "tools"]\n'
                'classified_count = 0\n\n'
                '# TODO: loop and count items that contain "classified"\n'
                'for item in cargo:\n'
                '    if "" in item:  # replace "" with the word to check\n'
                '        classified_count += 1\n\n'
                'print(f"Classified items found: {classified_count}")'
            ),
            "high": (
                'cargo = ["food supplies", "classified files", "medical kits", "tools", "comms device"]\n'
                'manifest = []\n\n'
                '# TODO: use enumerate() — labels must start at 1\n'
                'for i, item in enumerate(cargo):\n'
                '    manifest.append("")  # build the string here\n\n'
                'print(manifest)'
            ),
        },
        "check": {
            "primary": (
                'assert total_items == 4, f"Expected 4 items, got {total_items}"'
            ),
            "middle": (
                'assert classified_count == 2, f"Expected 2 classified items, got {classified_count}"'
            ),
            "high": (
                'assert len(manifest) == 5, f"manifest should have 5 entries, got {len(manifest)}"\n'
                'assert manifest[0] == "Item 1: food supplies", f"First entry wrong: {manifest[0]}"'
            ),
        },
    },

    "while_loops": {
        "title": "Lock — Crack the Combination",
        "groups": ["middle", "high"],
        "skills": ["beginner", "intermediate"],
        "instructions": {
            "middle": (
                "Set `attempts = 0` and `cracked = False`.\n\n"
                "Write a while loop: while `attempts < 5` and `not cracked`:\n\n"
                "- Increment `attempts`\n"
                "- When `attempts` reaches 3, set `cracked = True`"
            ),
            "high": (
                "Set `counter = 1`, `steps = 0`, `threshold = 100`.\n\n"
                "Write a while loop that **doubles** `counter` each iteration until it exceeds `threshold`.\n\n"
                "Count how many iterations in `steps`."
            ),
        },
        "starter": {
            "middle": (
                'attempts = 0\n'
                'cracked  = False\n\n'
                '# TODO: while loop — increment attempts, set cracked=True when attempts==3\n'
                'while attempts < 5 and not cracked:\n'
                '    attempts += 1\n'
                '    if attempts == 3:\n'
                '        cracked = True\n\n'
                'print(f"Cracked: {cracked}, Attempts used: {attempts}")'
            ),
            "high": (
                'counter   = 1\n'
                'steps     = 0\n'
                'threshold = 100\n\n'
                '# TODO: while loop — double counter, increment steps\n'
                'while counter <= threshold:\n'
                '    counter = counter * 2  # correct — make sure your condition is right\n'
                '    steps += 1\n\n'
                'print(f"Counter: {counter}, Steps taken: {steps}")'
            ),
        },
        "check": {
            "middle": (
                'assert cracked == True, "cracked should be True after 3 attempts"\n'
                'assert attempts == 3, f"Expected 3 attempts, got {attempts}"'
            ),
            "high": (
                'assert counter > 100, f"Counter should exceed 100, got {counter}"\n'
                'assert steps == 7, f"Expected 7 doublings, got {steps}"'
            ),
        },
    },

    "lists": {
        "title": "Lock — Inventory Check",
        "groups": ["middle", "high"],
        "skills": ["beginner", "intermediate"],
        "instructions": {
            "middle": (
                "You have an equipment list.\n\n"
                "1. Add `'grappling hook'` to the end\n"
                "2. Remove `'broken radio'`\n"
                "3. Store the final length in `item_count`"
            ),
            "high": (
                "Sort `equipment` alphabetically into a new list called `sorted_gear`.\n\n"
                "Then use a **list comprehension** to build `long_items` — "
                "items with more than 10 characters."
            ),
        },
        "starter": {
            "middle": (
                'equipment = ["torch", "broken radio", "rope", "first aid kit"]\n\n'
                '# TODO: append grappling hook, remove broken radio\n'
                'equipment.append("")   # add grappling hook\n'
                'equipment.remove("")   # remove broken radio\n\n'
                'item_count = len(equipment)\n'
                'print(f"Equipment: {equipment}")\n'
                'print(f"Total: {item_count}")'
            ),
            "high": (
                'equipment = ["torch", "rope", "first aid kit", "grappling hook", "compass"]\n\n'
                '# TODO: sort and build list comprehension\n'
                'sorted_gear = sorted(equipment)\n'
                'long_items  = [item for item in equipment if len(item) > 10]\n\n'
                'print(f"Sorted: {sorted_gear}")\n'
                'print(f"Long names: {long_items}")'
            ),
        },
        "check": {
            "middle": (
                'assert "grappling hook" in equipment, "grappling hook should be in equipment"\n'
                'assert "broken radio" not in equipment, "broken radio should be removed"\n'
                'assert item_count == 4, f"Expected 4 items, got {item_count}"'
            ),
            "high": (
                'assert sorted_gear == sorted(["torch","rope","first aid kit","grappling hook","compass"]), \\\n'
                '       "sorted_gear is not in alphabetical order"\n'
                'assert all(len(i) > 10 for i in long_items), \\\n'
                '       "long_items should only contain items with more than 10 characters"\n'
                'assert "first aid kit" in long_items, "first aid kit (11 chars) should be in long_items"'
            ),
        },
    },

    "dictionaries": {
        "title": "Lock — Agent Profiles",
        "groups": ["middle", "high"],
        "skills": ["intermediate"],
        "instructions": {
            "middle": (
                "You have an agent dictionary.\n\n"
                "1. Add a key `'status'` with value `'active'`\n"
                "2. Look up the agent's `'codename'` and store it in a variable called `codename`"
            ),
            "high": (
                "You have a list of agent dictionaries.\n\n"
                "Loop through them and build `active_agents` — "
                "a dictionary mapping **codename → clearance**, "
                "but only include agents whose status is `'active'`."
            ),
        },
        "starter": {
            "middle": (
                'agent = {\n'
                '    "codename": "Nighthawk",\n'
                '    "clearance": 8,\n'
                '    "location": "Berlin"\n'
                '}\n\n'
                '# TODO: add status key, then look up codename\n'
                'agent["status"] = "active"   # this line is correct\n'
                'codename = agent[""]         # replace "" with the right key\n\n'
                'print(agent)\n'
                'print(f"Codename: {codename}")'
            ),
            "high": (
                'agents = [\n'
                '    {"codename": "Nighthawk", "clearance": 8, "status": "active"},\n'
                '    {"codename": "Phantom",   "clearance": 5, "status": "inactive"},\n'
                '    {"codename": "Cipher",    "clearance": 9, "status": "active"},\n'
                ']\n'
                'active_agents = {}\n\n'
                '# TODO: loop and build active_agents\n'
                'for agent in agents:\n'
                '    if agent["status"] == "active":\n'
                '        active_agents[agent["codename"]] = agent["clearance"]\n\n'
                'print(active_agents)'
            ),
        },
        "check": {
            "middle": (
                'assert agent.get("status") == "active", "agent[\'status\'] should be \'active\'"\n'
                'assert codename == "Nighthawk", f"Expected Nighthawk, got {codename}"'
            ),
            "high": (
                'assert "Nighthawk" in active_agents, "Nighthawk should be in active_agents"\n'
                'assert "Phantom" not in active_agents, "Phantom is inactive and should not be included"\n'
                'assert active_agents.get("Cipher") == 9, "Cipher\'s clearance should be 9"'
            ),
        },
    },

    "functions": {
        "title": "Lock — Decode the Signal",
        "groups": ["middle", "high"],
        "skills": ["intermediate"],
        "instructions": {
            "middle": (
                "Write a function `decode(message)` that returns `message` reversed.\n\n"
                "Call it on `encrypted` and store the result in `decoded`."
            ),
            "high": (
                "Write `caesar_shift(text, shift)` — shifts every letter forward by `shift` positions "
                "(wrapping z → a). Non-letters stay unchanged.\n\n"
                "Test: `caesar_shift('abc', 1)` → `'bcd'`"
            ),
        },
        "starter": {
            "middle": (
                'encrypted = "noissiM tpeccA uoY dluohS"\n\n'
                '# TODO: define decode and call it\n'
                'def decode(message):\n'
                '    return message[::-1]   # this is correct — make sure you call the function below\n\n'
                'decoded = decode(encrypted)\n'
                'print(f"Decoded: {decoded}")'
            ),
            "high": (
                '# TODO: complete caesar_shift\n'
                'def caesar_shift(text, shift):\n'
                '    result = ""\n'
                '    for char in text:\n'
                '        if char.isalpha():\n'
                '            base = ord("a") if char.islower() else ord("A")\n'
                '            result += chr((ord(char) - base + shift) % 26 + base)\n'
                '        else:\n'
                '            result += char\n'
                '    return result\n\n'
                'print(caesar_shift("abc", 1))   # should print: bcd\n'
                'print(caesar_shift("xyz", 3))   # should print: abc'
            ),
        },
        "check": {
            "middle": (
                'assert callable(decode), "decode must be a function"\n'
                'assert decoded == "Should You Accept Mission", f"Got: {decoded}"'
            ),
            "high": (
                "assert caesar_shift('abc', 1) == 'bcd', f\"Expected bcd, got {caesar_shift('abc', 1)}\"\n"
                "assert caesar_shift('xyz', 3) == 'abc', f\"Expected abc, got {caesar_shift('xyz', 3)}\""
            ),
        },
    },

    "string_methods": {
        "title": "Lock — Parse the Transmission",
        "groups": ["high"],
        "skills": ["intermediate"],
        "instructions": {
            "high": (
                "A transmission arrived as a raw, messy string.\n\n"
                "1. Split `transmission` on `','` into a list called `parts`\n"
                "2. Strip whitespace from each part\n"
                "3. Join them back with `' | '` into `clean_signal`"
            ),
        },
        "starter": {
            "high": (
                'transmission = "ALPHA ,  BRAVO , CHARLIE,  DELTA "\n\n'
                '# TODO: split, strip each part, join\n'
                'parts = transmission.split(",")\n'
                'parts = [p.strip() for p in parts]    # this is correct\n'
                'clean_signal = " | ".join(parts)      # this is correct — check your split delimiter above\n\n'
                'print(f"Parts: {parts}")\n'
                'print(f"Clean signal: {clean_signal}")'
            ),
        },
        "check": {
            "high": (
                'assert parts == ["ALPHA", "BRAVO", "CHARLIE", "DELTA"], f"Got: {parts}"\n'
                'assert clean_signal == "ALPHA | BRAVO | CHARLIE | DELTA", f"Got: {clean_signal}"'
            ),
        },
    },
}


# ---------------------------------------------------------------------------
# Concept sequence per group/skill
# ---------------------------------------------------------------------------
SEQUENCES = {
    ("primary",  "beginner"):     ["variables", "conditionals", "for_loops"],
    ("primary",  "intermediate"): ["conditionals", "for_loops", "lists"],
    ("middle",   "beginner"):     ["conditionals", "for_loops", "while_loops", "lists"],
    ("middle",   "intermediate"): ["for_loops", "lists", "dictionaries", "functions"],
    ("high",     "beginner"):     ["conditionals", "for_loops", "while_loops", "lists"],
    ("high",     "intermediate"): ["functions", "dictionaries", "string_methods", "while_loops"],
}

SCENARIOS = {
    "primary": [
        "You are a junior coder at **Cipher HQ**. The database has been locked by a rogue program. Solve each puzzle to recover a fragment of the override password and restore access!",
        "A data thief has frozen the school's robot fleet. Each robot is locked behind a code. Unlock them one by one to get the robots running again!",
    ],
    "middle": [
        "You are a field operative. Your handler has gone dark. The only way to reach base is to crack through each security lock using your training dossier.",
        "The **Data Vault** was sealed after a breach. Mission-critical intelligence is locked inside. Work through each security layer to recover the files.",
    ],
    "high": [
        "A hostile actor has encrypted the agency's network. You have limited time to reverse-engineer each protection layer and recover the master decryption key.",
        "You are a systems analyst. An unknown process has locked the production environment. Solve each diagnostic challenge to neutralise it.",
    ],
}

BONUS = {
    "primary": (
        "Can you print your variables in **reverse order** using a list and `reversed()`?\n\n"
        "```python\n# Put your variables in a list, then loop through it in reverse\n```"
    ),
    "middle": (
        "Add a `try/except` block around your main logic so that if a variable is undefined, "
        "it prints a friendly message instead of crashing.\n\n"
        "```python\ntry:\n    pass  # your code\nexcept NameError as e:\n    print(f'Missing variable: {e}')\n```"
    ),
    "high": (
        "Write `validate_all(checks: list) -> bool` that returns `True` only if every item "
        "in the list is `True`. Test it with at least two different inputs.\n\n"
        "```python\ndef validate_all(checks):\n    return all(checks)\n```"
    ),
}


# ---------------------------------------------------------------------------
# Cell builders
# ---------------------------------------------------------------------------
def _pick(d, group):
    """Return the variant for group, falling back gracefully."""
    return d.get(group) or d.get("middle") or d.get("primary") or list(d.values())[0]


def lock_cells(lock_id, group, skill, fragment, num, total):
    L = LOCKS[lock_id]
    instruct = _pick(L["instructions"], group)
    starter  = _pick(L["starter"], group)
    check    = _pick(L["check"], group)

    # Markdown
    md_src = (
        f"## 🔒 {L['title']}\n\n"
        f"**Concept:** {lock_id.replace('_', ' ').title()}"
        f"  &nbsp;|&nbsp;  Lock {num} of {total}\n\n"
        f"{instruct}\n\n"
        f"---"
    )

    # Student work
    work_src = f"# ── Your code ──────────────────────────────────────────\n\n{starter}"

    # Check — indents the assert lines inside try block
    indented_check = "\n".join("    " + line for line in check.split("\n"))
    chk_src = (
        "# ── Check cell — do not edit ────────────────────────────\n"
        "_frags = globals().get('_frags', [])\n"
        "try:\n"
        f"{indented_check}\n"
        f'    _frags.append("{fragment}")\n'
        f'    print(f"\\u2705  Lock {num} open! Fragment: {fragment}")\n'
        "except AssertionError as e:\n"
        '    print(f"\\u274c  Not yet \u2014 {e}")\n'
        "except Exception as e:\n"
        '    print(f"\\u26a0\\ufe0f   Error \u2014 {e}")\n'
    )

    return [md_cell(md_src), code_cell(work_src), code_cell(chk_src)]


def intro_cells(title, group, skill, scenario, team_note=""):
    body = (
        f"# \U0001f510 {title}\n\n"
        f"**Group:** {group.title()}\u2003|\u2003**Skill level:** {skill.title()}\n\n"
        "---\n\n"
        "## The Scenario\n\n"
        f"{scenario}"
    )
    if team_note:
        body += f"\n\n---\n\n{team_note}"
    body += (
        "\n\n---\n\n"
        "## How It Works\n\n"
        "- Each lock has three cells: **instructions \u2192 your code \u2192 check**\n"
        "- Run the **check cell** to test your answer\n"
        "- A correct answer reveals a **code fragment**\n"
        "- Collect all fragments to build the **final password**\n\n"
        "**Rules:**\n"
        "- Write your own code\n"
        "- Use index card helpers for syntax \u2014 not AI\n"
        "- Ask a classmate before asking the teacher"
    )
    setup_src = (
        "# \u2500\u2500 Run this cell first \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n"
        "_frags = []\n"
        'print("\\U0001f680 Escape room ready. Good luck.")'
    )
    return [md_cell(body), code_cell(setup_src)]


def final_cells(fragments, group):
    n  = len(fragments)
    pw = "-".join(fragments)
    final_md = (
        "## \U0001f3c1 Final Lock\n\n"
        "Solved all your locks? Run the cell below to reveal the password."
    )
    final_code = (
        "# \u2500\u2500 Final check \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n"
        "_frags = globals().get('_frags', [])\n"
        f"if len(_frags) == {n}:\n"
        f'    print(f"\\U0001f389 PASSWORD UNLOCKED: {pw}")\n'
        "else:\n"
        f'    print(f"\\U0001f512 {{len(_frags)}}/{n} fragments collected. Keep going.")\n'
    )
    bonus_md = (
        "## \u2b50 Bonus Challenge \u2014 Optional\n\n"
        f"{BONUS.get(group, 'No bonus for this level.')}\n\n"
        "*This does not affect your password.*"
    )
    bonus_code = "# Your bonus code here\n"
    return [
        md_cell(final_md),
        code_cell(final_code),
        md_cell(bonus_md),
        code_cell(bonus_code),
    ]


# ---------------------------------------------------------------------------
# Solo escape room
# ---------------------------------------------------------------------------
def generate_solo(grade, skill, output_dir):
    group    = get_group(grade)
    seq      = SEQUENCES.get((group, skill))
    if not seq:
        raise ValueError(f"No concept sequence defined for group={group}, skill={skill}")

    frags    = [make_code() for _ in seq]
    scenario = random.choice(SCENARIOS[group])
    title    = f"Escape Room \u2014 Grade {grade} ({skill.title()})"

    cells = intro_cells(title, group, skill, scenario)
    for i, lid in enumerate(seq):
        cells += lock_cells(lid, group, skill, frags[i], i + 1, len(seq))
    cells += final_cells(frags, group)

    nb    = build_notebook(cells)
    fname = f"escape_room_grade{grade}_{skill}_solo.ipynb"
    path  = os.path.join(output_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
    return path


# ---------------------------------------------------------------------------
# Team chain escape room
# Student A solves lock 1 → passes fragment → Student B enters it as entry code,
# solves lock 2 → passes → ... → last student assembles final password.
# ---------------------------------------------------------------------------
def generate_team(grade, skill, team_size, output_dir):
    group    = get_group(grade)
    all_seq  = SEQUENCES.get((group, skill))
    if not all_seq:
        raise ValueError(f"No concept sequence defined for group={group}, skill={skill}")

    assigned = [all_seq[i % len(all_seq)] for i in range(team_size)]
    frags    = [make_code() for _ in range(team_size)]
    scenario = random.choice(SCENARIOS[group])
    paths    = []

    for idx in range(team_size):
        label      = chr(65 + idx)          # A, B, C …
        lid        = assigned[idx]
        frag       = frags[idx]
        prev_label = chr(65 + idx - 1) if idx > 0 else None
        next_label = chr(65 + idx + 1) if idx < team_size - 1 else None
        prev_frag  = frags[idx - 1] if idx > 0 else None

        # Team note for intro
        if idx == 0:
            team_note = (
                f"## \U0001f517 Team Chain \u2014 Student {label} of {team_size}\n\n"
                "You are **first in the chain**. No entry code needed.\n\n"
                f"Solve your lock, then pass your fragment to **Student {next_label}**."
            )
        elif idx == team_size - 1:
            team_note = (
                f"## \U0001f517 Team Chain \u2014 Student {label} of {team_size}\n\n"
                f"\u26a0\ufe0f Wait for **Student {prev_label}'s fragment** before running the setup cell.\n\n"
                "You are **last in the chain**. Once your lock is open, assemble the final password."
            )
        else:
            team_note = (
                f"## \U0001f517 Team Chain \u2014 Student {label} of {team_size}\n\n"
                f"\u26a0\ufe0f Wait for **Student {prev_label}'s fragment** before running the setup cell.\n\n"
                f"Once your lock is open, pass your fragment to **Student {next_label}**."
            )

        title = f"Escape Room \u2014 Grade {grade} ({skill.title()}) \u2014 Student {label}"
        cells = intro_cells(title, group, skill, scenario, team_note)

        # Entry gate
        if idx == 0:
            gate_src = (
                "# Student A \u2014 no entry code needed\n"
                "_frags = []\n"
                'print("\\U0001f680 Chain started. Solve your lock.")'
            )
        else:
            gate_src = (
                f'# Enter the fragment you received from Student {prev_label}\n'
                f'entry_code = input("Entry code from Student {prev_label}: ")\n\n'
                f'if entry_code.strip().upper() == "{prev_frag}":\n'
                f'    _frags = []\n'
                f'    print("\\u2705 Accepted. Begin your lock.")\n'
                f'else:\n'
                f'    print("\\u274c Wrong code. Check with Student {prev_label}.")\n'
            )
        cells.append(code_cell(gate_src))

        # Single lock for this student
        cells += lock_cells(lid, group, skill, frag, 1, 1)

        # Handoff or final
        if idx < team_size - 1:
            handoff_md = (
                f"## \U0001f501 Hand Off\n\n"
                f"Lock open? Copy your fragment and pass it to **Student {next_label}**.\n\n"
                "Do not share it until they are ready to start."
            )
            cells.append(md_cell(handoff_md))
        else:
            cells += final_cells(frags, group)
            cells.append(md_cell(
                "## \U0001f3c6 Chain Complete!\n\n"
                "You were the last link. The full password is assembled above.\n\n"
                "Raise your hand \u2014 your team has escaped!"
            ))

        nb    = build_notebook(cells)
        fname = f"escape_room_grade{grade}_{skill}_team_student{label}.ipynb"
        path  = os.path.join(output_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=2)
        paths.append(path)

    return paths


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Generate Python escape room notebooks for Google Colab."
    )
    parser.add_argument("--grade",     type=int, required=True,
                        help="Grade level 3-11")
    parser.add_argument("--skill",     type=str, required=True,
                        choices=["beginner", "intermediate"],
                        help="beginner or intermediate")
    parser.add_argument("--format",    type=str, required=True,
                        choices=["solo", "team"],
                        help="solo or team")
    parser.add_argument("--team-size", type=int, default=3,
                        help="Number of students in team chain (team format only)")
    parser.add_argument("--output",    type=str, default=".",
                        help="Output directory (default: current directory)")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    if args.format == "solo":
        path = generate_solo(args.grade, args.skill, args.output)
        print(f"\u2705  Solo notebook created:\n    {path}")
    else:
        paths = generate_team(args.grade, args.skill, args.team_size, args.output)
        print(f"\u2705  Team chain created ({len(paths)} notebooks):")
        for p in paths:
            print(f"    {p}")


if __name__ == "__main__":
    main()
