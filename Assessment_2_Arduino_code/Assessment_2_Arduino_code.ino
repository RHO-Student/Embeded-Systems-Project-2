const int control_MQ2 = A0;
const int Contaminated_MQ2 = A1;
int offset = 0;


void setup() {
  Serial.begin(9600);
  Serial.print("Pausing to warm up sensor");
  delay(120000); //sensor needs between 2-5 min for a mq-2
  Serial.print("Sensor warming done");
}

void loop() {
  int Control = analogRead(control_MQ2);
  int rawContam = analogRead(Contaminated_MQ2);
  int offset = rawContam - Control; //this is for if you are normilising the snesor in clean air 
  int ajustedContam = rawContam - offset;
  int diff = ajustedContam - Control;
  float diffVolt = diff *(5.0/1023.0); 
  Serial.print(Control);
  Serial.print(",");
  Serial.print(rawContam);
  Serial.print(",");
  Serial.print(offset);
  Serial.print(",");
  Serial.print(ajustedContam);
  Serial.print(",");
  Serial.print(diff);
  Serial.print(",");
  Serial.print(diffVolt);
  //return all variables with temp then timestamp with system time
}
