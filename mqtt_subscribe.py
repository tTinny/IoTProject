import json
from paho.mqtt import client as mqtt_client

if __name__ == '__main__':
    clientID = 'test'
    mqtt_ip = "localhost"
    mqtt_port = 1883
    topic = "python/mqtt"
    values  = []

    client = mqtt_client.Client()

    # Callback function for MQTT connection
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT OK!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Connect to MQTT service
    client.on_connect = on_connect
    client.connect(mqtt_ip, mqtt_port)

    # Callback function will be triggered
    def on_message(client, userdata, msg):
        print(f"Get message from publisher {json.loads(msg.payload)}")
        values.append(json.loads(msg.payload))


    print(len(values))
    # Subscribe MQTT topic
    client.subscribe(topic)
    client.on_message = on_message

    # Start a thread to monitor message from publisher
    client.loop_forever()