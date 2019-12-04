// Based on example code from the arduino_hexbug_spider project
//   Copyright (c) 2014 José Carlos Nieto, https://menteslibres.net/xiam
//   Used under permission.
// Derivative changes Copyright (c) 2017 Pablo Duboue, http://duboue.net

// Channel the Hexbug Spider is listenning to ('A' or 'B').
#define HEXBUG_SPIDER_CHANNEL 'A'
// How many times does a rotation code needs to be send to complete a full
// turn? This number was made up based on experimentation.
#define HEXBUG_FULL_ROTATION 18
// The number of milliseconds to wait after sending an instruction. This number
// was also made up based on experimentation.
#define HEXBUG_DELAY_AFTER_INSTRUCTION 192
// IR codes and utilities for Hexbug Spider.
#include "hexbug_spider.h"

// Pin the IR LED is         wired to. Must be a PWM pin.
#define PIN_IR_OUTPUT    3

#define CPU_PRESCALE(n) (CLKPR = 0x80, CLKPR = (n))
#define CPU_16MHz       0x00
#define CPU_8MHz        0x01
#define CPU_4MHz        0x02
#define CPU_2MHz        0x03
#define CPU_1MHz        0x04
#define CPU_500kHz      0x05
#define CPU_250kHz      0x06
#define CPU_125kHz      0x07
#define CPU_62kHz       0x08

void setup(void)
{
  Serial.begin(9600);
  Serial.println("Make sure your HexBug spider is within the IR LED's range.");

  hexbug_spider_setup_pin(PIN_IR_OUTPUT);
}

void loop(void) {

  // send data only when you receive data:
  if (Serial.available() > 0) {
     // read the incoming byte:
     int incomingByte = Serial.read();
     int returnChar = Serial.read();
     
     // say what you got:
     Serial.print("I received: ");
     Serial.println(incomingByte, DEC);
     
     if(incomingByte == 'R'){
       Serial.println("Spin right");
       hexbug_spider_spin(-25);
     }
     
     if(incomingByte == 'L'){
       Serial.println("Spin left");
       hexbug_spider_spin(25);
     }
     
     if(incomingByte == 'F'){
       Serial.println("Advance");
       hexbug_spider_advance(-1);
     }

     if(incomingByte == 'B'){
      Serial.println("Back");
      hexbug_spider_advance(1);
     }
  }
}
