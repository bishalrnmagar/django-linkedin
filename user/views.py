from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm

def register(request):
    form = UserCreationForm
    if request.user.is_authenticated:
        return redirect(reverse('notes.all'))
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('user.login')
    return render(request, 'user/form.html',{'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('notes.all'))
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('notes.all')
    form = LoginForm
    return render(request, 'user/form.html',{'form': form})

def sign_out(request):
    logout(request)
    return redirect('user.login')
