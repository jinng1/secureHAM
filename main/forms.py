from turtle import textinput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm, TextInput
from .models import CustomUser, Inventory, Items


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','role','hospital')

    def save(self,commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','role','hospital')


class addItemForm(ModelForm):
    class Meta:
        model = Items
        fields = '__all__'

class managerItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(managerItemForm, self).__init__(*args, **kwargs)
        self.fields['item'].disabled = True
    class Meta:
        model = Inventory
        exclude = ['hospital', 'status']
        # fields = '__all__'