from rest_framework import routers
from django.conf.urls import url
from forexPredict import views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^getstockdata/$', views.Stocks.getStockData),
    url(r'^getimg/$', views.Stocks.getImage),
    url(r'^getlstm/$', views.Stocks.getLSTM),
    url(r'^getlstmplot/$', views.Stocks.getLSTMplot),
]
