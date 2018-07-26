from django.shortcuts import render
from django.utils import timezone
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})