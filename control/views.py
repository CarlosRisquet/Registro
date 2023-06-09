from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PiezaForm,MunicipioForm,RegistroForm, Tipo_VentaForm
from .models import Registro, Pieza, Tipo_Venta
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
@login_required(login_url='/login')
def reg_piezas(request):
    if request.method == 'POST':
        form = PiezaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = PiezaForm()
        return render(request,'registro_pieza.html', {'form':form})
@login_required(login_url='/login')    
def reg_municipio(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = MunicipioForm()
        return render(request,'municipio.html', {'form':form})
    
@login_required(login_url='/login')    
def reg_tipo(request):
    if request.method == 'POST':
        form = Tipo_VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = Tipo_VentaForm()
        return render(request,'tipo_venta.html', {'form':form})
    
@login_required(login_url='/login')   
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = RegistroForm()
        return render(request,'registro.html', {'form':form})

@login_required(login_url='/login')    
def listado(request):
    registros = Registro.objects.all()
    return render(request,'listado.html',context={'registros':registros})

def detalles(request,pk):
    registros = Registro.objects.get(id= pk)
    return render(request,'detalles.html',context={'registros':registros})


class RegistroUpdateView(UpdateView):
    model = Registro
    template_name = "update.html"
    form_class = RegistroForm
    success_url=reverse_lazy("Control:listado")


class RegistroDeleteView(DeleteView):
    model = Registro
    template_name = "delete.html"
    success_url=reverse_lazy("Control:listado")

def filtrado(request):
    registro = Registro.objects.all()
    pieza = Pieza.objects.all()
    tipo = Tipo_Venta.objects.all()
    if ('pedido' in request.GET and request.GET ['pedido'] != ''):
        registros = registro.filter( pedido = request.GET ['pedido'])
    if ('codigo' in request.GET and request.GET ['codigo'] !=''):
        piezas = pieza.filter( codigo = request.GET ['codigo'])
        for pieza in piezas:
            registros = registro.filter(pieza_id = pieza.id)
    if ('fecha' in request.GET and request.GET ['fecha'] !=''):
        registros = registro.filter( fecha_compra = request.GET ['fecha'])
    if ('entrega_fecha' in request.GET and request.GET ['entrega_fecha'] !=''):
        registros = registro.filter( fecha = request.GET ['entrega_fecha'])
    if ('parte' in request.GET and request.GET ['parte'] !=''):
        piezas = pieza.filter( pieza = request.GET ['parte'])
        pieza = piezas[0]
        registros = registro.filter( pieza_id = pieza.id)
    if ('venta' in request.GET and request.GET ['venta'] !=''):
        tipos = tipo.filter(tipo = request.GET ['venta'] )
        tipo = tipos[0]
        registros = registro.filter(tipo_id = tipo.id)
    return render(request,'resultados.html',{ 'registros': registros })
    
    
