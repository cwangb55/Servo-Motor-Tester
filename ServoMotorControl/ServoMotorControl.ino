#include <Servo.h>


Servo myservo;  // create servo object to control a servo


int potpin = A0;  // analog pin used to connect the potentiometer

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 (D9 on Arduino Nano) to the servo object
//  Serial.begin(9600);  
}


void loop() {
  int val = analogRead(A4);            // reads the potentiometer from Gripper
//  Serial.println(val);

  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)

  val = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
//  Serial.println(val);

  myservo.write(val);                  // sets the servo position according to the scaled value
  delay(15);                           // waits for the servo to get there

}
