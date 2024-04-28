# review/models.py

from django.db import models
from account.models import User
from account.models import TechnicianProfile

class Review(models.Model):
    technician = models.ForeignKey(TechnicianProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Rating out of 5, for example
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.technician.user.username} by {self.user.username}"
