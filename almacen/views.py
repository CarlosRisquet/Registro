from django.shortcuts import render
from .models import Almacen
from control.models import Articulo

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