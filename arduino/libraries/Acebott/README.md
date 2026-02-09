# Acebott ESP32 Car Shield – Arduino Cloud compatible

Custom library for the Acebott four-wheel mecanum car kit (ESP32).

This is a **fixed** version of the vendor library, rebuilt to compile cleanly
in Arduino Cloud's Linux-based build environment.

## What was fixed

- Added `Motor.h` / `Motor.cpp` – a thin wrapper expected by example sketches.
- Replaced `SR04.h` dependency with the bundled `ultrasonic.h`.
- Corrected header-casing mismatches (`Vehicle.h`) so builds succeed on
  case-sensitive filesystems.

## Quick start (Arduino Cloud)

1. Zip this folder.
2. **Libraries → Custom → Import** the zip.
3. `#include <Motor.h>` in your sketch.

## Contents

| File | Purpose |
|---|---|
| `src/Vehicle.h` / `vehicle.cpp` | Low-level 74HC595 + PWM motor driver |
| `src/Motor.h` / `Motor.cpp` | Compatibility wrapper used by examples |
| `src/ultrasonic.h` / `ultrasonic.cpp` | HC-SR04 ultrasonic sensor driver |
| `src/MY1690.h` / `MY1690.cpp` | MY1690 MP3 module driver |

## License

See [LICENSE](LICENSE).
