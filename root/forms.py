from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password = forms.PasswordInput()


    class Meta:
        model = User
        fields = ('username', 'password')

