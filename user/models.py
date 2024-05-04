from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #image = models.ImageField(upload_to='products/images/')  # Aquí indicas dónde se almacenarán las imágenes
    # Agrega otros campos según sea necesario, como imagen, categoría, etc.

    def __str__(self):
        return self.name
    

from django.db import models


class ItemCarrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    # Otros campos relevantes
