import numpy as np
import yfinance as yf
import math
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dropout, Dense
from keras.models import Sequential, load_model

from forexPredict.algorithms import utils


def lstm_forecast():
    df = yf.download(tickers='EURUSD=X', start='2005-01-01', end='2019-12-31', interval='1d')
    data_close = df.filter(['Close'])
    dataset = data_close.values
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

    # forexPredictor = Sequential()
    # forexPredictor.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    # forexPredictor.add(LSTM(50, return_sequences=False))
    # forexPredictor.add(Dropout(0.2))
    # forexPredictor.add(Dense(50))
    # forexPredictor.add(Dense(1))
    # forexPredictor.compile(optimizer='adam', loss='mean_squared_error')
    # forexPredictor.save('my_model')
    #
    # forexPredictor.fit(x_train, y_train, epochs=100, batch_size=128)

    model = load_model('my_model')

    end_date = utils.get_today_date()
    start_date = utils.get_previous_date(84)

    new = yf.download(tickers='EURUSD=X', start=start_date, end=end_date, interval='1d')

    new = new.filter(['Close'])
    new_dataset = new.values
    new_data = scaler.transform(new_dataset)

    new_test = []
    for i in range(60, len(new_data)):
        new_test.append(new_data[i - 60:i, 0])

    temp_input = list(new_test)
    temp_input = temp_input[0].tolist()

    new_test = np.array(new_test)
    print(new_test.shape)
    new_test = np.reshape(new_test, (new_test.shape[0], new_test.shape[1], 1))
    print(new_test.shape)

    lst_output = []
    n_steps = 60
    i = 0
    predictions = list()

    while (i < 10):

        if (len(temp_input) > n_steps):
            new_test = np.array(temp_input[1:])
            new_test = new_test.reshape(1, -1)
            new_test = new_test.reshape((1, n_steps, 1))
            yhat = model.predict(new_test)
            yhat = scaler.inverse_transform(yhat)
            predictions.append(yhat[0][0])
            temp_input.extend(yhat[0].tolist())
            temp_input = temp_input[1:]
            i = i + 1
        else:
            new_test = new_test.reshape((1, n_steps, 1))
            yhat = model.predict(new_test)
            yhat = scaler.inverse_transform(yhat)
            temp_input.extend(yhat[0].tolist())
            lst_output.extend(yhat.tolist())
            i = i + 1

    print(predictions)
    return predictions
