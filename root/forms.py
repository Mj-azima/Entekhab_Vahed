
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class SignInForm(forms.ModelForm):

    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'password')

class ContactForm(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(
        required=True,
        widget=forms.Textarea,
        max_length=250,
        min_length=10
    )

