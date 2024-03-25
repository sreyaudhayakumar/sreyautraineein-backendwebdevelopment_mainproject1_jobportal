# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You may need to customize this logic based on your requirements
            user_type = form.cleaned_data['user_type']
            user.user_type = user_type
            user.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
