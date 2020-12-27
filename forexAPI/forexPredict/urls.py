from rest_framework import routers
from django.conf.urls import url
from forexPredict import views

router = routers.DefaultRouter()
router.register(r'stocks', views.StockViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^getcust/$', views.Stocks.getStock),
    url(r'^getnum/$', views.Stocks.getNums),
    url(r'^getimg/$', views.Stocks.getImage),
    url(r'^getdata/$', views.Stocks.getData),
    url(r'^getdejt/$', views.Stocks.getTodayDate),
]
