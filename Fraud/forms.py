from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Fraud.models import Comment

class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        required = True,
        label = 'NAME',
        max_length = 100
    )
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'EMAIL',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class UserAuthenticationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class question:
    class Meta:
        field=('question')



class MyCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['fullname', 'cardnumber', 'mm', 'yy','cvv','amount1']


