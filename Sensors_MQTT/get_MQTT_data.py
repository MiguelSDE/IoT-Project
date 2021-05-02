import paho.mqtt.client as mqtt

MQTT_ADDRESS = '192.192.1.99' # IP address is Pi's one
MQTT_USER = 'Hello'
MQTT_PASSWORD = 'Hell0!'
MQTT_TOPIC = 'home/+/+'
i = 0
lines = 1

def on_connect(client, userdata, flags, rc):
   """ The callback for when the client receives a CONNACK response from the server. """
   print('Connected with result code ' + str(rc)) 
   client.subscribe(MQTT_TOPIC)
   
def on_message(client, userdata, msg):
   global i
   global lines
   """  The callback for when a PUBLISH  message is received from the server. """
   print(msg.topic + ' ' + str(msg.payload))
   with open('data/mqttData' + str(i) + ' .txt', 'a+') as f:
      f.write(str(msg.payload) + "\n")
   if (lines % 3 == 0):
      i += 1 
   f.close()
   lines += 1

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_ADDRESS, 1883)
mqtt_client.loop_forever()
