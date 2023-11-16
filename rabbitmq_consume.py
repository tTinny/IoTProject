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
        if timestamp != 'None':
            date = datetime.fromtimestamp(timestamp)
            value = f"{msg[:10]}{date}{msg[23:]}"
            print(f"Got message from producer msg: {value}")


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

def plotdata():
    # Prepare data
    timestamp = []
    value = []
    data = {
        'Timestamp': ['01/11','02/11','03/11','04/11','05/11','06/11','07/11','08/11','09/11','10/11','11/11','12/11','13/11','14/11','15/11','16/11','17/11'],
        'Value': [2.122,5.226,0.65,2.498,5.297,8.882,2.886,3.209,5.453,8.537,3.796,12.58,13.52,1.142,8.551,11.92]
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

if __name__ == '__main__':
    fetch_data()
    plotdata()


    