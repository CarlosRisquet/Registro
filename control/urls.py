"""Registro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Control'
urlpatterns = [
    path('reg_pieza/',views.reg_piezas, name = 'registro_pieza'),
    path('reg_municipio/',views.reg_municipio, name = 'municipio'),
    path('registro/',views.registro, name = 'registro'),
    path('listado/',views.listado, name = 'listado'),
    path('registro_productos/',views.reg_producto, name = 'registro_producto'),
    path('tipo_venta/',views.reg_tipo, name = 'tipo_venta'),
    path('actualizar_pedido/<pk>',views.PedidoUpdate, name = 'update'),
    path('actualizar_producto/<pk>',views.ProductoUpdate, name= 'update_producto'),
    path('detalles/<pk>',views.detalles_pedidos, name = 'detalles_pedido'),
    path('delete/<pk>',views.PedidoDeleteView.as_view(), name= 'delete')
  #  path('filtrado/',views.filtrado, name= 'filtrado')
]