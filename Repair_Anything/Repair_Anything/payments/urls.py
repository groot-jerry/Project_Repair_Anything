from django.urls import path
from . import views

urlpatterns = [

 path('payment/', views.make_payment, name='make_payment'),

]