<<<<<<< HEAD
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import Order, customer

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreationUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CastomersForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
=======
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import Order, customer

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreationUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CastomersForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
>>>>>>> 7511be836ccd1300326d827fd7d821c5e95ba3b4
        exclude = ['user']