from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pages/', views.MotoList.as_view(), name='motos_list'),
    path('pages/<int:pk>/', views.MotoDetail.as_view(), name='moto_detail'),
    path('crear-moto/', views.crear_moto, name='crear_moto'),
    path('buscar-moto/', views.buscar_moto, name='buscar_moto'),
    # URLs de Usuario
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register, name='register'),
]