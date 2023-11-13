# python code for data injection

import requests
import paho.mqtt.client as mqtt
import json
import random

starttime = "20230701"
endtime = "20230802"
values = []
dictionary = {}

broker = 'emqx@172.17.0.2'
port = 1883
topic = 'python/mqtt'
client_id = f'python-mqtt-123'
username = 'admin'
password = 'admin1234'



url = f"https://newcastle.urbanobservatory.ac.uk/api/v1.1/sensors/PER_AIRMON_MONITOR1135100/data/json/?starttime={starttime}&endtime={endtime}"

data = requests.get(url)

data = data.json()

data_input = data.get('sensors')[0]['data'].get('PM2.5')

for i in range(0,len(data_input)):
	dictionary['Timestamp'] = data_input[i].get('Timestamp')
	dictionary['Value'] = data_input[i].get('Value')
	values.append(dictionary)


client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(broker, port)
publish(client)
print(client)

print('client connected')
