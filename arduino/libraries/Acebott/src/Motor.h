#ifndef _MOTOR_H__
#define _MOTOR_H__

#include "Arduino.h"
#include "Vehicle.h"

// A thin compatibility wrapper used by Acebott example sketches.
// It delegates to the existing vehicle driver implementation
// (74HC595 direction + PWM speed) defined in Vehicle.h / vehicle.cpp.

class motor
{
public:
    // Historical name used in examples. Initializes the motor control pins.
    void _74HC595D();

    // Drive the car using direction constants from Vehicle.h (Forward, Backward, Stop, Clockwise, Contrarotate, etc.)
    void Motor(int Dir, int Speed);

private:
    vehicle _veh;
};

#endif
