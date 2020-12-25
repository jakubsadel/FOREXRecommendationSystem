from django.conf.urls import url
from django.urls import path, include

from forexPredict import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customers', views.CustViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^links/$', views.LinksPageView.as_view()),  # simple view
    url(r'^getcust/$', views.Customers.getCust),  # simple view
    url(r'^apitest/$', views.CalcTest),  # for REST API test
    url(r'^getnum/$', views.Customers.getNums),
    url(r'^getimg/$', views.Customers.getimage),
    url(r'^getdata/$', views.Customers.getData),
    url(r'^getavg/$', views.Customers.getAvg),

]
