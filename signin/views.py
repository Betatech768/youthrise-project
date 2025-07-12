from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated:
        return redirect('create_post')  # Redirect already logged-in users

    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('create_post')  # Change to your dashboard/home URL name
            else:
                messages.error(request, 'Invalid credentials')
    return render(request, 'signin/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')
