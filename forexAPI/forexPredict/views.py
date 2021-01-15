import matplotlib as plt
from django.http import HttpResponse
from django.shortcuts import render
from .algorithms import utils, forexLSTM, forexTALib
from django.views.generic import TemplateView

plt.use('Agg')

# Create your views here.

predictions, rmse = forexLSTM.lstm_forecast()

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request,
                      'index.html',
                      context=None)


class Stocks(TemplateView):

    def get_stock_data(request):
        todayDate = utils.get_today_date()
        previousDate = utils.get_previous_date(13)
        stockID = 'EUR/USD'

        return HttpResponse('{ "todayDate":"' + todayDate +
                            '", "previousDate":"' + previousDate +
                            '", "stockID":"' + stockID + '" }')



    def get_patterns(request):
        candle_name, trend_val, spot_date, trend, ta_recommendation = forexTALib.find_patterns()

        trend_val = str(trend_val)
        return HttpResponse('{ "candleName":"' + candle_name +
                            '", "trendVal":"' + trend_val +
                            '", "spotDate":"' + spot_date +
                            '", "taRecommendation":"' + ta_recommendation +
                            '", "trend":"' + trend + '" }')

    def get_lstm_data(request):
        pred_list = list(predictions)
        send_list = []
        for ele in pred_list:
            single_price = ele.item()
            single_price = "{:.4f}".format(single_price)
            single_price = str(single_price)
            send_list.append(single_price)
        send_rmse = str(rmse)
        return HttpResponse('{ "rmse":"' + send_rmse +
                            '", "day_1":"' + send_list[0] +
                            '", "day_2":"' + send_list[1] +
                            '", "day_3":"' + send_list[2] +
                            '", "day_4":"' + send_list[3] +
                            '", "day_5":"' + send_list[4] + '" }')


    def get_lstm_plot(request):

        chart = forexLSTM.get_LSTM_plot(predictions)

        response = HttpResponse(content_type="image/jpeg")
        chart.savefig(response, format="png")
        return response

    def get_stock_plot(request):
        todayDate = utils.get_today_date()
        previousDate = utils.get_previous_date(13)
        chart = utils.get_stock_plot(previousDate, todayDate)

        response = HttpResponse(content_type="image/jpeg")
        chart.savefig(response, format="png")
        return response
