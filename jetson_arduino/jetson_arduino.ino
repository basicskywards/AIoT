#include<Servo.h>
Servo x;
Servo y;
void setup() {
  // put your setup code here, to run once:
x.attach(2);
y.attach(3);
Serial.begin(9600);
x.write(0); // move servo to 0 degrees
//y.write(102);
}

void loop() {
  // put your main code here, to run repeatedly:

  if(Serial.available()>0)
  {
    int inp=Serial.read();
    if(inp=='1')
       left();
       
    else if(inp=='2')
        right();  
  }
}

void left()
{
//  x.write(0);
//  delay(500);
  x.write(180); // turn 180 degrees
//  delay(500);
  delay(180 *  (10.0/3.0)); //delay for max speed
  x.write(0); // turn back into 0 degrees
  delay(500);
  
}

void right()
{
  y.write(152);
  delay(500);
  y.write(102);
  delay(500      );
}
