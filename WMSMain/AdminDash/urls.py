from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    url('chartAPI', views.ChartData.as_view(), name='chart'),
]
