from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from MovieApp.models import UserReview

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label='', max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2',]

class SignInForm(forms.Form):
    username = forms.CharField(label='Username or Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ['title', 'text', 'rating']