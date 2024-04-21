from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:technician_id>/add_review/', views.add_review, name='add_review'),
]
