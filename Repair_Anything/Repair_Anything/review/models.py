
# Create your models here.

from django.db import models
from account.models import User


def average_rating(self):
        reviews = self.review_set.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            return total_rating / len(reviews)
        else:
            return "No reviews yet"

class Review(models.Model):
    technician = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
