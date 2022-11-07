//Blink program for onboard LED on esp32
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

#ifndef STASSID
#define STASSID "Galaxy A50s904F"
#define STAPSK  "borahae7"
#endif
const char* ssid = STASSID;
const char* password = STAPSK;

#define F_pin 2
#define X_pin 4
#define Y_pin 5

#define CLK_pin 13
#define CLK_TP 4000

int F,X,Y;

void OTAsetup() {
WiFi.mode(WIFI_STA);
WiFi.begin(ssid,password);
while(WiFi.waitForConnectResult() != WL_CONNECTED) {
delay(5000);
ESP.restart();
}
ArduinoOTA.begin();
}

void OTAloop() {
ArduinoOTA.handle();
}

void setup() {
OTAsetup();

  pinMode(F_pin,OUTPUT);
  pinMode(X_pin,INPUT);
  pinMode(Y_pin,INPUT);
  // put your setup code here, to run once:
}

void loop() {
OTAloop();
delay(10);
  X = digitalRead(X_pin);
  Y = digitalRead(Y_pin);

  F = (X&&Y) || (X&&!Y) || (!X&&!Y);
  digitalWrite(F_pin,F);

  digitalWrite(CLK_PIN, 0);
  delay(CLK_TP/2);
  digitalWrite(CLK_PIN, 1);
  delay(CLK_TP/2);
  // put your main code here, to run repeatedly:
}
