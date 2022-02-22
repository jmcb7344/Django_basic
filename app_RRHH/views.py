from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from app_RRHH import models

# Create your views here.
class HomeView(generic.View):
    title = 'Recursos Humanos'

    def get(self, request, *args, **kwargs):
        activo = models.Empleado.objects.filter(activo=True).count()
        no_activo = models.Empleado.objects.filter(activo=False).count()
        empleado = models.Empleado.objects.all()
        contar = models.Empleado.objects.count()
        context = {
            'title':self.title,
            'activo':activo, 
            'noactivo': no_activo,
            'empleado':empleado,
            'contar':contar,
        }
        return render(request, 'rrhh.html', context)

 
class CreatePersona(generic.CreateView):
    model = models.Empleado
    fields = "__all__"
    
    def get_success_url(self):
        return reverse_lazy('app_RRHH:rrhhhome')


class DetalleView(generic.DetailView):
    model = models.Empleado


class EditarView(generic.UpdateView):
    model = models.Empleado
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('app_RRHH:rrhhhome')


class DeleteViews(generic.DeleteView):
    model = models.Empleado

    def get_success_url(self):
        return reverse_lazy('app_RRHH:rrhhhome')