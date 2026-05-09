from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pages/', views.MotoList.as_view(), name='motos_list'),
    path('pages/<int:pk>/', views.MotoDetail.as_view(), name='moto_detail'),
    path('crear-moto/', views.crear_moto, name='crear_moto'),
    path('buscar-moto/', views.buscar_moto, name='buscar_moto'),
    
    # NUEVAS RUTAS PARA EDITAR Y ELIMINAR
    path('pages/editar/<int:pk>/', views.MotoUpdate.as_view(), name='editar_moto'),
    path('pages/eliminar/<int:pk>/', views.MotoDelete.as_view(), name='eliminar_moto'),

    # URLs de Usuario
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register, name='register'),
]