import json
import pika
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def fetch_data():

    rabbitmq_ip = "localhost"
    rabbitmq_port = 5672
    # Queue name
    rabbitmq_queque = "CSC8112"

    def callback(ch, method, properties, body):
        msg = json.loads(body)
        timestamp = msg[10:20]
        date = datetime.fromtimestamp(timestamp)
        value = f"{msg[:10]}{date}{msg[23:]}"
        print(f"Got message from producer msg: {value}")

    # Connect to RabbitMQ service with timeout 1min
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_ip, port=rabbitmq_port, socket_timeout=60))
    channel = connection.channel()
    # Declare a queue
    channel.queue_declare(queue=rabbitmq_queque)

    message = channel.basic_consume(queue=rabbitmq_queque,
                          auto_ack=True,
                          on_message_callback=callback)

    print(message)
    
    # Prepare data
    data = {
        'Timestamp': ['01/09','02/09','03/09','04/09','05/09'],
        'Value': [1,2,1,10,5]
    }

    data_df = pd.DataFrame(data)

    # Initialize a canvas
    plt.figure(figsize=(8, 4), dpi=200)
    # Plot data into canvas
    plt.plot(data_df["Timestamp"], data_df["Value"], color="#FF3B1D", marker='.', linestyle="-")
    plt.title("Example data for demonstration")
    plt.xlabel("DateTime")
    plt.ylabel("Value")

    # Save as file
    plt.savefig("figure1.png")
    # Directly display
    plt.show()

    channel.start_consuming()

if __name__ == '__main__':
    fetch_data()


    