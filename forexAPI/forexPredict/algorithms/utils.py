from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas_datareader as web
import plotly.graph_objects as go

def get_today_date():
    tup = datetime.today().strftime('%Y-%m-%d')
    date_today =''.join(tup)
    return date_today


def get_2weeks_date():
    tup = (datetime.today() - timedelta(days=14)).strftime('%Y-%m-%d')
    date_2weeks_ago = ''.join(tup)
    return date_2weeks_ago


def get_stock_plot(start_data, end_data):

    df = web.DataReader('EURUSD=X', data_source='yahoo', start=start_data, end= end_data)
    plt.figure(figsize=(16, 8))
    plt.title('Euro Close Price History')
    plt.plot(df['Close'])

    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Close Price USD ($)', fontsize=10)
    plt.show()
    return plt
