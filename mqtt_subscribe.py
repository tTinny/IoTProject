import json
from paho.mqtt import client as mqtt_client
import pika

if __name__ == '__main__':
    clientID = 'test'
    mqtt_ip = "l192.168.0.102"
    mqtt_port = 1883
    topic = "python/mqtt"
    values  = []

    rabbitmq_ip = "192.168.0.100"
    rabbitmq_port = 5672
    # Queue name
    rabbitmq_queque = "CSC8112"

    # Connect to RabbitMQ service
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_ip, port=rabbitmq_port))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue=rabbitmq_queque)

    client = mqtt_client.Client()

    # Callback function for MQTT connection
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT OK!", flush=True)
        else:
            print("Failed to connect, return code %d\n", rc)

    # Connect to MQTT service
    client.on_connect = on_connect
    client.connect(mqtt_ip, mqtt_port)

    # Callback function will be triggered
    def on_message(client, userdata, msg):
        # print(f"Get message from publisher {json.loads(msg.payload)}")
        values = json.loads(msg.payload)
        print(values,flush=True)
        channel.basic_publish(exchange='',
                          routing_key=rabbitmq_queque,
                          body=json.dumps(values))


    # Subscribe MQTT topic
    client.subscribe(topic)
    client.on_message = on_message

    # Start a thread to monitor message from publisher
    client.loop_forever()