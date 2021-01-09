import matplotlib as pl
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import matplotlib.pyplot as plt

pl.use('Agg')
import pandas as pd
import numpy as np
# Create your views here.

from .algorithms import utils, forexLSTM

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

    def getLSTM(request):
        print(predictions)
        pred_list = list(predictions)
        str_response = ""
        for ele in pred_list:
            single_price = ele.item()
            single_price = "{:.4f}".format(single_price)
            due = str(single_price)
            str_response = '{ "' + str_response + '", "day":"' + due + '" }'

        str_response[:-1]
        print(str_response)

        return HttpResponse('{ "' + str_response + '" }')


    def getImage(request):
        todayDate = utils.get_today_date()
        previousDate = utils.get_previous_date(13)
        plt = utils.get_stock_plot(previousDate, todayDate)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def getLSTMplot(request):
        print(predictions)
        days = np.arange(1, 6)

        plt.figure(figsize=(16, 8))
        plt.title('Euro Close Price History')
        plt.plot(days, predictions)

        plt.xlabel('Day', fontsize=10)
        plt.ylabel('Close Price USD ($)', fontsize=10)

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response


    def getImage(request):
        todayDate = utils.get_today_date()
        previousDate = utils.get_previous_date(13)
        plt = utils.get_stock_plot(previousDate, todayDate)

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response
