from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas_datareader as web


def get_today_date():
    tup = datetime.today().strftime('%Y-%m-%d')
    date_today = ''.join(tup)
    return date_today


def get_previous_date():
    tup = (datetime.today() - timedelta(days=6)).strftime('%Y-%m-%d')
    date_previous = ''.join(tup)
    return date_previous


def get_stock_plot(start_data, end_data):
    df = web.DataReader('EURUSD=X', data_source='yahoo', start=start_data, end=end_data)
    plt.figure(figsize=(16, 8))
    plt.title('Euro Close Price History')
    plt.plot(df['Close'])

    print(df)
    print(df.shape)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Close Price USD ($)', fontsize=10)
    plt.show()
    return plt
