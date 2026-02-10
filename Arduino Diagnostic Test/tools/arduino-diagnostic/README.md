# Arduino Certification Diagnostic Test

Interactive practice exam matching the official [Arduino Fundamentals Certification](https://www.arduino.cc/education/certification) format.

## What it covers

36 multiple-choice questions across the 8 official exam categories:

| Category | Questions |
|----------|-----------|
| Electricity | 5 |
| Circuits & Schematics | 3 |
| Arduino Boards | 4 |
| Arduino IDE | 4 |
| Electronic Components | 6 |
| Programming Syntax & Semantics | 5 |
| Programming Logic | 6 |
| PWM & Frequency | 3 |

## Features

- 75-minute countdown timer (matches real exam)
- Free navigation between questions
- Flag questions for review
- Per-category score breakdown on completion
- Full answer review with correct answers shown

## Standards alignment

**CSTA:** 2-CS-01, 2-CS-02, 2-AP-10, 2-AP-11, 2-AP-12, 2-AP-13, 2-AP-17, 2-AP-19, 2-DA-08

**NGSS:** MS-PS2-2, MS-PS2-3, MS-PS2-5, MS-PS4-1, MS-PS4-2, MS-ETS1-1, MS-ETS1-2, MS-ETS1-3, MS-ETS1-4

## Run locally

```bash
cd tools/arduino-diagnostic
npm install
npm run dev
```

Opens at `http://localhost:5173`

## Deploy to GitHub Pages

Build the static files:

```bash
npm run build
```

Output goes to `dist/`. See the root README for GitHub Pages setup instructions.
