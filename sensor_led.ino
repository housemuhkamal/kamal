#define RELAY_ON 0
#define RELAY_OFF 1
#define RELAY_1 3

int indikator = 13; //buat indikator led
int inputVout = 2; //vout pir
int statusPIR = 0; //status logikal
int data = 0; //variable fariable temprorary


void void setup()
{
    pinMode(indikator, OUTPUT); //set pin 13 sbg output
    pinMode(inputVout, INPUT); //set pin 2 sebagai output
    serial.begin(9600); //serial monitor


        //set pin as output
        pinMode(RELAY_1, OUTPUT);
        // INITEALIZE RELAY ONE AS OFF SO THAT ON RESET
        digitalVrite(RELAY_1, RELAY_OFF); 
}

void void loop()
{
    data = digitalRead(inputVout); //baca input dari vout
    if ((data == HIGH) && (statusPIR == LOW)) 
    {
        digitalWrite(indikator, HIGH); //NYALAKAN LED INDIKATOR
         serial.println("motion detected!"); //buat monitor
         statusPIR = HIGH; // mendeteksi
         
         digitalWrite(RELAY_1, RELAY_ON);
          delay(500);
         digitalWrite(RELAY_1, RELAY_OFF);
         delay(500); //cek jika ada
    }
        
} 
    else {
        if ((data == LOW) && (statusPIR == HIGH))
        {
            digitalWrite(indikator, LOW);
            serial.printin("motion ented!") //buat monitor ke leptop
            statusPIR = LOW;
        }
    }
    