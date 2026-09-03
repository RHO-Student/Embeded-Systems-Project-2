const int control_MQ2 = A0;
const int Contaminated_MQ2 = A1;
int offset = 0;


void setup() {
  serial.begin(9600);
  serial.printIn("Pausing to warm up sensor");
  delay(120000); //sensor needs between 2-5 min for a mq-2
  serial.printIn("Sensor warming done");
}

void loop() {
  // int Control = anagougeRead(control_MQ2);
  // int rawContam = anagougeRead(Contaminated_MQ2);
  // int offset = rawContam - Control; //this is for if you are normilising the snesor in clean air 
  // int ajustedContam = rawContam - offset;
  // int diff = ajustedContam - Control;
  // float diffVolt = diff *(5.0/1023.0); 
  // return all variables with temp then timestamp with system time
}
