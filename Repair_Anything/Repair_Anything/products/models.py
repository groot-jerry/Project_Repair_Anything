from django.db import models

# Create your models here.
from django.db import models
from account.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    technician = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_products', null=True, blank=True)
    is_repaired = models.BooleanField(default=False)
