from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SeuUser(models.Model):
    username =  models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=128)
