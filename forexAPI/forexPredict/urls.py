from rest_framework import routers
from django.conf.urls import url
from forexPredict import views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^getstockdata/$', views.Stocks.getStockData),
    url(r'^getimg/$', views.Stocks.getStockPlot),
    url(r'^getlstmdata/$', views.Stocks.getLSTMdata),
    url(r'^getlstmplot/$', views.Stocks.getLSTMPlot),
    url(r'^getpatterns/$', views.Stocks.getPatterns),
]
