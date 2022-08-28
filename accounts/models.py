from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    birthday = models.DateField()


