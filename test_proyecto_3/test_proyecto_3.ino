//Declare pins
int arriba = 2;
int abajo = 3;
int izquierda = 4;
int derecha = 5;
int planta = 9;
int nuez = 8 ;
int zombie1 = 6;
int zombie2 = 7;
int listo = 10;
int led = 11;


void setup() {
  Serial.begin(9600);
  pinMode(arriba, INPUT);
  pinMode(abajo, INPUT);
  pinMode(izquierda, INPUT);
  pinMode(derecha, INPUT);
  pinMode(planta, INPUT);
  pinMode(nuez, INPUT);
  pinMode(zombie1, INPUT);
  pinMode(zombie2, INPUT);
  pinMode(listo, INPUT);
  pinMode(led,OUTPUT);
  

}

void loop() {
 //read values from color buttons JOYSTICK
  int arrBtn = digitalRead(arriba);
  int abjBtn = digitalRead(abajo);
  int izqBtn = digitalRead(izquierda);
  int derBtn = digitalRead(derecha);
  // botones
  int pltBtn = digitalRead(planta);
  int nueBtn = digitalRead(nuez);
  int zomb1Btn = digitalRead(zombie1);
  int zomb2Btn = digitalRead(zombie2);
  int listoBtn = digitalRead(listo);
  

if (arrBtn == HIGH){
  Serial.println("arriba%");
delay(100);
}
if (abjBtn == HIGH){
  Serial.println("abajo%");
delay(100);
}

if (izqBtn == HIGH){
  Serial.println("izquierda%");
delay(100);
}

if (derBtn == HIGH){
  Serial.println("derecha%");
delay(100);
}
if (pltBtn == HIGH){
  Serial.println("planta%");
  digitalWrite(led,LOW);
delay(100);
}
if (nueBtn == HIGH){
  Serial.println("nuez%");
  digitalWrite(led,LOW);
delay(100);
}
if (zomb1Btn == HIGH){
  Serial.println("zombie1%");
  digitalWrite(led,LOW);
delay(100);
}
if (zomb2Btn == HIGH){
  Serial.println("zombie2%");
  digitalWrite(led,LOW);
  
}
if (listoBtn == HIGH){
  Serial.println("listo%");
  digitalWrite(led,HIGH);
delay(100);
}
else{
  Serial.println("No hay nada");
  delay(100);
}

}
