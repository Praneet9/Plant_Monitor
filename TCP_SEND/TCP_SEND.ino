#include <SoftwareSerial.h>
SoftwareSerial SIM900A(11,10); // TX | RX
// Connect the SIM900A TX to Arduino pin 11. 
// Connect the SIM900A RX to Arduino pin 10. 

#include<dht.h>
dht DHT1;
//dht DHT2;

#define DHT11_PIN1 3 
//define DHT11_PIN2 4 

char c = ' ';

int sensor_pin0 = A0;
int sensor_pin1 = A1;
int sensor_pin2 = A2;
int sensor_pin3 = A3;
int sensor_pin4 = A4;
int moisture_0, moisture_1, moisture_2, moisture_3, moisture_4 ;

String url = "AT+HTTPPARA=\"URL\",\"http://eb3481c8.ngrok.io/test?";

void setup() 
{

    // start th serial communication with the host computer
    
    Serial.begin(9600);
    while(!Serial);
    
    // start communication with the SIM900A in 9600
    
    SIM900A.begin(9600);  
    delay(1000);

}


void loop() {

    // Moisture sensor values reading
    
    moisture_0 = analogRead(sensor_pin0);
    moisture_1 = analogRead(sensor_pin1);
    moisture_2 = analogRead(sensor_pin2);
    moisture_3 = analogRead(sensor_pin3);
    moisture_4 = analogRead(sensor_pin4);
    
    // Moisture sensor values calibrating
    
    moisture_0 = map(moisture_0,1100,100,0,100);
    moisture_1 = map(moisture_1,1100,100,0,100);
    moisture_2 = map(moisture_2,1100,100,0,100);
    moisture_3 = map(moisture_3,1100,100,0,100);
    moisture_4 = map(moisture_4,1100,100,0,100);
    
    url = url + "moisture_0=" + String(moisture_0) + "&&";
    url = url + "moisture_1=" + String(moisture_1) + "&&";
    url = url + "moisture_2=" + String(moisture_2) + "&&";
    url = url + "moisture_3=" + String(moisture_3) + "&&";
    url = url + "moisture_4=" + String(moisture_4) + "&&";
    
    delay(2000);
    
    // Humidity and Temperature Sensor initializing
    
    int chk1 = DHT1.read11(DHT11_PIN1);
    //int chk2 = DHT2.read11(DHT11_PIN2);
    
    // Humidity and Temperature Sensor reading
    
    int humidity_1 = DHT1.humidity;
    //int humidity_2 = DHT2.humidity;
    
    int temperature_1 = DHT1.temperature;
    //int temperature_2 = DHT2.temperature;
    
    url = url + "humidity_1=" + String(humidity_1) + "&&";
    //url = url + "humidity_2=" + String(humidity_2) + "&&";
    
    url = url + "temperature_1=" + String(temperature_1) + "&&";
    //url = url + "temperature_2=" + String(temperature_2) + "&&";
    
    delay(2000);
    
    // Send data to server
    
    SIM900A.println("AT"); /* Check Communication */
    delay(2000);
    
    SIM900A.println("AT+CPIN?"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(2000);
    
    SIM900A.println("AT+COPS?");  /* Single TCP/IP connection mode */
    delay(2000);
    
    SIM900A.println("AT+CREG?"); /* Attach to GPRS Service */
    delay(2000);
    
    SIM900A.println("AT+CGATT?"); /* Network registration status */
    delay(2000);
    
    SIM900A.println("AT+CIPSTATUS");  /* Attached to or detached from GPRS service */ 
    delay(2000);
    
    SIM900A.println("AT+CIPMUX=0"); /* Start task and set APN */
    delay(2000);
    
    SIM900A.println("AT+CSTT=\"airtelgprs.com\",\"\",\"\""); /* Bring up wireless connection with GPRS */
    delay(2000);
    
    SIM900A.println("AT+CIICR"); /* Get local IP address */
    delay(2000);
    
    SIM900A.println("AT+CIFSR");  /* Start up TCP connection */
    delay(2000);
    
    SIM900A.println("AT+SAPBR=1,1"); /* Send data through TCP connection */
    delay(2000);
    
    SIM900A.println("AT+SAPBR=2,1"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(2000);
    
    SIM900A.println("AT+HTTPINIT"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(2000);
    
    SIM900A.println("AT+HTTPPARA=\"CID\",1"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(2000);
    
    SIM900A.println(url + "\""); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(2000);
    
    SIM900A.println("AT+HTTPACTION=0"); /* Non-Transparent (normal) mode for TCP/IP application */
    delay(2000);

}
