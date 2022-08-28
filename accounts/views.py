from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Account,Image


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, "Username Or Password is incorrect!!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def create_user(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            image = form.cleaned_data['image']
            if password1 != password2:
                check1 = True
                messages.error(request, 'Password does\'t matched',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(request, 'Username already exists',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(request, 'Email already registered',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if check1 or check2 or check3:
                messages.error(
                    request, "Registration Failed", extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username,
                    email=email, password=password1, image=image)
                messages.success(
                    request, f'Thanks for registering {user.username}!',
                    extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('accounts:login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
