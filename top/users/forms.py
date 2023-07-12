from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin

class SignInForm(BulmaMixin,AuthenticationForm):
    username = forms.CharField(label = 'Никнейм')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

    class Meta:
        model = User
        fields = ['username', 'password']

class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label = 'Придумайте никнейм')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Придумайте пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')
    email = forms.EmailField(label='Введите адрес электронно почты')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
