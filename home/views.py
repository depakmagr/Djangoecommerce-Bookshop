from django.shortcuts import render
from .models import *

# Create your views here.

def homeview(request):
    context = {}
    return render(request, 'index.html',context)


def shop(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request,'shop.html',context)


def contact(request):
    context = {}
    return render(request, 'contact.html',context)


def singleproduct(request):
    context = {}
    return render(request, 'single-product.html',context)


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)

def myaccount(request):
    context = {}
    return render(request, 'myaccount.html', context)