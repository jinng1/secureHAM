#Manager is needed if base user has different fields from django default user
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    #method for creating user
    def create_user(self,username, password,**extra_fields):
        user = self.model(
            username = username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    #method for creating superuser
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role','A')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username,password,**extra_fields)