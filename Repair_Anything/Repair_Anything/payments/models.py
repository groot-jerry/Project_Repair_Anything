# Create your models here.

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
import datetime

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(default=datetime.datetime.now)  # Default value for new objects


    def __str__(self):
        return f"Payment #{self.id} - {self.user.username} - {self.product.name}"


    def save(self, *args, **kwargs):
        if not self.id:
            # Set date_paid to current date and time only if the object is being created
            self.date_paid = datetime.datetime.now()
        super().save(*args, **kwargs)
