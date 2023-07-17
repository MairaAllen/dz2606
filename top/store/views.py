from django.shortcuts import render, redirect
from .models import Product, SliderImage, Guest, CartItem
from django.http import HttpResponse
from django.db.models import Q

def home(request):
    products = Product.objects.all()
    slides = SliderImage.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    search = request.GET.get('search')

    products = Product.objects.filter(Q(name__icontains=search)) if search else products
    products = products.filter(category=category) if category else products
    products = products.filter(brand=brand) if brand else products
    return render(request, 'home.html', {'products':products, 'slides':slides})

def product(request, pk):
    product_data = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product':product_data})

def guest_register(request, pk):
    token = request.COOKIES['csrftoken']
    guest = Guest.objects.filter(token=token)

    if not guest:
        Guest.objects.create(token=token)
        guest = Guest.objects.filter(token=token)

    cart_item = CartItem.objects.filter(product=pk)

    if not cart_item:
        CartItem.objects.create(
            guest = guest[0],
            product = Product.objects.get(pk=pk),
            quantity = 1,
            customer = request.user if request.user.is_authenticated else None
        )

    else:
        cart_item[0].quantity +=1
        cart_item[0].save()
    
    return redirect('store:home')

def cart(request):
    token = request.COOKIES['csrftoken']
    guest = Guest.objects.filter(token=token)

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(customer=request.user)
    else:
        cart_items = CartItem.objects.filter(guest=guest[0]) if guest else []

    return render(request, 'cart.html', {'cart_items': cart_items})