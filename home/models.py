from django.db import models
import datetime
from django.contrib.auth.models import User
# car model
class Car(models.Model):
    image = models.ImageField(upload_to='car_images/')
    mileage = models.FloatField()
    rating = models.FloatField()
    color = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=100, default='')
    seats = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=20)
    def __str__(self):
        return self.carmodel 
# confirm subscription
class mySubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Assuming you have a Car model
    # Add more fields as needed for subscription details

    def __str__(self):
        return f"{self.user.username}'s subscription for {self.car.carmodel}"

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email = models.EmailField(default='')

    hearaboutus=models.CharField(max_length=12)
    desc=models.TextField()
    def __str__(self):
       return self.name
   
class Signup(models.Model):
    fname=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    email = models.EmailField(default='')

    number=models.CharField(max_length=12)
    password =models.CharField(max_length=50)
    address= models.TextField()
    def __str__(self):
       return self.fname
    


    

class myuser(models.Model):
    fname=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    email = models.EmailField(default='')

    number=models.CharField(max_length=12)
    password =models.CharField(max_length=50)
    address= models.TextField()
    def __str__(self):
       return self.fname

class Book(models.Model):
    fname=models.CharField(max_length=122)
    number=models.CharField(max_length=12)
    address=models.TextField()
    sdate = models.DateField(default=datetime.date.today)
    edate = models.DateField(default=datetime.date.today)  # Example default value

    def __str__(self):
       return self.fname