from datetime import datetime
from random import choice, choices
from re import M
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

# Create your models here.

#hospital model
class Hospital(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

#items model
class Items(models.Model):
    product_name = models.CharField(max_length=40)
    def __str__(self):
        return self.product_name

#inventory model
class Inventory(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def itemName(self):
        return self.item.product_name

    def itemId(self):
        return self.item.id
    
    def __str__(self):
        return self.item.product_name


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

    # hospital = Hospital.objects.all()
    # HOSPITAL_CHOICES = [
    #     (1,hospital[0].name),
    #     (2,hospital[1].name),
    #     (3,hospital[2].name),
    #     (4,hospital[3].name),
    #     (5,hospital[4].name),
    #     (6,hospital[5].name),
    # ]

    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE, null=True)
    passwordChangedAt = models.DateTimeField(default = datetime.now())

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()