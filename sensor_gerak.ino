//membuat dua fariable 
int buzz = 13;
int pir = 8;
int val ;

void setup()
{
    pinMode(buzz, OUTPUT);
    pinMode(pir, INPUT);
}

void loop()
{
    val = digitalRead(pir);
    if (val == 1){
        digitalWrite(buzz, 1);
    }
    else{
        digitalWrite(buzz,0);
    }
}