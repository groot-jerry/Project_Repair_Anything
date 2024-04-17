from django.urls import path
from. import views


urlpatterns = [

path('products/', views.product_list, name='products'),
path('technician/<int:product_id>/', views.choose_technician, name='choose_technician')

]