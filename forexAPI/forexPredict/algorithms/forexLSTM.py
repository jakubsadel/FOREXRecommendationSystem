import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from keras import models
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import math
import yfinance as yf


def use_model():
    new = web.DataReader('EURUSD=X', data_source='yahoo', start='2020-01-01', end='2020-05-05')
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    new = new.filter(['Close'])
    new_dataset = new.values
    model = models.load_model('lstm_model.h5')
    test = []
    for i in range(60, len(new_dataset)):
        test.append(new_dataset[i - 60:i, 0])

    test = np.array(test)
    test = np.reshape(test, (test.shape[0], test.shape[1], 1))
    new_predictions = model.predict(test)
    print(new_predictions)
    print(new_predictions.shape)

def train_model():
    data = web.DataReader('EURUSD=X', data_source='yahoo', start='2011-12-31', end='2019-12-31')
    data_close = data.filter(['Close'])
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

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.save('lstm_model.h5')

    model.fit(x_train, y_train, epochs=100, batch_size=32)

    # remaining 20%
    test_data = scaler.transform(dataset[train_len - 60:, :])
    x_test = []
    for i in range(60, len(test_data)):
        x_test.append(test_data[i - 60:i, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    x_test.shape

    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)  # importance of transforme only
    predictions.shape

    model.save('lstm_model.h5')


use_model()