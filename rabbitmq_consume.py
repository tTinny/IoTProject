import json
import pika
from datetime import datetime

def fetch_data():

    rabbitmq_ip = "localhost"
    rabbitmq_port = 5672
    # Queue name
    rabbitmq_queque = "CSC8112"
    Timestamp = []
    Value = []
    dictionary = {}

    def callback(ch, method, properties, body):
        msg = json.loads(body)
        timestamp = msg[10:20]
        if timestamp != 'None':
            date = datetime.fromtimestamp(timestamp)
            value = f"{msg[:10]}{date}{msg[23:]}"
            print(f"Got message from producer msg: {value}")
            Timestamp.append(date)
            Value.append({msg[28:]})


    # Connect to RabbitMQ service with timeout 1min
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_ip, port=rabbitmq_port, socket_timeout=60))
    channel = connection.channel()
    # Declare a queue
    channel.queue_declare(queue=rabbitmq_queque)

    channel.basic_consume(queue=rabbitmq_queque,
                          auto_ack=True,
                          on_message_callback=callback)

    channel.start_consuming()
    dictionary['timestamp'] = timestamp
    dictionary['value'] = value

    print(dictionary)

if __name__ == '__main__':
    fetch_data()


    