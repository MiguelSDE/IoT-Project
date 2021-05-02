# IoT-Project
An expandable security system implemented with CoAP or MQTT

#
## MQTT Setup
Install Mosquitto Broker on Raspberry Pi  
`$ sudo apt-get update`  
`$ sudo apt-get upgrade`  
`$ sudo apt-get install mosquitto`  
`$ sudo apt-get install mosquitto-clients -y`

Open mosquitto.conf   
`$ sudo nano /etc/mosquitto/mosquitto.conf`  
Add the following after the last line   
allow_anonymous = false   
password_file /etc/mosquitto/pwfile   
listener 1883

Create username and password   
`$ sudo mosquitto_passwd -c /etc/mosquitto/pwfile Username`   
Make sure is "active (running)   
`$ sudo systemctl status mosquitto`

Install Python's Paho-MQTT   
`$ sudo pip install paho-mqtt`

Upload the MQTT code to the ESP8266 NodeMCU along with the required libraries, which I also included., make sure it's running   
<img src="https://i.imgur.com/n68zRlU.png" width="800"/>



Run the Python code I have included on the Raspberry Pi   
`$ sudo nano get_MQTT_data.py`   
You are now subscribed and can start to receive the sensors' data.   
<img src="https://i.imgur.com/C2Avrpp.png" width="800"/>

#
## CoAP Setup
Upload the CoAP code to the ESP8266 NodeMCU along with the required libraries, which I also included.   
<img src="https://i.imgur.com/6wSuPXU.png"/>

To view the server on a website, simply paste the ip address shown in the serial monitor on any web browser   
<img src="https://i.imgur.com/dalotz7.png" width="800"/>

#
## Access your server from anywhere in the world
Use https://setuprouter.com/ if you do not know how to deal with your router


* On LAN TCP/IP Setup
    * Find your Raspberry Pi's and ESP8266 NodeMCU's IP addresses
    * Reserve them, meaning they are now static and will not be changing, allowing your code to always work
* On Port Forwarding/Port Triggering
    * Find your Raspberry Pi's and ESP8266 NodeMCU's IP addresses
    * Forward Raspberry Pi's IP address to port 1883 (for MQTT)
    * Forward ESP8266 NodeMCU's IP address to port 80 (for CoAP)

With this, now you have both protocols working, and with your public IP address, you can access your broker using either protocol from anywhere in the world.