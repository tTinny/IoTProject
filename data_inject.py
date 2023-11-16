# python code for data injection

import requests
from paho.mqtt import client as mqtt_client
import json
import random


def fetch_data():
	starttime = "20230701"
	endtime = "20230805"
	values = []
	dictionary = {}

	url = f"https://newcastle.urbanobservatory.ac.uk/api/v1.1/sensors/PER_AIRMON_MONITOR1135100/data/json/?starttime={starttime}&endtime={endtime}"

	data = requests.get(url)

	data = data.json()

	data_input = data.get('sensors')[0]['data'].get('PM2.5')

	for i in range(20):
		dictionary['Timestamp'] = data_input[i].get('Timestamp')
		dictionary['Value'] = data_input[i].get('Value')
		dictionary = {}
		values.append(dictionary)

	publish_msg(values)


def publish_msg(values):
	clientID = 'test'
	mqtt_ip = "192.168.0.102"
	mqtt_port = 1883
	topic = "python/mqtt"

	client = mqtt_client.Client()
	def on_connect(client, userdata, flags, rc):
		if rc == 0:
			print("Connected to MQTT OK!")
		else:
			print("Failed to connect, return code %d\n", rc)
		
	
	client.on_connect = on_connect
	client.connect(mqtt_ip, mqtt_port)


	for i in range(0,len(values)):
		msg = f"Timestamp:{values[i].get('Timestamp')}, Value:{values[i].get('Value')}"
		msg = json.dumps(msg)
		client.publish(topic, msg)


	print('client connected')

if __name__ == '__main__':
	fetch_data()
