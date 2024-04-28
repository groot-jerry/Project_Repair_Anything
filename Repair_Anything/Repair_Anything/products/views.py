# Create your views here.

from django.shortcuts import render, redirect
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def choose_technician(request, product_id):
    product = Product.objects.get(pk=product_id)
    # Logic to choose a technician and assign to the product
    return redirect('technician_list')  # Redirect to product list after choosing technician
