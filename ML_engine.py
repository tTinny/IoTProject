from ml_engine import MLPredictor

if __name__ == '__main__':
    # Prepare data
    data = {
        'Timestamp': ['2023-11-01', '2023-11-02', '2023-11-03','2023-11-04', '2023-11-05','2023-11-06', '2023-11-07', '2023-11-08','2023-11-09', '2023-11-10',
                        '2023-11-11', '2023-11-12', '2023-11-13','2023-11-14', '2023-11-15','2023-11-16', '2023-11-17'],
        'Value': [2.122,5.226,0.65,2.498,5.297,8.882,2.886,3.209,5.453,8.537,3.796,12.58,13.52,1.142,8.551,11.92]
    }
    data_df = pd.DataFrame(data)

    # Create ML engine predictor object
    predictor = MLPredictor(data_df)
    # Train ML model
    predictor.train()
    # Do prediction
    forecast = predictor.predict()

        # Get canvas
    fig = predictor.plot_result(forecast)
    fig.savefig("prediction.png")
    fig.show()