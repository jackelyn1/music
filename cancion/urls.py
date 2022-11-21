from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('inicio/', views.inicio, name='Inicio'),
]