from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Напишите никнейм')
    password = forms.CharField(
        widget=forms.PasswordInput(), label='Напишите пароль')

    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Придумайте никнейм')
    password1 = forms.CharField(
        widget=forms.PasswordInput(), label='Придуймайте пароль')
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Повторите пароль')
    email = forms.EmailField(label='Введите адрес почты')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(BulmaMixin, forms.ModelForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    username = forms.CharField(label='Никнейм')
    email = forms.CharField(label='Адрес почты')

    class Meta:
        model = User
        fields =['first_name','last_name','username','email']