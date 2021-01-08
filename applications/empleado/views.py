from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.db.models.functions import Lower
from django.urls import reverse_lazy
from .models import Empleado


class InicioView(TemplateView):
    """vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = "empleado/list_all.html"
    paginate_by = 4
    model = Empleado


class ListByArea(ListView):
    template_name = "empleado/list_by_area.html"
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        area = self.kwargs.get('name')
        queryset = Empleado.objects.filter(departamento__name=area.capitalize())
        return queryset

class ListaEmpleadosByKeyword(ListView):
    template_name = "empleado/by_kword.html"
    context_object_name = "empleados"
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        print(lista)
        return lista

class ListaHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.Habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "el puto amo"
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'Habilidades']
    success_url = reverse_lazy('empleado_app:empleado_creado_correctamente')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class SuccessView(TemplateView):
    template_name = 'empleado/success.html'


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/actualizar.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'Habilidades']
    success_url = "."

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        apellidos = request.POST.get("last_name")
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/borrar.html"
    success_url = "."

    def get_context_data(self, **kwargs):
        import pdb;pdb.set_trace()
        empleado = kwargs.get("object")
        eliminado = f'Se ha eliminado el empleado {empleado.full_name}'
        context = {"eliminado": eliminado}
        return context
