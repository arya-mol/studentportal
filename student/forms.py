from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["username","first_name","last_name","email_id","password1","password2","phone","address1","address2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email_id": forms.EmailInput(attrs={"class": "form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "address1": forms.TextInput(attrs={"class": "form-control"}),
            "address2": forms.TextInput(attrs={"class": "form-control"})
        }


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
