import matplotlib as pl
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import pandas as pd
import os

import matplotlib.pyplot as plt
import numpy as np
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets

from forexPredict.models import Customer
from .algorithms import forexLSTM
pl.use('Agg')


@api_view(["POST"])
def CalcTest(x1):
    try:
        x = json.loads(x1.body)
        y = str(x * 100)
        return JsonResponse("Result:" + y, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)


class Customers(TemplateView):
    def getCust(request):
        name = 'liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')

    def getNums(request):
        n = np.array([2, 3, 4])
        name1 = "name-" + str(n[1])
        return HttpResponse('{ "name":"' + name1 + '", "age":31, "city":"New York" }')

    def getAvg(request):
        s1 = request.GET.get("val", "")
        if len(s1) == 0:
            return HttpResponse("none")
        l1 = s1.split(',')
        ar = np.array(l1, dtype=int)

        return HttpResponse(str(np.average(ar)))

    def getimage(request):
        plt = forexLSTM.get_plot()

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def getData(request):
        samp = np.random.randint(100, 600, size=(4, 5))
        df = pd.DataFrame(samp, index=['avi', 'dani', 'rina', 'dina'],
                          columns=['Jan', 'Feb', 'Mar', 'Apr', 'May'])
        return HttpResponse(df.to_html(classes='table table-bordered'))



class CustSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'type')


class CustViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustSerializer
