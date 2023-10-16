from django.shortcuts import render
from products.models import Product, ProductCategory
#функції = контролери = вьюхі


def index(request):
    context = {
        'title': 'StoRe',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categoties': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)