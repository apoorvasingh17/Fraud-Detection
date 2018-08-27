from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from django.contrib.auth.models import User

import datetime


class USER(models.Model):
    USER_REF = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="USER")
    NAME = models.CharField(max_length=100)
    PROFILE_LINK = models.CharField(max_length=100)
    

    def __str__(self):
        return self.NAME 

class Comment(models.Model):
 
    fullname = models.CharField(max_length=100)
    cardnumber = models.IntegerField(default=0)
    mm = models.IntegerField(default=0)
    yy=models.IntegerField(default=0)
    cvv=models.IntegerField(default=0)
    amount1= models.IntegerField(default=0)
 
    def __str__(self):   # __unicode__ on Python 2
        return self.fullname

