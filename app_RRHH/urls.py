from django.urls import path
from app_RRHH import views

app_name='app_RRHH'

urlpatterns = [
    path('', views.RrhhView.as_view(), name='rrhhhome')
]