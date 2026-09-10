const int control_MQ2 = A0;
const int Contaminated_MQ2 = A1;
int inital_Control =131;
int initial_Contam = 172;
int sensor_Offset;
int diff;

void setup() {
  Serial.begin(9600);
  //Serial.print("Pausing to warm up sensor");
  //delay(120000);  //sensor needs between 2-5 min for a mq-2
  //Serial.print("Sensor warming done");
  //inital_Control = analogRead(control_MQ2);
  //initial_Contam = analogRead(Contaminated_MQ2);
  sensor_Offset = initial_Contam - inital_Control;  //moved to normalise the sensor at the start
}

void loop() {
  if (Serial.available() > 0) {
    Serial.read();  //clears the serial line to avoid running multipule timer
    detect();
  }
}

void detect() {
  int Control = analogRead(control_MQ2);
  int rawContam = analogRead(Contaminated_MQ2);
  int ajustedContam = rawContam - sensor_Offset;
  diff = ajustedContam - Control;
  float rawvolt = rawContam * (5.0 / 1023.0);
  float diffVolt = diff * (5.0 / 1023.0);
  Serial.print(inital_Control);
  Serial.print(",");
  Serial.print(initial_Contam);
  Serial.print(",");
  Serial.print(sensor_Offset);
  Serial.print(",");
  Serial.print(Control);
  Serial.print(",");
  Serial.print(rawContam);
  Serial.print(",");
  Serial.print(ajustedContam);
  Serial.print(",");
  Serial.print(diff);
  Serial.print(",");
  Serial.print(rawvolt);
  Serial.print(",");
  Serial.print(diffVolt);
  if (diff > 245) {
    Serial.print(",");
    Serial.print("HIGH");
  } else if (diff > 82) {
    Serial.print(",");
    Serial.print("MEDIUM");
  } else if (diff > 30) {
    Serial.print(",");
    Serial.print("LOW");
  } else {
    Serial.print(",");
    Serial.print("NORMAL");
  }
  //return all variables with temp then timestamp with system time
  // note that the break points for future use are <30 /0.15V diff means clean air
  // 30 /0.15v - 82/0.40v light contamination (not visalbe gas small flame of smoke)
  // 83/0.41v - 245/1.20v medium contamination (Clear presnase of vaopor or somke)
  // >245 / 1.20v High contamination (not safe clear heavy somke or toxic gas)
}
