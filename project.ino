String data = "";

#define GREEN_LED 23
#define RED_LED 4
#define RED_LED2 5
#define RED_LED3 18
#define BUZZER 19

void setup() {

  Serial.begin(115200);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(RED_LED2, OUTPUT);
  pinMode(RED_LED3, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  allOff();
}

void loop() {

  if (Serial.available()) {

    data = Serial.readStringUntil('\n');

    data.trim();

    Serial.println(data);

    // =====================
    // FOCUS
    // =====================

    if (data == "FOCUS") {

      allOff();

      digitalWrite(GREEN_LED, HIGH);
    }

    // =====================
    // SHUTDOWN
    // =====================

    else if (data == "SHUTDOWN") {

      allOff();

      digitalWrite(RED_LED, HIGH);
    }

    // =====================
    // BREAK
    // =====================

    else if (data == "BREAK") {

      allOff();

      digitalWrite(RED_LED2, HIGH);
      digitalWrite(RED_LED3, HIGH);

      digitalWrite(BUZZER, HIGH);

      delay(1000);

      digitalWrite(BUZZER, LOW);
    }

    // =====================
    // RESET
    // =====================

    else if (data == "RESET") {

      allOff();
    }
  }
}

void allOff() {

  digitalWrite(GREEN_LED, LOW);

  digitalWrite(RED_LED, LOW);

  digitalWrite(RED_LED2, LOW);

  digitalWrite(RED_LED3, LOW);

  digitalWrite(BUZZER, LOW);
}