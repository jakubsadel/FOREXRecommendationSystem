import talib
import pandas as pd
import yfinance as yf
from forexPredict.algorithms import utils
import matplotlib.pyplot as plt


def find_patterns():
    end_date = utils.get_today_date()
    start_date = utils.get_previous_date(13)

    print(start_date)
    print(end_date)

    single = pd.DataFrame

    df = yf.download(tickers='EURUSD=X', start=start_date, end=end_date, interval='1h')
    df = df.reset_index()

    print(df.shape)

    def hammer_pattern():
        hammer = talib.CDL2CROWS(df['Open'], df['High'], df['Low'], df['Close'])
        df['Hammer'] = hammer
        hammer_days = df[df['Hammer'] != 0]
        print('hammer works')
        return hammer_days

    def inverted_hammer_pattern():
        inverted_hammer = talib.CDLINVERTEDHAMMER(df['Open'], df['High'], df['Low'], df['Close'])
        df['Inverted Hammer'] = inverted_hammer
        inverted_hammer_days = df[df['Inverted Hammer'] != 0]
        print('inverted_hammer works')
        return inverted_hammer_days

    def morning_star_pattern():
        morning_star = talib.CDLMORNINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
        df['Morning Star'] = morning_star
        morning_star_days = df[df['Morning Star'] != 0]
        print('Morning Star works')
        return morning_star_days

    def three_white_soldiers_pattern():
        three_white_soldiers = talib.CDL3WHITESOLDIERS(df['Open'], df['High'], df['Low'], df['Close'])
        df['Three White Soldiers'] = three_white_soldiers
        three_white_soldiers_days = df[df['Three White Soldiers'] != 0]
        print('Three White Soldiers works')
        return three_white_soldiers_days

    def three_line_strike_pattern():
        three_line_strike = talib.CDL3LINESTRIKE(df['Open'], df['High'], df['Low'], df['Close'])
        df['Three Line Strike'] = three_line_strike
        three_line_strike_days = df[df['Three Line Strike'] != 0]
        print('Three Line Strike works')
        return three_line_strike_days

    def abandoned_baby_pattern():
        abandoned_baby = talib.CDLABANDONEDBABY(df['Open'], df['High'], df['Low'], df['Close'])
        df['Abandoned Baby'] = abandoned_baby
        abandoned_baby_days = df[df['Abandoned Baby'] != 0]
        print('Abandoned Baby works')
        return abandoned_baby_days

    def hanging_man_pattern():
        hanging_man = talib.CDLHANGINGMAN(df['Open'], df['High'], df['Low'], df['Close'])
        df['Hanging Man'] = hanging_man
        hanging_man_days = df[df['Hanging Man'] != 0]
        print('Hanging Man works')
        return hanging_man_days

    def shooting_star_pattern():
        shooting_star = talib.CDLSHOOTINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
        df['Shooting Star'] = shooting_star
        shooting_star_days = df[df['Shooting Star'] != 0]
        print('Shooting Star works')
        return shooting_star_days

    def evening_star_pattern():
        evening_star = talib.CDLEVENINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
        df['Evening Star'] = evening_star
        evening_star_days = df[df['Evening Star'] != 0]
        print('Evening Star works')
        return evening_star_days

    def three_black_crows_pattern():
        three_black_crows = talib.CDL3BLACKCROWS(df['Open'], df['High'], df['Low'], df['Close'])
        df['Three Black Crows'] = three_black_crows
        three_black_crows_days = df[df['Three Black Crows'] != 0]
        print('Three Black Crows works')
        return three_black_crows_days

    def dark_cloud_cover_pattern():
        dark_cloud_cover = talib.CDLDARKCLOUDCOVER(df['Open'], df['High'], df['Low'], df['Close'])
        df['Dark Cloud Cover'] = dark_cloud_cover
        dark_cloud_cover_days = df[df['Dark Cloud Cover'] != 0]
        print('Dark Cloud Cover works')
        return dark_cloud_cover_days

    # def doji_pattern():
    #     doji = talib.CDLDOJI(df['Open'], df['High'], df['Low'], df['Close'])
    #     df['Doji'] = doji
    #     doji_days = df[df['Doji'] != 0]
    #     print('Doji works')
    #     return doji_days

    # def spinning_top_pattern():
    #     spinning_top = talib.CDLSPINNINGTOP(df['Open'], df['High'], df['Low'], df['Close'])
    #     df['Spinning Top'] = spinning_top
    #     spinning_top_days = df[df['Spinning Top'] != 0]
    #     print('Spinning Top works')
    #     return spinning_top_days

    print(hammer_pattern())
    print(inverted_hammer_pattern())
    print(morning_star_pattern())
    print(three_white_soldiers_pattern())
    print(three_line_strike_pattern())
    print(abandoned_baby_pattern())
    print(hanging_man_pattern())
    print(shooting_star_pattern())
    print(evening_star_pattern())
    print(three_black_crows_pattern())
    print(dark_cloud_cover_pattern())
    # print(doji_pattern())
    # print(spinning_top_pattern())

    plt.figure(figsize=(16, 8))
    plt.title('Euro Close Price History')
    plt.plot(df['Close'])

    print(df)
    print(df.shape)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Close Price USD ($)', fontsize=10)
    plt.show()

    return plt


