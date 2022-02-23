from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from app_RRHH import models
from app_RRHH.forms import EditarF

# Create your views here.
class HomeView(generic.View):
    title = 'Recursos Humanos'

    def get(self, request, *args, **kwargs):
        activo = models.Empleado.objects.filter(activo=True).count()
        no_activo = models.Empleado.objects.filter(activo=False).count()
        empleado = models.Empleado.objects.all().order_by('id')
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

#Otra forma de Editar un Objeto
class EditView(generic.View):

    def get(self, request, id, *args, **kwargs):
        persona = get_object_or_404(models.Empleado, pk=id)
        form = EditarF(instance=persona)
        context = {
            'title':'Vista de Edit',
            'form':form,
        }
        return render(request, 'edit.html', context)

    def post(self, request,id, *args, **kwargs):
        persona = get_object_or_404(models.Empleado, pk=id)
        if request.method=='POST':
            form = EditarF(request.POST, instance=persona )
            if form.is_valid():
                form.save()
                return redirect('app_RRHH:rrhhhome')

class DeleteViews(generic.DeleteView):
    model = models.Empleado

    def get_success_url(self):
        return reverse_lazy('app_RRHH:rrhhhome')