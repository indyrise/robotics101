# robotics101

Classroom resources for introductory robotics with the Acebott ESP32 Car Shield.

## Repository layout

```
arduino/
  libraries/
    Acebott/          # Custom library – Arduino Cloud compatible
```

## Acebott ESP32 Car Shield library

`arduino/libraries/Acebott/` contains a custom Arduino library for the
Acebott ESP32 four-wheel mecanum car kit. It is intended to be imported as a
custom library in **Arduino Cloud** (or used locally with the Arduino IDE).

### Why this library exists

The vendor-supplied Acebott library cannot be used directly in Arduino Cloud
because of several packaging and cross-platform issues:

1. **Missing `Motor.h` abstraction** – example sketches `#include <Motor.h>`,
   but the original library did not ship that header. This library adds a thin
   `Motor` wrapper that delegates to the existing `Vehicle` driver.
2. **`SR04.h` dependency unavailable in Arduino Cloud** – the original
   ultrasonic examples pulled in a third-party `SR04.h` header that is not
   available as a Cloud library. The fixed examples use the bundled
   `ultrasonic.h` instead.
3. **Header-casing mismatches** – filenames like `vehicle.h` vs `Vehicle.h`
   compiled fine on case-insensitive macOS/Windows but broke on the Linux
   build agents used by Arduino Cloud. All `#include` directives now match
   the actual filenames.
4. **Classroom reliability** – students need a single zip import that "just
   works." This library is that single import.

### How to use in Arduino Cloud

1. Download or zip the `arduino/libraries/Acebott/` folder.
2. In Arduino Cloud, go to **Libraries → Custom → Import**.
3. Upload the zip. The library will appear as **acebott**.
4. In your sketch, `#include <Motor.h>` (or any other header listed in
   `library.properties`).
