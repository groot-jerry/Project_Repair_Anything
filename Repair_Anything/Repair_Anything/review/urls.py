from django.urls import path
from review import views

urlpatterns = [
    path('add_review/', views.add_review, name='add_review'),
    path('reviewsuccess/', views.review_success, name='review_success'),
]
