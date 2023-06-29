from django.shortcuts import render,redirect
from django.views.generic import DeleteView
from .models import Almacen
from control.models import Articulo
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    return render(request,'index_almacen.html')

def reg_tienda (request):
    articulos = Articulo.objects.all()
    if request.method == 'POST':
        almacen = Almacen(
            articulo_id = request.POST['articulo'],
            cantidad = request.POST['cantidad'],
            imagen = request.FILES['imagen']
        )
        almacen.save()
    return render(request,'registro_tienda.html',{'articulos':articulos})

def dispo_almacen(request):
    almacen = Almacen.objects.all()
    return render(request,'disponibilidad.html',{'almacen':almacen})

def actualizar(request,pk):
    almacen = Almacen.objects.all()
    almacen1 = Almacen.objects.get(id = pk)
    if request.method == 'POST':
        if (request.POST['cantidad'] != ''):
            almacen1.cantidad = int(request.POST['cantidad'])
            almacen1.save()
        else:
            almacen1 = []
    return render(request,'disponibilidad.html',{'almacen':almacen})

def admin (request):
    almacen = Almacen.objects.all()
    return render(request,'admin.html',{'almacen':almacen})


class AlmacenDeleteView(DeleteView):
    model = Almacen
    template_name = "delete_art.html"
    context_object_name = 'articulo'
    success_url=reverse_lazy("Almacen:administrador")
    success_message = "El Artículo fué eliminado correctamente"
