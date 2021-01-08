from django.contrib import admin
from django.urls import path
from .views import NewRegisterDepartamentoView

urlpatterns = [
    path('new-departamento/', NewRegisterDepartamentoView, name='nuevo_departamento'),
]