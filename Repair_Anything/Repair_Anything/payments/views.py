from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Payment
from products.models import Product
from account import views

def make_payment(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        # Logic to process payment
        amount = request.POST.get('amount')
        Payment.objects.create(product=product, amount=amount)
        product.is_repaired = True
        product.save()
        return redirect('product_list')  # Redirect to product list after successful payment
    return render(request, 'payments/payment.html', {'product': product})

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')