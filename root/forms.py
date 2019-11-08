
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


FAVORITE_DAYS_CHOICES = [
    ('0', 'شنبه'),
    ('1', 'یک شنبه'),
    ('2', 'دو شنبه'),
    ('3', 'سه شنبه'),
    ('4', 'چهار شنبه'),
]

# class NewCoursForm(forms.Form):
#     department= forms.CharField()
#     name = forms.CharField()
#     course_number = forms.CharField()
#     group_number = forms.CharField()
#     teacher = forms.CharField()
#     start_time = forms.TimeField()
#     end_time = forms.TimeField()
#     first_day = forms.ChoiceField(
#         required=True,
#         # widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_DAYS_CHOICES,
#     )
#     second_day = forms.ChoiceField(
#         required=False,
#         default=null,
#
#         # widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_DAYS_CHOICES,
#     )



