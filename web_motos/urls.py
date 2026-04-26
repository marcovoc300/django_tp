from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('motos.urls')),
    path('accounts/perfil/', accounts_views.ver_perfil, name='perfil'),
    path('accounts/perfil/editar/', accounts_views.editar_perfil, name='editar_perfil'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
