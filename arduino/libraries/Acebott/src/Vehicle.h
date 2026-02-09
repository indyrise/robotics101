#ifndef _VEHICLE_H__
#define _VEHICLE_H__

#define PWM1_PIN            19
#define PWM2_PIN            23
#define SHCP_PIN            18                          
#define EN_PIN              16                            
#define DATA_PIN            5                           
#define STCP_PIN            17                            

const int Forward           = 163;           // forward
const int Backward          = 92;            // back
const int Move_Left         = 106;           // left translation
const int Move_Right        = 149;           // Right translation 
const int Top_Left          = 34;            // Upper left mobile
const int Bottom_Left       = 72;            // Lower left mobile
const int Top_Right         = 129;           // Upper right mobile
const int Bottom_Right      = 20;            // The lower right move
const int Stop              = 0;             // stop
const int Contrarotate      = 83;            // Counterclockwise rotation
const int Clockwise         = 172;           // Rotate clockwise
const int Moedl1            = 25;            // model1
const int Moedl2            = 26;            // model2
const int Moedl3            = 27;            // model3
const int Moedl4            = 28;            // model4
const int MotorLeft         = 230;           // servo turn left
const int MotorRight        = 231;           // servo turn right
const int M1_Forward        = 128;
const int M1_Backward       = 64;
const int M2_Forward        = 32;
const int M2_Backward       = 16;
const int M3_Forward        = 2;
const int M3_Backward       = 4;
const int M4_Forward        = 1;
const int M4_Backward       = 8;

class vehicle
{   
     public: 
          void Init();        
          void Move(int Dir, int Speed);
     private:
          
};

#endif
