#include <Arduino.h>
#include<Servo.h>

Servo serFirst;

String serialData;

void setup() {

  serFirst.attach(11);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {

}

void serialEvent() {
  serialData = Serial.readString();
  serFirst.write(parseDataToVar(serialData));
}

int parseDataToVar(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}
