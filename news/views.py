from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def index(request):
    content = {
        'title': 'Home',
        'sliderData': Slider.objects.all()

    }
    return render(request, 'pages/home/home-view.html', content)


def about(request):
    content = {
        'title': 'About'
    }
    return render(request, 'pages/about/about-view.html', content)


def contact(request):
    return render(request, 'pages/contact/contact-view.html')


def product_details(request, slug):
    content = {
        'productDetailsData': Product.objects.filter(slug=slug)

    }

    return render(request, 'pages/product/product-details-view.html', content)


def user_register(request):
    if request.method == 'POST':
        data = UserCreationForm(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request, 'User was successfully register')
            return redirect('register')
        else:
            redirect('register')
    else:
        content = {
            'userRegister': UserCreationForm
        }
        return render(request, 'pages/login/register-view.html', content)


def user_login(request):
    if request.method == 'POST':
        data = AuthenticationForm(data=request.POST)
        if data.is_valid():
            user = data.get_user()
            login(request, user)
            return redirect('users')
        else:
            return redirect('login')
    else:
        content = {
            'loginForm': AuthenticationForm

        }
        return render(request, 'pages/login/login-view.html', content)


@login_required(login_url='login')
def users(request):
    return render(request, 'pages/users/users-view.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return HttpResponse('Invalid Access')
