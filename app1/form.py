from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import order,customer

class OrderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CustomerForm(ModelForm):
	class Meta:
		model = customer
		fields = '__all__'
		exclude = ['user']