from rest_framework import routers
from django.conf.urls import url
from forexPredict import views

router = routers.DefaultRouter()
router.register(r'stocks', views.StockViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^getstockdata/$', views.Stocks.getStockData),
    url(r'^getimg/$', views.Stocks.getImage),
    url(r'^getnum/$', views.Stocks.getNums),
    url(r'^getdata/$', views.Stocks.getData),
    url(r'^getlstm/$', views.Stocks.getLSTM),
]
