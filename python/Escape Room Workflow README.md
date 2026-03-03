# Python Escape Room Workflow

This document captures how I design Python escape room challenges and why I use them in class.

I started building these because my students were jumping straight into AI tools whenever they hit friction. Instead of thinking through the logic, they were outsourcing it. We already use Blooket every few sessions as a break. I wanted something that still felt like a game, but required real problem solving.

The escape room format lets me keep the energy of a game while protecting the thinking.

---

## Why I Use Escape Rooms

The goal is reinforcement.

Each lock targets one concept:

* conditionals
* loops
* list operations
* dictionaries
* integration across structures

Students have to write the code themselves. The check cell validates their answer immediately. They cannot move forward until the logic is correct.

That friction is intentional.

The structure slows them down just enough to think.

---

## How I Structure Each Lock

Each lock has three parts.

### 1. Markdown Cell

Short instructions. Clear expectations. Specific variable names. No ambiguity about what needs to be produced.

### 2. Student Work Cell

* Starter data provided
* Target variables already declared
* A TODO marker
* Print statements for visibility

I remove unnecessary structural decisions so students focus on logic.

### 3. Check Cell

* Uses assert
* Appends a password fragment when correct
* Prints useful error messages
* Shows progress

This gives immediate feedback and removes grading overhead.

Students see exactly what is wrong and try again.

---

## Index Card Helpers (Syntax Support Without AI)

To prevent students from defaulting to AI tools for small syntax questions, I provide index card reference helpers.

These are physical or printable cards that include:

* Basic if / elif / else structure
* for loop patterns
* range examples
* List methods such as append, sort, remove
* Dictionary access using dict[key] and dict.get()
* While loop pattern

The rule is simple:

Before asking AI, check the cards.

The cards give syntax reminders, not solutions. They support recall without replacing reasoning.

This keeps the cognitive work in the room while still reducing frustration.

---

## Design Decisions

I introduce only one new idea per lock.

If students struggle because the structure is too complex, I simplify the data model. For example, I may use parallel lists instead of a list of dictionaries. The goal is to reinforce reasoning, not overwhelm them with nested syntax.

The final lock combines earlier ideas instead of introducing something new.

Difficulty should come from thinking, not from decoding structure.

---

## Bonus Challenges

Bonus sections are optional.

They introduce stretch ideas, like a while loop, without affecting the main password. This allows stronger students to go further without increasing pressure on everyone else.

---

## Authoring Workflow

I design and test notebooks in VS Code.

Once stable, I upload the .ipynb file to Colab for students.

I avoid editing the same notebook back and forth between environments. VS Code is the authoring space. Colab is the classroom space.

Each version is saved clearly:

* data_vault_v1.ipynb
* data_vault_v2.ipynb

---

## Reflection After Running a Session

After each session, I ask:

* Where did students hesitate?
* Was the issue logic or structure?
* Did the error messages help?
* Did the reference cards reduce AI dependency?
* Did the final challenge feel fair?

I adjust the next version based on those answers.

---

The escape room format creates a contained, serious challenge. The index cards reduce unnecessary dependency. Together, they shift students from outsourcing thinking to practicing it.

If you have feedback, please reach out to me on linkedin: https://www.linkedin.com/in/ruchagokhale or send me an email at rucha@indyri.se. Thanks so much!