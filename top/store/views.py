from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


def home(request):
    products = Product.objects.all()
    slides = SliderImage.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')

    action = request.GET.get('action')
    if action:
        favorite(request)
        return redirect('store:home')

    products = products.filter(category=category) \
        if category else products
    products = products.filter(brand=brand) \
        if brand else products
    return render(request, 'home.html', {'products': products, 'slides': slides})


def product(request, pk):
    product_data = Product.objects.get(pk=pk)
    action = request.GET.get('action')
    if action:
        favorite(request,pk)
        return redirect('store:product', pk=pk)
    return render(request, 'product.html', {'product': product_data})


def guest_register(request, pk):
    token = request.COOKIES['csrftoken']
    guest = Guest.objects.filter(token=token)

    if not guest:
        Guest.objects.create(token=token)
        guest = Guest.objects.filter(token=token)

    cart_item = CartItem.objects.filter(
        product=pk,
        guest=guest[0] if request.user.is_anonymous else None,
        customer=request.user if request.user.is_authenticated else None
        )

    if not cart_item:
        CartItem.objects.create(
            guest=guest[0],
            product=Product.objects.get(pk=pk),
            quantity=1,
            customer=request.user if request.user.is_authenticated else None
        )

    else:
        cart_item[0].quantity += 1
        cart_item[0].save()

    return redirect('store:home')


def cart(request):
    token = request.COOKIES['csrftoken']
    guest = Guest.objects.filter(token=token)
    action = request.GET.get('action')
    cart_item_pk = request.GET.get('pk')
    confirm_delete = False

    if action == 'delete':
        confirm_delete = True
    elif action == 'increment' or action == 'decrement':
        edit_cart(action, cart_item_pk)
        return redirect('store:cart')
    elif action == 'favorite':
        favorite(request)
        return redirect('store:cart')


    if request.GET.get('confirm'):
        confirm_delete = True
        CartItem.objects.get(pk=cart_item_pk).delete()
        return redirect('store:cart')

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(customer=request.user)
    else:
        cart_items = CartItem.objects.filter(guest=guest[0]) if guest else []

    total_quantity = sum([i.quantity for i in cart_items])
    total_sum = sum([i.total_price() for i in cart_items])

    return render(request, 'cart.html', {'cart_items': cart_items, 
                                         'confirm_delete': confirm_delete, 
                                         'total_quantity': total_quantity, 
                                         'total_sum': total_sum}
                                         )

def edit_cart(action, pk):
    cart_item = CartItem.objects.get(pk=pk)
    if action == 'increment':
        cart_item.quantity += 1
        cart_item.save()

    if action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()

@login_required(login_url='/users/sign_in/')
def create_order(request):


    cart_items = CartItem.objects.filter(customer=request.user)
    if not cart_items:
        return render(request, 'error.html', {})

    total_price = sum(item.total_price() for item in cart_items)
    amount = sum(item.quantity for item in cart_items)

    form = OrderForm(request.POST or None)
    
    if form.is_valid():
        order = Order.objects.create(
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            total_price=total_price,
            customer=request.user
        )
        for item in cart_items:
            OrderProduct.objects.create(
                order=order, 
                product=item.product,
                amount=item.quantity,
                total=item.total_price()
                )
        cart_items.delete()
        return redirect('store:home')
    
    return render(request, 'order_create.html',
                  {'cart_items': cart_items,
                   'total_price': total_price,
                   'amount': amount,
                   'form': form
                   })

def favorite(request, pk=None):
    product_pk = request.GET.get('product') if not pk else pk
    product_detail = Product.objects.get(pk=product_pk)
    product_detail.favorite.add(request.user) \
        if request.user not in product_detail.favorite.all() \
        else product_detail.favorite.remove(request.user)

   
def favorite_page(request):
    favorite_products = Product.objects.filter(favorite=request.user)
    action = request.GET.get('action')
    if action:
        favorite(request)
        return redirect('store:favorite')
    
    return render(request, 'favorite.html', {'favorites':favorite_products})  
