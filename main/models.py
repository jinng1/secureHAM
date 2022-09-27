from datetime import datetime
from re import M
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

# Create your models here.

#hospital model
class Hospital(models.Model):
    name = models.CharField(max_length=40)

#items model
class Items(models.Model):
    product_name = models.CharField(max_length=40)

#inventory model
class Inventory(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    quantity = models.IntegerField()

#request model
class Requests(models.Model):
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    STATUS = [
        ('submitted','Submitted'),
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected')
    ]
    status = models.CharField(
        max_length = 9,
        choices = STATUS,
        default = 'submitted'
    )

#custom user model
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    ROLE_CHOICES = [
        ("S","Staff"),
        ("M","Manager"),
        ("A","Admin")
    ]
    role = models.CharField(max_length=1,choices = ROLE_CHOICES, default="S")

    HOSPITAL_CHOICES = [
        ("1","Tan Tock Seng Hospital"),
        ("2","Ng Teng Fond General Hospital"),
        ("3", "National University Hospital"),
        ("4","Changi General Hospital"),
        ("5", "Raffles Hospital"),
        ("6", "Thomson Medical Centre"),
    ]

    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE, null=True,choices = HOSPITAL_CHOICES)
    passwordChangedAt = models.DateTimeField(default = datetime.now())

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()