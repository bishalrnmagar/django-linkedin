from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, ProfileForm

def register(request):
    form = RegisterForm
    errors = {}
    if request.user.is_authenticated:
        return redirect(reverse('notes.all'))
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request=request, user=user)
                    return redirect('notes.all')
            errors = form.error_messages
            print(errors)
    return render(request, 'user/form.html',{'form': form, 'errors': errors})

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

@login_required(login_url='user.login')
def update_profile(request):
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('notes.all'))
    return render(request, 'user/form.html', {'form': form})
