
from django.urls import path

from myapp import views

urlsPattarns = [
    path('' , views.index, name='index'),
    path('atmath.P')
]