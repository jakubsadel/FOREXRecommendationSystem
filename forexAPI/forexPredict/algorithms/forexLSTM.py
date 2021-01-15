import numpy as np
import yfinance as yf
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dropout, Dense
from keras.models import Sequential, load_model


from forexPredict.algorithms import utils


def lstm_forecast():
    df = yf.download(tickers='EURUSD=X', start='2010-01-01', end='2019-12-31', interval='1d')
    df_close = df.filter(['Close'])
    dataset = df_close.values
    train_len = math.ceil(len(dataset) * .8)
    scaler = MinMaxScaler(feature_range=(0, 1))
    training_data = scaler.fit_transform(dataset[:train_len, :])
    x_train = []
    y_train = []

    for i in range(60, len(training_data)):
        x_train.append(training_data[i - 60:i, 0])
        y_train.append(training_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    test_data = scaler.transform(dataset[train_len - 60:, :])
    x_test = []
    y_test = dataset[train_len:, :]

    for i in range(60, len(test_data)):
        x_test.append(test_data[i - 60:i, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    forexPredictor = Sequential()
    forexPredictor.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    forexPredictor.add(Dropout(0.2))
    forexPredictor.add(LSTM(50, return_sequences=False))
    forexPredictor.add(Dropout(0.2))
    forexPredictor.add(Dense(50))
    forexPredictor.add(Dense(1))
    forexPredictor.compile(optimizer='adam', loss='mean_squared_error')
    forexPredictor.fit(x_train, y_train,  epochs=5, batch_size=32)
    forexPredictor.save("forex_model")

    forexPredictor = load_model("forex_model")
    test_predictions = forexPredictor.predict(x_test)
    test_predictions = scaler.inverse_transform(test_predictions)


    rmse = np.sqrt(np.mean(((test_predictions - y_test) ** 2)))
    print(rmse)
    


    end_date = utils.get_previous_date(0)
    start_date = utils.get_previous_date(84)
    print(start_date)
    print(end_date)
    user_df = yf.download(tickers='EURUSD=X', start=start_date, end=end_date, interval='1d')
    user_df = user_df.filter(['Close'])
    user_data_value = user_df.values
    user_data = scaler.transform(user_data_value)
    forex_input = []
    for i in range(60, len(user_data)):
        forex_input.append(user_data[i - 60:i, 0])

    temp_input = list(forex_input)
    temp_input = temp_input[0].tolist()
    forex_input = np.array(forex_input)
    forex_input = np.reshape(forex_input, (forex_input.shape[0], forex_input.shape[1], 1))

    forex_output = []
    n_steps = 60
    i = 0

    while i < 5:

        if (len(temp_input) > n_steps):
            forex_input = np.array(temp_input[1:])
            forex_input = forex_input.reshape(1, -1)
            forex_input = forex_input.reshape((1, n_steps, 1))
            pred_value = forexPredictor.predict(forex_input)
            temp_input.extend(pred_value[0].tolist())
            temp_input = temp_input[1:]
            forex_output.extend(pred_value.tolist())
            i = i + 1
        else:
            forex_input = forex_input.reshape((1, n_steps, 1))
            pred_value = forexPredictor.predict(forex_input)
            temp_input.extend(pred_value[0].tolist())
            forex_output.extend(pred_value.tolist())
            i = i + 1

    predictions = scaler.inverse_transform(forex_output)

    print(predictions)
    rmse = "{:.6f}".format(rmse)
    return predictions, rmse


def get_LSTM_plot(predictions):
    days = np.arange(1, 6)

    plt.figure(figsize=(16, 8))
    plt.title('Euro Close Price Predictions')
    plt.plot(days, predictions)

    plt.xlabel('Day', fontsize=10)
    plt.ylabel('Close Price USD ($)', fontsize=10)

    return plt
