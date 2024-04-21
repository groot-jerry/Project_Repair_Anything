from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('technician/', views.technician, name='technician'),
    path('technician_list/',views.technician_list, name='technician_list'),
    path('review/',views.add_review, name='add_review'),
]

