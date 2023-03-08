from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
class LoginForm(forms.Form) :
    User = get_user_model()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
class RegisterForm(forms.Form) :
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput()
    )