from django import forms
from .bulma_mixin import BulmaMixin
from .models import Order

class OrderForm(BulmaMixin, forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Напишите адрес доставки'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Напишите номер телефона'
    }))

    class Meta:
        model = Order
        fields = ['address', 'phone']