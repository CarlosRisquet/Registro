from django.db import models

# Create your models here.

class Pieza(models.Model):
    pieza = models.CharField(max_length=50)
    codigo = models.CharField(max_length=15)


    class Meta:
        verbose_name = 'Pieza'
        verbose_name_plural = 'Pieza' 

    def __str__(self):
        return self.pieza

class Municipio(models.Model):
    municipio = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipio' 

    def __str__(self):
        return self.municipio

class Tipo_Venta(models.Model):
    tipo = models.CharField("Tipo de Venta", max_length=50)

    def __str__(self):
        return self.tipo

class Registro(models.Model):
    pedido = models.CharField(max_length=12)
    fecha_compra = models.DateField(auto_now=False)
    cantidad = models.IntegerField()
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_Venta, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    orden_trabajo = models.CharField(max_length=20)
    precio_tienda = models.FloatField()
    import_fact = models.FloatField()
    pre_fact = models.CharField(default = '-',max_length=20)
    fact = models.CharField(default = '-', max_length=20)
    entregado = models.CharField(max_length=50)
    recibe = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=False)

    @property
    def fullname(self):
        return self.nombre + ' ' + self.apellido_1 + ' ' + self.apellido_2
    
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
