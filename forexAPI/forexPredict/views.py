import matplotlib as pl
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from .algorithms import utils, forexLSTM, forexTALib

from django.views.generic import TemplateView
import matplotlib.pyplot as plt

pl.use('Agg')


# Create your views here.


predictions = forexLSTM.lstm_forecast()


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class Stocks(TemplateView):

    def getStockData(request):
        todayDate = utils.get_today_date()
        previousDate = utils.get_previous_date(13)
        stockID = 'EUR/USD'

        return HttpResponse('{ "todayDate":"' + todayDate +
                            '", "previousDate":"' + previousDate +
                            '", "stockID":"' + stockID + '" }')

    def getLSTMdata(request):
        pred_list = list(predictions)
        send_list = []
        for ele in pred_list:
            single_price = ele.item()
            single_price = "{:.4f}".format(single_price)
            send_list.append(str(single_price))

        return HttpResponse('{ "day_1":"' + send_list[0] +
                            '", "day_2":"' + send_list[1] +
                            '", "day_3":"' + send_list[2] +
                            '", "day_4":"' + send_list[3] +
                            '", "day_5":"' + send_list[4] + '" }')

    def getPatterns(request):
        candle_name, trend_val, spot_date, trend = forexTALib.find_patterns()

        trend_val = str(trend_val)
        return HttpResponse('{ "candle_name":"' + candle_name +
                            '", "trend_val":"' + trend_val +
                            '", "spot_date":"' + spot_date +
                            '", "trend":"' + trend + '" }')


    def getLSTMPlot(request):

        chart = forexLSTM.get_LSTM_plot(predictions)

        response = HttpResponse(content_type="image/jpeg")
        chart.savefig(response, format="png")
        return response

    def getStockPlot(request):
        todayDate = utils.get_today_date()
        previousDate = utils.get_previous_date(13)
        chart = utils.get_stock_plot(previousDate, todayDate)

        response = HttpResponse(content_type="image/jpeg")
        chart.savefig(response, format="png")
        return response
