from django.shortcuts import render
from django.views import generic
from app_RRHH import models

# Create your views here.
class RrhhView(generic.View):
    cont = models.Empleado.objects.count()
    activos = models.Empleado.objects.filter(activo=True).count
    noactv = models.Empleado.objects.filter(activo=False).count
    empleado = models.Empleado.objects.order_by('id')
    def get(self, request, *args, **kwargs):
        context = {
            'title':'RRHH',
            'contar':self.cont,
            'activo':self.activos,
            'noactv':self.noactv,
            'empleado':self.empleado,
        }
        return render(request, 'rrhh.html', context)


class DetalleView(generic.DetailView):
    model = models.Empleado

    """def get(self, request,id, *args, **kwargs):
        empleado = self.model.objects.get(pk=id)
        context ={
            'persona':empleado
        }
        return render(request, 'detalle.html', context)"""