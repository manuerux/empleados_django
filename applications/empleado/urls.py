from django.contrib import admin
from django.urls import path
from .views import (ListAllEmpleados, ListByArea, ListaEmpleadosByKeyword, ListaHabilidadesEmpleado,
                    EmpleadoDetailView, EmpleadoCreateView, SuccessView, EmpleadoUpdateView, EmpleadoDeleteView,
                    InicioView)

app_name = 'empleado_app'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('listar-todo-empleado/', ListAllEmpleados.as_view()),
    path('list-by-area/<name>', ListByArea.as_view()),
    path('buscar-empleado/', ListaEmpleadosByKeyword.as_view()),
    path('lista-habilidades-empleado/', ListaHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', EmpleadoDetailView.as_view()),
    path('crear-empleado/', EmpleadoCreateView.as_view()),
    path('success/', SuccessView.as_view(), name='empleado_creado_correctamente'),
    path('actualizar-empleado/<pk>/', EmpleadoUpdateView.as_view(), name='actualizado'),
    path('borrar-empleado/<pk>/', EmpleadoDeleteView.as_view(), name='borrado'),
]