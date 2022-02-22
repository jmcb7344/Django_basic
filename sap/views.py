from django.shortcuts import render
from django.views import generic


class HomeView(generic.View):
    """Esta es la vista de la pag de inicio"""

    def get(self, request, *args, **Kwargs):
        context = {
            'titulo':'Inicio',
            }
        return render(request, 'index.html', context)