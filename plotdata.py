import matplotlib.pyplot as plt
import pandas as pd
from rabbitmq_consume import fetch_data


def plotdata():
    # Prepare data
    timestamp = []
    value = []
    data = {
        'Timestamp': ['2023-11-01', '2023-11-02', '2023-11-03','2023-11-04', '2023-11-05','2023-11-06', '2023-11-07', '2023-11-08','2023-11-09', '2023-11-10',
                        '2023-11-11', '2023-11-12', '2023-11-13','2023-11-14', '2023-11-15','2023-11-16'],
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
    plotdata()