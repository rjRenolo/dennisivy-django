from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product, Order, Costumer

def home(request):
    orders = Order.objects.all()
    costumers = Costumer.objects.all()
    context = {'orders':orders, 'costumers':costumers}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

def costumer(request):
    return render(request, 'accounts/costumer.html')
