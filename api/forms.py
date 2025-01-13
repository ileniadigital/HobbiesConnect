from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from api.models import User
from django.forms import CharField, DateField, DateInput, EmailField

class UserForm(UserCreationForm):
    '''
    Custom form for user registration (sign up).
    '''
    email = EmailField(max_length=150)
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)
    dob = DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label="Date of Birth",
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'dob', 'password1', 'password2']

class UserAuthenticationForm(AuthenticationForm):
    '''
    Custom form for user login.
    '''
    username = EmailField(label="Email", max_length=150)