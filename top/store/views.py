from django.shortcuts import render
from .models import Product, SliderImage

def home(request):
    products = Product.objects.all()
    slides = SliderImage.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')

    products = products.filter(category=category) if category else products
    products = products.filter(brand=brand) if brand else products
    return render(request, 'home.html', {'products':products, 'slides':slides})

def product(request, pk):
    product_data = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product':product_data})