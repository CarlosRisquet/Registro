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
    path('detalles/<pk>',views.detalles, name = 'detalles'),
    path('tipo_venta/',views.reg_tipo, name = 'tipo_venta'),
    path('actualizar/<pk>',views.RegistroUpdateView.as_view(), name = 'update'),
    path('delete/<pk>',views.RegistroDeleteView.as_view(), name= 'delete'),
    path('filtrado/',views.filtrado, name= 'filtrado')
]