from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50)
    contact = models.PositiveIntegerField(default=1,unique=True)
    email   = models.EmailField(unique=True)
    college = models.CharField(max_length=50)
    branch  = models.CharField(max_length=50)
    course  = models.CharField(max_length=50)
    sem     = models.IntegerField(default=1)
    city    = models.CharField(max_length = 50)
    otp     = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    

    def __str__(self):
        return self.first_name