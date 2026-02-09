#include "Motor.h"

void motor::_74HC595D()
{
    _veh.Init();
}

void motor::Motor(int Dir, int Speed)
{
    _veh.Move(Dir, Speed);
}
