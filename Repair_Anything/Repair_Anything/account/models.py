from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_technician = models.BooleanField('Is technician', default=False)
    technician_id = models.CharField(max_length=10, blank=True, null=True, unique=True)

class TechnicianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    experience = models.PositiveIntegerField(default=0)
    skills = models.CharField(max_length=255, blank=True)

class utechnicianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    experience = models.PositiveIntegerField(default=0)
    skills = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.user.username
    
    def is_complete(self):
        # Check if all required fields are filled
        return self.bio and self.experience and self.skills

