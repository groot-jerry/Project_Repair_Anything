from django.db import models
from account.models import User
from account.models import TechnicianProfile
from django.utils import timezone

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    technician = models.CharField(max_length=100, default='default_value')
    rating = models.IntegerField()
    comment = models.TextField()
    
    def __str__(self):
        return f"Review for {self.technician.user.username} by {self.user.username}"
