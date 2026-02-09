#include <Motor.h>

motor Motor;

void setup()
{
  Motor._74HC595D();
  Motor.Motor(Stop, 0);
}

void loop()
{

}