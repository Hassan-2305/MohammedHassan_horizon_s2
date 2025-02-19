#include <Servo.h>
Servo servo_1;
Servo servo_2;
Servo servo_3;
Servo servo_4;
Servo servo_5;
Servo servo_6;

void setup() {
    Serial.begin(9600);
    servo_1.attach(3);
    servo_2.attach(5);
    servo_3.attach(6);
    servo_4.attach(9);
    servo_5.attach(10);
    servo_6.attach(11);
    Serial.println("enter the angle a,b,c,d,e,f");

    servo_1.write(0);
    servo_2.write(0);
    servo_3.write(0);
    servo_4.write(0);
    servo_5.write(0);
    servo_6.write(0);
}

void loop() {
    if (Serial.available() > 0) {
        int a = Serial.parseInt();
        int b = Serial.parseInt();
        int c = Serial.parseInt();
        int d = Serial.parseInt();
        int e = Serial.parseInt();
        int f = Serial.parseInt();
            if(a >= 0 && a <= 180) {
                servo_1.write(a);
            }
            if(b >= 0 && b <= 180) {
                servo_2.write(b);
            }
            if(c >= 0 && c <= 180) {
                servo_3.write(c);
            }
            if(d >= 0 && d <= 180) {
                servo_4.write(d);
            }
            if(e >= 0 && e <= 180) {
                servo_5.write(e);
            }
            if(f >= 0 && f <= 180) {
                servo_6.write(f);
            }
    }
    delay(25);
}
