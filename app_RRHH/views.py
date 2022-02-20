from django.shortcuts import render
from django.views import generic
from app_RRHH import models

# Create your views here.
class RrhhView(generic.View):
    cont = models.Empleado.objects.count()
    def get(self, request, *args, **kwargs):
        context = {
            'title':'RRHH',
            'contar':self.cont,
        }
        return render(request, 'rrhh.html', context)


