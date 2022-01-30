const int DRUM_1 = 4;
const int DRUM_2 = 5;
const int DRUM_3 = 6;
const int DRUM_4 = 7;
const int DRUM_5 = 8;
const int LOOP_DELAY = 10;
const int AFTERTOUCH_DELAY = 65;

void setup() {
  pinMode(DRUM_1, INPUT_PULLUP);
  pinMode(DRUM_2, INPUT_PULLUP);
  pinMode(DRUM_3, INPUT_PULLUP);
  pinMode(DRUM_4, INPUT_PULLUP);
  pinMode(DRUM_5, INPUT_PULLUP);
  
  Serial.begin(9600);
}


int lastd1 = 1;
int lastd2 = 1;
int lastd3 = 1;
int lastd4 = 1;
int lastd5 = 1;

void check(int pin, String msg, int& last) {
  int value = digitalRead(pin);
  if(last != value) {
    if(value == 0) {
      Serial.print(msg);
    }
    last = value;
    delay(AFTERTOUCH_DELAY);

  }
}

void loop() {
  check(DRUM_1, "1", lastd1);
  check(DRUM_2, "2", lastd2);
  check(DRUM_3, "3", lastd3);
  check(DRUM_4, "4", lastd4);
  check(DRUM_5, "5", lastd5);  
}
