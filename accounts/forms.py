from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100, min_length=5,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, min_length=5,
                                widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    username = forms.CharField(label='Username', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    email = forms.EmailField(label='Email', max_length=50, min_length=5,
                             required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    password2 = forms.CharField(label='Confirm Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

