from django.db import models

class Categoria(models.Model):
    Nombre = models.CharField(max_length=200, blank= False, default='')
    Icono = models.CharField(max_length=500, blank= False, default='')
    Descripcion = models.CharField(max_length=500, blank= False, default='')

class Stock_En_Tienda(models.Model):
    SKU = models.CharField(max_length=200, blank= False, default='')
    Categori_ID = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pvp = models.DecimalField(max_digits=5, decimal_places=2)
    margen_ganancia = models.DecimalField(max_digits=5, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
    tiene_iva = models.BooleanField()
    Estado = models.CharField(max_length=50)

class Tienda1(models.Model):
    ID_Ciudad = models.IntegerField()
    Nombre = models.CharField(max_length=200, blank= False, default='')
    Logo = models.CharField(max_length=500, blank= False, default='')    
    
class Tienda2(models.Model):
    ID_Ciudad = models.IntegerField()
    Nombre = models.CharField(max_length=200, blank= False, default='')
    Logo = models.CharField(max_length=500, blank= False, default='')    

class Tienda3(models.Model):
    ID_Ciudad = models.IntegerField()
    Nombre = models.CharField(max_length=200, blank= False, default='')
    Logo = models.CharField(max_length=500, blank= False, default='')

class Tienda4(models.Model):
    ID_Ciudad = models.IntegerField()
    Nombre = models.CharField(max_length=200, blank= False, default='')
    Logo = models.CharField(max_length=500, blank= False, default='')

class Producto(models.Model):
    Stock = models.ForeignKey(Stock_En_Tienda, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200, blank= False, default='')
    Presentacion = models.CharField(max_length=200, blank= False, default='')
    Marca = models.CharField(max_length=100, blank= False, default='')
    Fabricante = models.CharField(max_length=100, blank= False, default='')
    Foto = models.CharField(max_length=500, blank= False, default='')
    Venta_al_granel= models.BooleanField(default=False)
    Descripcion = models.TextField()
    Nivel_Azucar = models.DecimalField(max_digits=5, decimal_places=2)
    Nivel_Sal = models.DecimalField(max_digits=5, decimal_places=2)
    Nivel_Grasa = models.DecimalField(max_digits=5, decimal_places=2)
    Estado = models.CharField(max_length=50)
    
class SubCategoria(models.Model):
    ID_Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200, blank= False, default='')
    Icono = models.CharField(max_length=500, blank= False, default='')
    Descripcion = models.CharField(max_length=500, blank= False, default='')