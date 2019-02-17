
//Libraries
#include <DHT.h>;
#include <SoftwareSerial.h>
SoftwareSerial SIM900A(11,10); // TX | RX

//Constants
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino

//Variables
int chk;
float humidity_1;  //Stores humidity value
float temperature_1; //Stores temperature value
int sensor_pin = A0;
int moisture_1 ;

void setup() {

   Serial.begin(9600);
   while(!Serial);

   SIM900A.begin(9600);  

//   Serial.println("Reading From the Sensor ...");
   dht.begin();

   start_gsm();
   
   delay(2000);

}


void start_gsm() {

    SIM900A.println("AT"); /* Check Communication */
    delay(4000);
    
    
    SIM900A.println("AT+CPIN?"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(4000);
    
    
    SIM900A.println("AT+COPS?");  /* Single TCP/IP connection mode */
    delay(4000);
    
    
    SIM900A.println("AT+CREG?"); /* Attach to GPRS Service */
    delay(4000);
    
    
    SIM900A.println("AT+CGATT?"); /* Network registration status */
    delay(4000);
    
    
    SIM900A.println("AT+CIPSTATUS");  /* Attached to or detached from GPRS service */ 
    delay(4000);
    
    
    SIM900A.println("AT+CIPMUX=0"); /* Start task and set APN */
    delay(4000);
    
    
    SIM900A.println("AT+CSTT=\"airtelgprs.com\",\"\",\"\""); /* Bring up wireless connection with GPRS */
    delay(4000);
    
    
    SIM900A.println("AT+CIICR"); /* Get local IP address */
    delay(4000);
    
    
    SIM900A.println("AT+CIFSR");  /* Start up TCP connection */
    delay(4000);
    
    
    SIM900A.println("AT+SAPBR=1,1"); /* Send data through TCP connection */
    delay(4000);

    SIM900A.println("AT+SAPBR=2,1"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(4000);
    
    
    SIM900A.println("AT+HTTPINIT"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(4000);
}


void loop() {

   moisture_1 = analogRead(sensor_pin);

   moisture_1 = map(moisture_1,800,400,0,100);

//   Serial.print("Mositure : ");
//
//   Serial.print(moisture_1);
//
//   Serial.println("%");

   //Read data and store it to variables hum and temp
    humidity_1 = dht.readHumidity();
    temperature_1 = dht.readTemperature();
    //Print temp and humidity values to serial monitor
//    Serial.print("Humidity: ");
//    Serial.print(humidity_1);
//    Serial.print(" %, Temp: ");
//    Serial.print(temperature_1);
//    Serial.println(" Celsius");




    String url = "AT+HTTPPARA=\"URL\",\"http://my_ip/route?";

    // Moisture sensor values reading
    
//    moisture_0 = analogRead(sensor_pin0);
//    moisture_1 = analogRead(sensor_pin1);
//    moisture_2 = analogRead(sensor_pin2);
//    //moisture_3 = analogRead(sensor_pin3);
//    //moisture_4 = analogRead(sensor_pin4);
//    
//    // Moisture sensor values calibrating
//    
//    moisture_0 = map(moisture_0,1100,100,0,100);
//    moisture_1 = map(moisture_1,1100,100,0,100);
//    moisture_2 = map(moisture_2,1100,100,0,100);
//    //moisture_3 = map(moisture_3,1100,100,0,100);
//    //moisture_4 = map(moisture_4,1100,100,0,100);
//    
    url = url + "moisture_1=" + moisture_1 + "&&";
//    url = url + "moisture_1=" + moisture_1 + "&&";
//    url = url + "moisture_2=" + moisture_2;
    //url = url + "moisture_3=" + moisture_3 + "&&";
    //url = url + "moisture_4=" + moisture_4 + "&&";
    
    
    // Humidity and Temperature Sensor initializing
    
    //int chk1 = DHT1.read11(DHT11_PIN1);
    //int chk2 = DHT2.read11(DHT11_PIN2);
    
    // Humidity and Temperature Sensor reading
    
    //int humidity_1 = DHT1.humidity;
    //int humidity_2 = DHT2.humidity;
    
    //int temperature_1 = DHT1.temperature;
    //int temperature_2 = DHT2.temperature;
    
    url = url + "humidity_1=" + humidity_1 + "&&";
    //url = url + "humidity_2=" + humidity_2 + "&&";
    
    url = url + "temperature_1=" + temperature_1;
    //url = url + "temperature_2=" + temperature_2;


    

    delay(1000);
    
    // Send data to server
    
    
    SIM900A.println("AT+HTTPPARA=\"CID\",1"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(5000);
    
    
    SIM900A.println(url + "\""); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(5000);
    
    
    SIM900A.println("AT+HTTPACTION=0"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(290000);

}
