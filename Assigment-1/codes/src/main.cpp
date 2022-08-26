#include <Arduino.h>
int X,Y,F;
void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(5, OUTPUT);
  // put your setup code here, to run once:
}

void loop() {
 X= digitalRead(2);
 Y= digitalRead(3);
 F=(X&&Y) || (X&&!Y) || (!X&&!Y);
 if(F==1){
     digitalWrite(5,HIGH);
  }
 else{
     digitalWrite(5,LOW);
  }
  // put your main code here, to run repeatedly:
}
