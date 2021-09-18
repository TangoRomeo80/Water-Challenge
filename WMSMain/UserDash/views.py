from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random

# Create your views here.


def index(request):
    return render(request, 'UserDash/starter.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        Ph = [6.8]
        TDS = [200]
        Turb = [2]
        labels = []
        for i in range(1, 32):
            labels.append(str(i))
        default_items = []
        for i in range(1, 32):
            default_items.append(random.randint(155, 200))
        data = {
            "labels": labels,
            "default": default_items,
            "Ph": Ph,
            "TDS": TDS,
            "Turb": Turb,
        }
        return Response(data)
