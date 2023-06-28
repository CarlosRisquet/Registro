from django.db import models
from control.models import Articulo
# Create your models here.

class Almacen (models.Model):
    id = models.BigAutoField(primary_key=True)
    articulo  = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to=f'static/images/', default='imagen')

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacen'

    def __str__(self):
        return self.articulo