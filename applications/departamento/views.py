from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm

from applications.empleado.models import Empleado
from .models import Departamento

# Create your views here.
class NewRegisterDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        depa = Departamento(name=form.cleaned_data['departamento'], short_name=form.cleaned_data['short_name'])
        depa.save()
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewRegisterDepartamentoView, self).form_valid(form)
