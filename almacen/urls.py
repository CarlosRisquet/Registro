from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Almacen'
urlpatterns = [
    path('inicio/',views.inicio, name = 'inicio_almacen'),
    path('registro_tienda/',views.reg_tienda, name = 'registro_tienda'),
    path('disponibilidad/',views.dispo_almacen, name='disponibilidad'),
    path('actualizar/<pk>',views.actualizar, name = 'actualizar')
]
