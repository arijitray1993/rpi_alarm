void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(31, OUTPUT);
}

void buzz(){
  Serial.println("enter");
  digitalWrite(31, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);                       // wait for a second
  digitalWrite(31, LOW);    // turn the LED off by making the voltage LOW
  delay(200);
  digitalWrite(31, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(200);
  digitalWrite(31, LOW);    // turn the LED off by making the voltage LOW
  delay(50);
}

void al_off(){
  digitalWrite(31, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    String command = Serial.readString();

    Serial.println(command);
    if(command=="al_on"){
      while(command!="al_off"){
        buzz();
        command = Serial.readString();
      }
      
    }

    if(command=="al_off"){
      al_off();
    }
    
  }
  
}
