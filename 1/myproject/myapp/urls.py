
from django.urls import path

from myapp import views

urlspatterns = [
    path('' , views.index, name='index'),

]