import matplotlib as pl
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

pl.use('Agg')
import pandas as pd

import numpy as np
# Create your views here.
from rest_framework import serializers
from rest_framework import viewsets

from forexPredict.models import Stock
from .algorithms import utils, forexLSTM


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
        predictions = forexLSTM.lstm_forecast()
        str1 = ""

        # traverse in the string
        for ele in predictions:
            due = str(ele.item())
            str1 += due

        return HttpResponse('{ "todayDate":"' + str1 + '" }')

    def getNums(request):
        n = np.array([2, 3, 4])
        name1 = "name-" + str(n[1])
        return HttpResponse('{ "name":"' + name1 + '", "age":31, "city":"New York" }')

    def getImage(request):
        todayDate = utils.get_today_date()
        previousDate = utils.get_previous_date(13)
        plt = utils.get_stock_plot(previousDate, todayDate)

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def getData(request):
        samp = np.random.randint(100, 600, size=(4, 5))
        df = pd.DataFrame(samp, index=['avi', 'dani', 'rina', 'dina'],
                          columns=['Jan', 'Feb', 'Mar', 'Apr', 'May'])
        return HttpResponse(df.to_html(classes='table table-bordered'))


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('today_date', 'previous_date')


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
