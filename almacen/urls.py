from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Almacen'
urlpatterns = [
    path('registro_tienda/',views.reg_tienda, name = 'registro_tienda'),
]