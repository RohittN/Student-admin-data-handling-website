from django.db import models
from django.contrib.auth.models import User

class stdform(models.Model):
    Name = models.CharField(max_length=200)
    Phonenumber=models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    Message=models.CharField(max_length=200)

class loginform(models.Model):
    Username = models.CharField(max_length=200)
    Password=models.CharField(max_length=200)

class stdregister(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    Phonenumber=models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
