from django.urls import path
from . import views

urlpatterns = [
    path('tres/', views.vistaTres, name='vistaTres'),
    path('cuatro/', views.vistaCuatro, name='vistaCuatro'),
]