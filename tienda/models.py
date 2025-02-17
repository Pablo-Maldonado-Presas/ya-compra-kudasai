from django.db import models
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle_producto', args=[str(self.id)])