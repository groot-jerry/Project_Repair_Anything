# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings

class Review(models.Model):

    rating = models.IntegerField()  # Assuming you want to store rating as an integer
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.technician.username}"
