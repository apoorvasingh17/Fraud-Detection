from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import *
from django.contrib.auth.models import User
from django.http import *
from django.conf import settings
import json

from django.template import loader

from database.functions import *
from Fraud.forms import *
from django.http import HttpResponse
from django.utils import timezone



def home(request):
    return render(request, 'home.html')


def sign_in_up_view(request):
    signin_form = UserAuthenticationForm()
    singnup_form = UserRegistrationForm()
    return render(request, 'home.html', {'signin' : signin_form, 'signup':singnup_form})


def sign_in_view(request):
    form = UserAuthenticationForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        username = userObj['username']
        password =  userObj['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return add_model(request)
        else:
            raise forms.ValidationError('Looks like a username with that email or password is incorrect!!')
    return render(request, template_name, {'form' : form})


def sign_up_view(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        name = userObj['name']
        username = userObj['username']
        email =  userObj['email']
        password =  userObj['password']
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username = username, password = password)
            create_user(user, name)
            login(request, user)
            return add_model(request)
        else:
            raise forms.ValidationError('Looks like a username with that email or password already exists')
    return redirect('/')

def add_model(request):
 
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
 
    else:
 
        form = MyCommentForm()
 
    return render(request, "portal.html", {'form': form})
