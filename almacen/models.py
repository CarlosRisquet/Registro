from django.db import models
from control.models import Articulo
# Create your models here.

class Almacen (models.Model):
    id = models.BigAutoField(primary_key=True)
    articulo  = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacen'

    def __str__(self):
        return self.articulo