#include"ultrasonic.h"
#include"Arduino.h"

void ultrasonic::Init(int trigPin, int echoPin)
{
    _trigPin = trigPin;
    _echoPin = echoPin;
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

float ultrasonic::Ranging()
{
    digitalWrite(_trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(_trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(_trigPin, LOW);
    float distance = pulseIn(_echoPin, HIGH) / 58.00;
    delay(10);
    return distance;
}