from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Form to handle user sign-in
class SignInForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

# Form to handle user registration (if required)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = [ 'email', 'password1', 'password2']
