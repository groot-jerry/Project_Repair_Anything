# Create your models here.

from django.db import models
from django.conf import settings
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User


from django.contrib.auth import get_user_model

class Payment(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f"Payment of ${self.amount} by {self.user.username}"

    class Meta:
        verbose_name_plural = 'Payments'
         
