import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt


def get_plot():
    df = web.DataReader('EURUSD=X', data_source='yahoo', start='2010-01-01', end='2020-11-22')
    plt.figure(figsize=(30, 15))
    plt.title('Euro Close Price History')
    plt.plot(df['Close'])
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.show()
    return plt
