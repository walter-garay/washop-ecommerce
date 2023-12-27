from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=22, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    stock = models.PositiveIntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=80, blank=True, null=True)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    proveedores_id = models.ManyToManyField(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre 
