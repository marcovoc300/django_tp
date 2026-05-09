from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from .models import Moto
from .forms import MotoForm

# Inicio
def inicio(request):
    return render(request, "motos/inicio.html")

# Listado y Detalle
class MotoList(ListView):
    model = Moto
    template_name = "motos/motos_list.html"
    context_object_name = "motos"

class MotoDetail(DetailView):
    model = Moto
    template_name = "motos/moto_detail.html"

# EDITAR MOTO (Esto lo pidió el profe)
class MotoUpdate(UpdateView):
    model = Moto
    template_name = "motos/moto_form.html"
    fields = ['marca', 'modelo', 'descripcion', 'anio', 'imagen']
    success_url = reverse_lazy('motos_list')

# ELIMINAR MOTO (Esto también lo pidió)
class MotoDelete(DeleteView):
    model = Moto
    template_name = "motos/moto_confirm_delete.html"
    success_url = reverse_lazy('motos_list')

# Crear Moto
def crear_moto(request):
    if request.method == 'POST':
        form = MotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('motos_list')
    else:
        form = MotoForm()
    return render(request, 'motos/moto_form.html', {'form': form})

# Buscador
def buscar_moto(request):
    query = request.GET.get('modelo', '')
    if query:
        motos = Moto.objects.filter(modelo__icontains=query) | Moto.objects.filter(marca__icontains=query)
    else:
        motos = Moto.objects.all()
    return render(request, 'motos/resultado_busqueda.html', {'motos': motos, 'query': query})

# --- USUARIOS ---
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect("inicio")
    form = AuthenticationForm()
    return render(request, "motos/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("inicio")
    else:
        form = UserCreationForm()
    return render(request, "motos/register.html", {"form": form})

def logout_request(request):
    logout(request)
    return redirect("inicio")