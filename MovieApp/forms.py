from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2',]

class SignInForm(forms.Form):
    username = forms.CharField(label='Username or Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)