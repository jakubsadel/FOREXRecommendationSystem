from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import yfinance as yf

def get_today_date():
    tup = datetime.today().strftime('%Y-%m-%d')
    date_today = ''.join(tup)
    return date_today


def get_previous_date(days):
    tup = (datetime.today() - timedelta(days=days)).strftime('%Y-%m-%d')
    date_previous = ''.join(tup)
    return date_previous


def get_stock_plot(start_date, end_date):
    df = yf.download(tickers='EURUSD=X', start=start_date, end=end_date, interval='15m')

    plt.figure(figsize=(16, 8))
    plt.title('Euro Close Price History')
    plt.plot(df['Close'])

    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Close Price USD ($)', fontsize=10)
    plt.show()
    return plt

