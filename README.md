# Robotics 101

Classroom resources for introductory robotics education using the Acebott ESP32 Car Shield.

This repository contains libraries, tools, and projects designed to support hands-on learning in middle and high school robotics courses.

## 📚 Repository Contents

### [Arduino Diagnostic Test](./Arduino%20Diagnostic%20Test)

An interactive web-based practice exam designed to help students prepare for the official [Arduino Fundamentals Certification](https://www.arduino.cc/education/certification).

**Features:**
- 36 multiple-choice questions covering 8 Arduino topics
- 75-minute countdown timer matching real exam format
- Free navigation between questions
- Instant feedback and scoring
- Built with React + Vite

📖 **[View Documentation →](./Arduino%20Diagnostic%20Test/README.md)**

---

### [Acebott ESP32 Car Shield Library](./arduino/libraries/Acebott)

A custom Arduino library for the Acebott ESP32 four-wheel mecanum car kit, rebuilt to work seamlessly with Arduino Cloud.

**What's Fixed:**
- Added `Motor.h` abstraction for compatibility
- Replaced unavailable SR04.h dependency with bundled ultrasonic.h
- Corrected header-casing mismatches for Linux build agents
- Single zip import for classroom reliability

**Use Cases:**
- Arduino Cloud projects with Acebott hardware
- Local Arduino IDE development
- Classroom robotics projects requiring reliable library imports

📖 **[View Documentation →](./arduino/libraries/Acebott/README.md)**

---

## 🎯 Educational Context

These resources are designed for **Robotics 101** courses teaching:
- Arduino programming fundamentals
- Embedded systems with ESP32
- Mecanum wheel robotics
- Sensor integration (ultrasonic, motors, servos)
- Arduino Certification preparation

## 🚀 Quick Start

### For Students
1. **Practicing for Arduino Certification?** → Check out the [Arduino Diagnostic Test](./Arduino%20Diagnostic%20Test/README.md)
2. **Building with Acebott Car Shield?** → Install the [Acebott Library](./arduino/libraries/Acebott/README.md)

### For Educators
- Each project includes detailed README files with setup instructions
- Tools are designed for classroom deployment and reliability
- All resources support both individual and collaborative learning

## 📂 Repository Structure

```
robotics101/
├── Arduino Diagnostic Test/     # Practice exam for Arduino certification
│   ├── tools/
│   │   └── arduino-diagnostic/  # React web application
│   ├── README.md               # Full documentation
│   └── SETUP_INSTRUCTIONS.md   # Deployment guide
│
└── arduino/
    └── libraries/
        └── Acebott/             # Custom Arduino library
            ├── src/             # Library source code
            ├── examples/        # Example sketches
            └── README.md        # Library documentation
```

## 🤝 Contributing

This is an educational project developed for classroom use. If you find bugs, have suggestions, or want to contribute improvements:

1. Check existing issues
2. Open a new issue describing your suggestion
3. For code contributions, submit a pull request

## 📝 License

Developed for educational use in Robotics 101 courses.

---

**Questions?** Open an issue or reach out to the course instructors.
