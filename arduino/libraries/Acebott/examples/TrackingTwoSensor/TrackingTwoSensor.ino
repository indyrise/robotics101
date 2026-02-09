#include <Motor.h>

#define Left_Line           35
#define Center_Line         36
#define Right_Line          39 

int Left_Tra_Value;
int Center_Tra_Value;
int Right_Tra_Value;
int Black_Line = 2000;
int Off_Road = 4000;
int Speed = 150;
int RotateSpeed = 150;

motor Motor;

void setup()
{
    Serial.begin(115200);
    Motor._74HC595D();
    pinMode(Left_Line, INPUT);
    pinMode(Center_Line, INPUT);
    pinMode(Right_Line, INPUT);
    Motor.Motor(Stop, 0);
}

void loop()
{
    Left_Tra_Value = analogRead(Left_Line);
    Center_Tra_Value = analogRead(Center_Line);
    Right_Tra_Value = analogRead(Right_Line);
    delay(10);
    //Serial.println(Left_Tra_Value);Serial.println(Center_Tra_Value);Serial.println(Right_Tra_Value);delay(1000);

    if (Left_Tra_Value < Black_Line && Right_Tra_Value < Black_Line)
    {
        Motor.Motor(Forward, Speed);
    }
    else if (Left_Tra_Value >= Black_Line && Right_Tra_Value < Black_Line)
    {
        Motor.Motor(Contrarotate, RotateSpeed);
    }
    else if (Left_Tra_Value < Black_Line && Right_Tra_Value >= Black_Line)
    {
        Motor.Motor(Clockwise, Speed);
    }
    else if (Left_Tra_Value >= Black_Line && Left_Tra_Value < Off_Road && Right_Tra_Value >= Black_Line && Right_Tra_Value < Off_Road)
    {
        Motor.Motor(Forward, Speed);
    }
    else if (Left_Tra_Value >= Off_Road && Right_Tra_Value >= Off_Road)
    {
        Motor.Motor(Stop, 0);
    }
}
