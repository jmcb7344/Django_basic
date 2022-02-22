from django.urls import path
from app_RRHH import views

app_name='app_RRHH'

urlpatterns = [
    path('', views.HomeView.as_view(), name='rrhhhome'),
    path('<int:pk>/',views.DetalleView.as_view(), name='detalle'),
    path('create', views.CreatePersona.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteViews.as_view(), name='delete'),
    path('editar/<int:pk>/', views.EditarView.as_view(), name='editar'),
]