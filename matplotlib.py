import matplotlib.pyplot as plt
import pandas as pd

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
    plotdata()