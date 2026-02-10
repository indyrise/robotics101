# Arduino Certification Diagnostic Test

An interactive web-based practice exam designed to help students prepare for the official [Arduino Fundamentals Certification](https://www.arduino.cc/education/certification).

## Overview

This tool provides a realistic exam experience with 36 multiple-choice questions covering all 8 official Arduino certification categories. Perfect for middle and high school students preparing to demonstrate their Arduino competency.

## Features

- **75-minute countdown timer** - Matches the real certification exam format
- **36 comprehensive questions** across 8 key Arduino topics:
  - Electricity (5 questions)
  - Circuits & Schematics (3 questions)
  - Arduino Boards (4 questions)
  - Arduino IDE (4 questions)
  - Electronic Components (6 questions)
  - Programming Syntax & Semantics (5 questions)
  - Programming Logic (6 questions)
  - PWM & Frequency (3 questions)
- **Free navigation** - Move between questions at any time
- **Progress tracking** - See which questions you've answered
- **Instant feedback** - Review your results at the end

## Tech Stack

This is a React application built with:
- React + Vite
- Modern JavaScript (ES6+)
- Responsive design for desktop and tablet

## Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:
```bash
cd "Arduino Diagnostic Test/tools/arduino-diagnostic"
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser to the URL shown (typically `http://localhost:5173`)

### Building for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

## Usage

1. Click "Start Test" to begin the 75-minute timer
2. Answer questions by selecting radio buttons
3. Use the question navigator to jump between questions
4. Click "Submit Test" when finished
5. Review your score and see which questions you got right/wrong

## Educational Context

This diagnostic tool is designed for use in **Robotics 101** courses teaching introductory Arduino programming and electronics. It helps students:
- Identify knowledge gaps before taking the official certification
- Get comfortable with the exam format and timing
- Build confidence in their Arduino fundamentals
- Practice under realistic test conditions

## Additional Setup Instructions

For detailed deployment instructions, see [SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md).

## Contributing

This is an educational project. If you find errors in questions or have suggestions for improvement, please open an issue.

## License

For educational use in Robotics 101 courses.

---

**Part of the [Robotics 101](../..) curriculum**
