from rest_framework import routers
from django.conf.urls import url
from forexPredict import views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^getstockdata/$', views.Stocks.get_stock_data),
    url(r'^getstockplot/$', views.Stocks.get_stock_plot),
    url(r'^getlstmdata/$', views.Stocks.get_lstm_data),
    url(r'^getlstmplot/$', views.Stocks.get_lstm_plot),
    url(r'^getpatternsdata/$', views.Stocks.get_patterns),
]
