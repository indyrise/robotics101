#ifndef _ULTRASONIC_H__
#define _ULTRASONIC_H__

                        

class ultrasonic
{   
     public: 
          void Init(int trigPin, int echoPin); 
          float Ranging();
     private:
          int _trigPin;
          int _echoPin;
          
};

#endif
