from django.urls import path
from . import views  # importa views.py de tu app

urlpatterns = [
    path("", views.calcular, name="calcular"),
]
