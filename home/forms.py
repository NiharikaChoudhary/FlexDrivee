from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Car

        
# car
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['carmodel','image', 'mileage', 'rating', 'color', 'seats', 'price', 'fuel_type']

class UserRegisterForm(UserCreationForm):
	fname=forms.CharField(max_length=122)
	username=forms.CharField(max_length=122)
	email=forms.EmailField(max_length=254)
	number=forms.CharField(max_length=12)
	password =forms.CharField(max_length=50)
	address= forms.CharField(max_length=122)
    
	class Meta:
		model = User
		fields = ['fname','username', 'email', 'number', 'password', 'address']
