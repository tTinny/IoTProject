# python code for data injection

import requests
from paho.mqtt import client as mqtt_client
import json
import random

starttime = "20230701"
endtime = "20230802"
values = []
dictionary = {}

clientID = 'test'
mqtt_ip = "localhost"
mqtt_port = 1883
topic = "python/mqtt"
#msg = f'python-mqtt-123'


url = f"https://newcastle.urbanobservatory.ac.uk/api/v1.1/sensors/PER_AIRMON_MONITOR1135100/data/json/?starttime={starttime}&endtime={endtime}"

data = requests.get(url)

data = data.json()

data_input = data.get('sensors')[0]['data'].get('PM2.5')

for i in range(0,len(data_input)):
	dictionary['Timestamp'] = data_input[i].get('Timestamp')
	dictionary['Value'] = data_input[i].get('Value')
	values.append(dictionary)

#print(values)

client = mqtt_client.Client()
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT OK!")
	else:
		print("Failed to connect, return code %d\n", rc)
	
# Connect to MQTT service
client.on_connect = on_connect
client.connect(mqtt_ip, mqtt_port)

# Publish message to MQTT
# Note: MQTT payload must be a string, bytearray, int, float or None
#msg = json.dumps(msg)

for i in range(0,len(values)):
	msg = f"Timestamp:{values[i].get('Timestamp')}, Value:{values[i].get('Value')}"
	msg = json.dumps(msg)
	print(msg)
	client.publish(topic, msg)


print('client connected')
