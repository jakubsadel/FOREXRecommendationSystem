import talib
import pandas as pd
import numpy as np
import yfinance as yf
from forexPredict.algorithms import utils



def find_patterns():
    end_date = utils.get_today_date()
    start_date = utils.get_previous_date(13)

    print(start_date)
    print(end_date)

    single = pd.DataFrame

    df = yf.download(tickers='EURUSD=X', start=start_date, end=end_date, interval='1h')
    # df = df.reset_index()
    print(df.shape)

    list = []

    def hammer_pattern():
        hammer = talib.CDL2CROWS(df['Open'], df['High'], df['Low'], df['Close'])
        df['Hammer'] = hammer
        hammer_days = df[df['Hammer'] != 0]
        isempty = hammer_days.empty
        if isempty:
            print('hammer empty')
            hammer_days = 0
        else:
            hammer_days = hammer_days['Hammer'].iloc[[-1]]
            list.append(hammer_days)
            print('hammer added')
        return hammer_days

    def inverted_hammer_pattern():
        inverted_hammer = talib.CDLINVERTEDHAMMER(df['Open'], df['High'], df['Low'], df['Close'])
        df['Inverted Hammer'] = inverted_hammer
        inverted_hammer_days = df[df['Inverted Hammer'] != 0]
        isempty = inverted_hammer_days.empty
        if isempty:
            inverted_hammer_days = 0
            print('inverted_hammer empty')
        else:
            inverted_hammer_days = inverted_hammer_days['Inverted Hammer'].iloc[[-1]]
            list.append(inverted_hammer_days)
            print('inverted_hammer added')
        return inverted_hammer_days

    def morning_star_pattern():
        morning_star = talib.CDLMORNINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
        df['Morning Star'] = morning_star
        morning_star_days = df[df['Morning Star'] != 0]
        isempty = morning_star_days.empty
        if isempty:
            print('morning star empty')
            morning_star_days = 0
        else:
            morning_star_days = morning_star_days['Morning Star'].iloc[[-1]]
            list.append(morning_star_days)
            print('morning star added')
        return morning_star_days

    def three_white_soldiers_pattern():
        three_white_soldiers = talib.CDL3WHITESOLDIERS(df['Open'], df['High'], df['Low'], df['Close'])
        df['Three White Soldiers'] = three_white_soldiers
        three_white_soldiers_days = df[df['Three White Soldiers'] != 0]
        isempty = three_white_soldiers_days.empty
        if isempty:
            three_white_soldiers_days = 0
            print('three white soldiers empty')
        else:
            three_white_soldiers_days = three_white_soldiers_days['Three White Soldiers'].iloc[[-1]]
            list.append(three_white_soldiers_days)
            print('three white soldiers added')
        return three_white_soldiers_days

    def three_line_strike_pattern():
        three_line_strike = talib.CDL3LINESTRIKE(df['Open'], df['High'], df['Low'], df['Close'])
        df['Three Line Strike'] = three_line_strike
        three_line_strike_days = df[df['Three Line Strike'] != 0]
        isempty = three_line_strike_days.empty
        if isempty:
            three_line_strike_days = 0
            print('three line strike empty')
        else:
            three_line_strike_days = three_line_strike_days['Three Line Strike'].iloc[[-1]]
            list.append(three_line_strike_days)
            print('three line strike added')
        return three_line_strike_days

    def abandoned_baby_pattern():
        abandoned_baby = talib.CDLABANDONEDBABY(df['Open'], df['High'], df['Low'], df['Close'])
        df['Abandoned Baby'] = abandoned_baby
        abandoned_baby_days = df[df['Abandoned Baby'] != 0]
        isempty = abandoned_baby_days['Abandoned Baby'].empty
        if isempty:
            abandoned_baby_days = 0
            print('abandoned baby empty')
        else:
            abandoned_baby_days = abandoned_baby_days['Abandoned Baby'].iloc[[-1]]
            list.append(abandoned_baby_days)
            print('abandoned baby added')
        return abandoned_baby_days

    def hanging_man_pattern():
        hanging_man = talib.CDLHANGINGMAN(df['Open'], df['High'], df['Low'], df['Close'])
        df['Hanging Man'] = hanging_man
        hanging_man_days = df[df['Hanging Man'] != 0]
        isempty = hanging_man_days.empty
        if isempty:
            hanging_man_days = 0
            print('hanging man empty')
        else:
            hanging_man_days = hanging_man_days['Hanging Man'].iloc[[-1]]
            list.append(hanging_man_days)
            print('hanging man added')
        return hanging_man_days

    def shooting_star_pattern():
        shooting_star = talib.CDLSHOOTINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
        df['Shooting Star'] = shooting_star
        shooting_star_days = df[df['Shooting Star'] != 0]
        isempty = shooting_star_days.empty
        if isempty:
            shooting_star_days = 0
            print('shooting star empty')
        else:
            shooting_star_days = shooting_star_days['Shooting Star'].iloc[[-1]]
            list.append(shooting_star_days)
            print('shooting star added')
        return shooting_star_days

    def evening_star_pattern():
        evening_star = talib.CDLEVENINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
        df['Evening Star'] = evening_star
        evening_star_days = df[df['Evening Star'] != 0]
        isempty = evening_star_days.empty
        if isempty:
            evening_star_days = 0
            print('evening star empty')
        else:
            evening_star_days = evening_star_days['Evening Star'].iloc[[-1]]
            list.append(evening_star_days)
            print('evening star added')
        return evening_star_days

    def three_black_crows_pattern():
        three_black_crows = talib.CDL3BLACKCROWS(df['Open'], df['High'], df['Low'], df['Close'])
        df['Three Black Crows'] = three_black_crows
        three_black_crows_days = df[df['Three Black Crows'] != 0]
        isempty = three_black_crows_days.empty
        if isempty:
            three_black_crows_days = 0
            print('three black crows empty')
        else:
            three_black_crows_days = three_black_crows_days['Three Black Crows'].iloc[[-1]]
            list.append(three_black_crows_days)
            print('three black crows added')
        return three_black_crows_days

    def dark_cloud_cover_pattern():
        dark_cloud_cover = talib.CDLDARKCLOUDCOVER(df['Open'], df['High'], df['Low'], df['Close'])
        df['Dark Cloud Cover'] = dark_cloud_cover
        dark_cloud_cover_days = df[df['Dark Cloud Cover'] != 0]
        isempty = dark_cloud_cover_days.empty
        if isempty:
            dark_cloud_cover_days = 0
            print('dark cloud cover empty')
        else:
            dark_cloud_cover_days = dark_cloud_cover_days['Dark Cloud Cover'].iloc[[-1]]
            list.append(dark_cloud_cover_days)
            print('dark cloud cover added')
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

    hammer_pattern()
    inverted_hammer_pattern()
    morning_star_pattern()
    three_white_soldiers_pattern()
    three_line_strike_pattern()
    abandoned_baby_pattern()
    hanging_man_pattern()
    shooting_star_pattern()
    evening_star_pattern()
    three_black_crows_pattern()
    dark_cloud_cover_pattern()

    max_index = list[0].index
    max = 0

    for ele in list:
        if ele.index >= max_index:
            max_index = ele.index
            max = ele

    candle_name = max.name

    val = max.values
    val = np.int32(val)
    trend_val = val.item()

    npdate = max.index.values[0]

    ts = pd.to_datetime(str(npdate))
    spot_date = ts.strftime('%Y.%m.%d')

    print(spot_date)
    print(trend_val)
    print(candle_name)

    if trend_val>0:
        trend = "Wzrost"
    else:
        trend = "Spadek"

    return candle_name, trend_val, spot_date, trend

