from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout

def sign_in(request):
    form = SignInForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('store:home')
    return render(request, 'sign_in.html', {'form': form})

def sign_up(request):
    form = SignUpForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        print(request)
        return redirect('users:sign_in')
    return render(request, 'sign_up.html', {'form':form}) 

def sign_out(request):
    logout(request)
    return redirect('users:sign_in')
    

