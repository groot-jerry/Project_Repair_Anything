
# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model

class Review(models.Model):
    technician = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField()  # Assuming you want to store rating as an integer
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.technician.username}"
