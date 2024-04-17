from django.db import models

# Create your models here.

from products.models import Product

class Payment(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
