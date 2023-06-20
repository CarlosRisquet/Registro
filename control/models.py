from django.db import models

# Create your models here.
class Municipio(models.Model):
    municipio = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipio' 

    def __str__(self):
        return self.municipio
    

class Articulo (models.Model):
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero = models.CharField(max_length=15)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now=False)
    orden_trabajo = models.CharField(max_length=20)
    pre_fact = models.CharField(default = '-',max_length=20)
    fact = models.CharField(default = '-', max_length=20)
    fecha = models.DateField(auto_now=False)
    entregado = models.CharField(max_length=50)
    recibe = models.CharField(max_length=50)

    def __str__(self):
        return str(self.numero)

    @property
    def producto(self):
        return Producto.objects.filter(pedido_id = self.id).first()


class Tipo_Venta(models.Model):
    tipo = models.CharField("Tipo de Venta", max_length=50)

    def __str__(self):
        return self.tipo
    


class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo = models.ForeignKey(Tipo_Venta, on_delete=models.CASCADE)
    precio_tienda = models.FloatField()
    import_fact = models.FloatField()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos' 

    def __str__(self):
        return str(self.id)

    
    @property
    def importe_tienda(self):
        return round(((self.precio_tienda * self.cantidad) +34.95),2)


    @property
    def descuento_pasarela(self):
        return round((self.importe_tienda * 0.02),2)
        
    @property
    def importe_pasarela(self):
        return round(((self.precio_tienda - ((self.precio_tienda * self.descuento_pasarela)/ 100)) * self.cantidad),2)
    
    @property
    def total_pagar(self):
        return round(self.precio_tienda + 34.95 - self.descuento_pasarela,2)
    
    @property
    def m_pasarela(self):
        return round(self.importe_tienda + self.importe_pasarela,2)
