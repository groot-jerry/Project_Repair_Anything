from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')
    
    def __str__(self):
        return self.name

    
