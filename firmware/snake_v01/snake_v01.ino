/*
 * Proyecto Serpiente — Firmware v0.1 (skeleton)
 *
 * Gait serpentina básico + placeholder para control Bluetooth.
 * Requiere: Adafruit PWM Servo Driver Library
 *
 * TODO:
 * - Integrar Bluetooth (BluetoothSerial o Bluepad32)
 * - Integrar ESP32-CAM streaming
 * - Ajustar amplitud, frecuencia y phase lag según el hardware real
 */

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

const int NUM_SERVOS = 6;          // Ajustar a la cantidad real
const int SERVO_MIN = 150;         // Pulse width mínimo (ajustar)
const int SERVO_MAX = 600;         // Pulse width máximo (ajustar)
const int SERVO_CENTER = 375;      // Centro aproximado

float amplitude = 40.0;            // Grados de amplitud
float frequency = 0.8;             // Hz
float phaseLag = 0.8;              // Desfase entre segmentos (rad)
unsigned long lastUpdate = 0;
const unsigned long interval = 20; // ms

void setup() {
  Serial.begin(115200);
  pwm.begin();
  pwm.setPWMFreq(50);              // 50 Hz para servos

  // Centrar todos los servos al iniciar
  for (int i = 0; i < NUM_SERVOS; i++) {
    setServoAngle(i, 90);
  }
  delay(1000);
}

void loop() {
  if (millis() - lastUpdate >= interval) {
    lastUpdate = millis();
    float t = millis() / 1000.0;

    for (int i = 0; i < NUM_SERVOS; i++) {
      float angle = 90 + amplitude * sin(2 * PI * frequency * t - i * phaseLag);
      setServoAngle(i, angle);
    }
  }

  // TODO: leer comandos Bluetooth para cambiar amplitud, frecuencia, modo, etc.
}

void setServoAngle(int channel, float angle) {
  angle = constrain(angle, 0, 180);
  int pulse = map(angle, 0, 180, SERVO_MIN, SERVO_MAX);
  pwm.setPWM(channel, 0, pulse);
}
