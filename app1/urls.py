from django.urls import path
from . import views

urlpatterns = [
    path('uno/', views.vistaUno, name= 'vistaUno'),
    path('dos/', views.vistaDos, name= 'vistados'),
]
