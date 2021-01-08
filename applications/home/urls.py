from django.contrib import admin
from django.urls import path
from .views import PruebaView, PruebaListView, ListarPrueba, PruebaCreateView


urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista-prueba/', ListarPrueba.as_view()),
    path('add/', PruebaCreateView.as_view(), name='prueba_add'),
    #path('/', PruebaCreateView.as_view()),
]