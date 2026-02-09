#include <MY1690.h>

my1690 MY1690;

void setup()
{
  Serial.begin(9600);
  delay(100);
  MY1690.play();
}

void loop()
{

}
