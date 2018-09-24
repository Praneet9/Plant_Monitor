#include <SoftwareSerial.h>
SoftwareSerial SIM900A(10,11); // RX | TX
// Connect the SIM900A TX to Arduino pin 2 RX. 
// Connect the SIM900A RX to Arduino pin 3 TX. 
char c = ' ';
void setup() 
{
// start th serial communication with the host computer
Serial.begin(9600);
while(!Serial);
Serial.println("Arduino with SIM900A is ready");
// start communication with the SIM900A in 9600
SIM900A.begin(9600); 
Serial.println("SIM900A started at 9600");
delay(1000);
Serial.println("Setup Complete! SIM900A is Ready!");
}
//void loop()
//{
//// Keep reading from SIM800 and send to Arduino Serial Monitor
//if (SIM900A.available())
//{ c = SIM900A.read();
//Serial.write(c);}
//// Keep reading from Arduino Serial Monitor and send to SIM900A
//if (Serial.available())
//{ c = Serial.read();
//SIM900A.write(c); 
//}
//}






void loop() {
  Serial.println("TCP Send :");
  Serial.print("AT\\r\\n");
  SIM900A.println("AT"); /* Check Communication */
  delay(2000);
  ShowSerialData(); /* Print response on the serial monitor */
  delay(2000);
  Serial.print("AT+CPIN?\\r\\n");
  SIM900A.println("AT+CPIN?"); /* Non-Transparent (normal) mode for TCP/IP application */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+COPS?\\r\\n");
  SIM900A.println("AT+COPS?");  /* Single TCP/IP connection mode */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+CREG?\\r\\n");
  SIM900A.println("AT+CREG?"); /* Attach to GPRS Service */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+CGATT?\\r\\n");
  SIM900A.println("AT+CGATT?"); /* Network registration status */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+CIPSTATUS\\r\\n");
  SIM900A.println("AT+CIPSTATUS");  /* Attached to or detached from GPRS service */ 
  delay(2000); 
  ShowSerialData();
  delay(2000);
  Serial.print("AT+CIPMUX=0\\r\\n");
  SIM900A.println("AT+CIPMUX=0"); /* Start task and set APN */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+CSTT=\"airtelgprs.com\",\"\",\"\"\\r\\n");
  SIM900A.println("AT+CSTT=\"airtelgprs.com\",\"\",\"\""); /* Bring up wireless connection with GPRS */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+CIICR\\r\\n");
  SIM900A.println("AT+CIICR"); /* Get local IP address */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+CIFSR\\r\\n");
  SIM900A.println("AT+CIFSR");  /* Start up TCP connection */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+SAPBR=1,1\\r\\n");
  SIM900A.println("AT+SAPBR=1,1"); /* Send data through TCP connection */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+SAPBR=2,1\\r\\n");
  SIM900A.println("AT+SAPBR=2,1"); /* Non-Transparent (normal) mode for TCP/IP application */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+HTTPINIT\\r\\n");
  SIM900A.println("AT+HTTPINIT"); /* Non-Transparent (normal) mode for TCP/IP application */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+HTTPPARA=\"CID\",1\\r\\n");
  SIM900A.println("AT+HTTPPARA=\"CID\",1"); /* Non-Transparent (normal) mode for TCP/IP application */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+HTTPPARA=\"URL\",\"http://35.199.49.62/\"\\r\\n");
  SIM900A.println("AT+HTTPPARA=\"URL\",\"http://35.199.49.62/\""); /* Non-Transparent (normal) mode for TCP/IP application */
  delay(2000);
  ShowSerialData();
  delay(2000);
  Serial.print("AT+HTTPACTION=0\\r\\n");
  SIM900A.println("AT+HTTPACTION=0"); /* Non-Transparent (normal) mode for TCP/IP application */
  delay(2000);
  ShowSerialData();
//  delay(2000);
//  Serial.print("GET /update?api_key=C7JFHZY54GLCJY38&field1=1\\r\\n");
//  SIM900A.print("GET /update?api_key=C7JFHZY54GLCJY38&field1=1\r\n\x1A");  /* URL for data to be sent to */
//  delay(10000);
//  ShowSerialData();
//  delay(2000);
//  Serial.print("AT+CIPSHUT\\r\\n");
//  SIM900A.println("AT+CIPSHUT"); /* Deactivate GPRS PDP content */
//  delay(2000);
//  ShowSerialData();
//  delay(2000);
}

void ShowSerialData()
{
  while(SIM900A.available()!=0)  /* If data is available on serial port */
  Serial.write(char (SIM900A.read())); /* Print character received on to the serial monitor */
}








//AT
//
//OK
//AT+CPIN?
//
//+CPIN: READY
//
//OK
//AT+COPS?
//
//+COPS: 0,0,"AirTel"
//
//OK
//AT+CREG?
//
//+CREG: 0,1
//
//OK
//AT+CGATT?
//
//+CGATT: 1
//
//OK
//AT+CIPSTATUS
//
//OK
//
//STATE: IP INITIAL
//AT+CIPMUX=0
//
//OK
//AT+CSTT="airtelgprs.com","",""
//
//OK
//AT+CIICR
//
//OK
//AT+CIFSR
//
//100.90.43.59
//AT+SAPBR=1,1
//
//OK
//AT+SAPBR=2,1
//
//+SAPBR: 1,1,"100.77.138.232"
//
//OK
//AT+HTTPINIT
//
//OK
//AT+HTTPPARA="CID",1
//
//OK
//AT+HTTPPARA="URL","http://35.199.49.62/"
//
//OK
//AT+HTTPACTION=0
//
//OK
//
//+HTTPACTION: 0,200,438
//AT+HTTPACTION=0  
//
//OK
//
//+HTTPACTION: 0,200,438
//AT+HTTPREAD
//
//+HTTPREAD: 438
//<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><html>
//<title>Directory listing for /</title>
//<body>
//<h2>Directory listing for /</h2>
//<hr>
//<ul>
//<li><a href=".bash_history">.bash_history</a>
//<li><a href=".bash_logout">.bash_logout</a>
//<li><a href=".bashrc">.bashrc</a>
//<li><a href=".cache/">.cache/</a>
//<li><a href=".config/">.config/</a>
//<li><a href=".profile">.profile</a>
//<li><a href=".ssh/">.ssh/</a>
//</ul>
//<hr>
//</body>
//</html>
//
//OK

