from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db import models

class UserForm(UserCreationForm):
    """
    Custom form for user registration (sign up).
    """

    email = forms.EmailField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    dob = forms.DateField()

    class UserForm(UserCreationForm):
        dob = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}),
            label="Date of Birth",
        )

        class Meta:
            model = User
            fields = ['email', 'first_name', 'last_name', 'dob', 'password1', 'password2']

class UserAuthenticationForm(AuthenticationForm):
    """
    Custom form for user login.
    """
    username = forms.EmailField(label="Email")

