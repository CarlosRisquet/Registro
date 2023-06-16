from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm,MunicipioForm,PedidoForm, Tipo_VentaForm,ArticuloForm
from .models import Pedido, Producto, Tipo_Venta, Articulo
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
@login_required(login_url='/login')
def reg_piezas(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = ArticuloForm()
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
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El Pedido fué agregado satisfactoriamente.")
            return render(request,'index.html')
    else:
        form = PedidoForm()
        return render(request,'registro.html', {'form':form})

@login_required(login_url='/login')    
def listado(request):
    registros = Pedido.objects.all()
    return render(request,'listado.html',context={'registros':registros})

def PedidoUpdate(request,pk):
    pedidos = Pedido.objects.get(id= pk)
    if request.method == 'POST':
        pedidos.numero = request.POST['numero']
        pedidos.municipio.municipio = request.POST['municipio']
        pedidos.fecha_compra = request.POST['fecha_compra']
        pedidos.orden_trabajo = request.POST['orden_trabajo']
        pedidos.pre_fact = request.POST['pre_fact']
        pedidos.fact = request.POST['fact']
        pedidos.fecha = request.POST['fecha']
        pedidos.entregado = request.POST['entregado']
        pedidos.recibe = request.POST['recibe']
        pedidos.save()
        messages.add_message(request, messages.SUCCESS, "El Pedido fué actualizado satisfactoriamente.")
        return redirect(f"/control/actualizar_pedido/{pedidos.id}")
    else:
        tipos = Tipo_Venta.objects.all()
        articulos = Articulo.objects.all()
        productos = Producto.objects.filter(pedido_id = pk)
        form = PedidoForm(instance=pedidos)
        return render(request, template_name="update.html", context={ 'form': form, 'pedidos': pedidos, 'productos': productos, 'tipos':tipos,'articulos': articulos })


def reg_producto (request):
    pedido_id = request.POST ['pedido_id']
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        producto = Producto(
            pedido_id = pedido_id,
            articulo_id = request.POST['articulo'],
            cantidad = request.POST['cantidad'],
            import_fact = request.POST['import_fact'],
            precio_tienda = request.POST['precio_tienda'],
            tipo_id = request.POST['tipo_id']
        )
        producto.save()
        messages.add_message(request, messages.SUCCESS, "El Producto fué agregado satisfactoriamente.")
    return redirect(f"/control/actualizar_pedido/{pedido.id}")

def ProductoUpdate (request,pk):
    producto = Producto.objects.get(id = pk)
    if request.method == 'POST':
        pedido_id = request.POST['pedido_id']
        pedido = Pedido.objects.get(id = pedido_id) 
        producto = Producto.objects.get(id = pk)
        if request.method == 'POST':
            print(request.POST['articulo'])
            producto.cantidad = request.POST['cantidad']
            producto.tipo_id = request.POST['tipo_id']
            producto.precio_tienda = request.POST['precio_tienda'].replace(',', '.')
            producto.import_fact = request.POST['import_fact'].replace(',', '.')
            producto.articulo_id = request.POST['articulo']
            producto.save()
            messages.add_message(request, messages.SUCCESS, "El Producto fué actualizado satisfactoriamente.")
    return redirect(f"/control/actualizar_pedido/{pedido.id}")

def detalles_pedidos (request,pk):
    pedido = Pedido.objects.get(id=pk)
    productos = Producto.objects.filter(pedido_id = pedido.id)
    Importe_tiendaT = 0
    Descuento_pasarelaT = 0
    Importe_pasarelaT = 0
    Total_pagarT = 0
    Importe_facturaT = 0
    Precio_tiendaT = 0
    for producto in productos:
        Importe_tiendaT += producto.importe_tienda
        Descuento_pasarelaT += producto.descuento_pasarela
        Importe_pasarelaT += producto.importe_pasarela
        Total_pagarT += producto.total_pagar
        Precio_tiendaT += producto.precio_tienda
        Importe_facturaT += producto.import_fact
    return render(request,'detalles.html',{'productos':productos,'Importe_facturaT':Importe_facturaT,'Importe_tiendaT':Importe_tiendaT,'Descuento_pasarelaT':Descuento_pasarelaT,'Importe_pasarelaT':Importe_pasarelaT,'Total_pagarT':Total_pagarT,'Precio_tiendaT':Precio_tiendaT})
    

class PedidoDeleteView(SuccessMessageMixin,DeleteView):
    model = Pedido
    template_name = "delete.html"
    context_object_name = 'pedido'
    success_url=reverse_lazy("Control:listado")
    success_message = "El Pedido fué eliminado correctamente"


#class RegistroUpdateView(UpdateView):
#    model = Registro
#    template_name = "update.html"
#    form_class = RegistroForm
#    success_url=reverse_lazy("Control:listado")


# class RegistroDeleteView(DeleteView):
#    model = Registro
#    template_name = "delete.html"
#   success_url=reverse_lazy("Control:listado")

def filtrado(request):
    pedidos = Pedido.objects.all()
    articulo = Articulo.objects.all()
    producto = Producto.objects.all()
    tipo = Tipo_Venta.objects.all()
    if ('pedido' in request.GET and request.GET ['pedido'] != ''):
        pedidos = pedidos.filter( numero = request.GET ['pedido'])
    if ('codigo' in request.GET and request.GET ['codigo'] !=''):
        articulo1 = articulo.filter( codigo = request.GET ['codigo'])
        print(articulo1)
        producto = producto.filter(articulo_id = articulo1.id)
        print(producto)
        pedidos = pedidos.filter(id = producto.pedido_id)
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
    return render(request,'resultados.html',{ 'pedidos': pedidos }) 