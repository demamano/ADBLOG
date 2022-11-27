from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegisterForm(UserCreationForm):
    class Meta: #nested namespace for configuration
        model = User
        fields = ['username','email','password1','password2']
# class UserProfileForm