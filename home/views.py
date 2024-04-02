from django.shortcuts import render, redirect,get_object_or_404
# from datetime import datetim
from home.models import Contact
from home.models import Signup
from home.models import Book
from home.models import Car
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import mySubscription
# 

# update profile
from django.contrib.auth.decorators import login_required

# car etails
def subscription_details_view(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'subscription_details.html', {'car': car})
# confirm subscription
@login_required
def confirm_subscription(request, car_id):
    if request.method == 'POST':
        user = request.user
        car = Car.objects.get(id=car_id)
        # Process form data and save subscription details
        subscription = mySubscription.objects.create(user=user, car=car)
        # Redirect to a success page or display a success message
        messages.success(request, "Your subscription is confirmed")
        return render(request, 'subscription_details.html', {'car': car}) # Change 'success_page' to the URL name of your success page
    else:
        messages.error(request, "Invalid request method")
        return render(request, 'subscription_details.html', {'car': car}) 

@login_required
def update_profile(request):
    if request.method == "POST":
        # Get the user instance
        user = request.user
        
        # Get the data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        # Update the user's profile
        user.username = username
        user.email = email
        user.save()
        
        # Optionally, you can add more fields to update
        
        # Display success message
        messages.success(request, "Profile updated successfully")
        
        # Redirect to the profile page or any other page
        return redirect('profile')  # Assuming you have a URL named 'profile'
    
    # If the request method is not POST, render the form page
    return render(request, 'profile_update.html')




# Create your views here.
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page or any other page after adding the car
    else:
        form = CarForm()
    return render(request, 'subscription.html', {'form': form})


# def car_list(request):
#     cars = Car.objects.all()  # Querying all cars from the database
#     return render(request, 'subscription.html', {'cars': cars})


def index(request):
    return render(request,'index.html')
def subscription(request):
    cars = Car.objects.all()
    return render(request, 'subscription.html', {'cars': cars})
    # return render(request, 'subscription.html')
def subscribe(request):
    return render(request, 'car_desc.html')
def blogs(request):
    return render(request, 'blog.html')
def about(request):
    return render(request, 'about.html')
def profile(request):
    return render(request,'profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')
# def logout(request):
#     messages.success(request, "You have been logged out")
#     return render(request,'logout.html')
def book(request):
    if request.method == "POST":
        
       
    # Continue with your view logic

        fname = request.POST.get('fname')
        number = request.POST.get('number')
        address = request.POST.get('address')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        
        # Debugging statements
        print("Received data:")
        print("fname:", fname)
        print("number:", number)
        print("address:", address)
        print("sdate:", sdate)
        print("edate:", edate)
        
        # Create and save Book instance
        book = Book(fname=fname, number=number, address=address, sdate=sdate, edate=edate)
        try:
            book.save()
        except Exception as e:
            print("Error saving book instance:", str(e))
        
        # Optionally, you can return a success message or redirect to another page
        messages.success(request, "Booking has been successful. Please find a subscription plan from below.")
        return redirect('subscription')  # Assuming you have a URL named 'subscription'

    return render(request, 'subscription.html')


# login signup logout

def signup(request):
    
    
    if request.method == "POST":
        # fname = request.POST.get('fname')
        username = request.POST.get('username')
        # email = request.POST.get('email')
        # number = request.POST.get('number')
        # password = request.POST.get('password')
        # address = request.POST.get('address')
        if User.objects.filter(username=username).exists():
            # Username already exists, display an error message
            messages.error(request, "Username already exists. Please choose a different username.")
            return render(request, 'signup.html')
        else:
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            number = request.POST.get('number')
            address = request.POST.get('address')
            # Create the user
            myuser = User.objects.create_user(username=username, email=email, password=password)
            
            myuser.first_name = fname
            myuser.number=number
            myuser.address=address
            myuser.save()
          
            messages.success(request, "you has been registered as a new user")
            return render(request,'index.html')
            # Create and save  instance

            # Optionally, you can return a success message or redirect to another page
        

    
    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate the user
        user = authenticate(request,username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, "You have been logged in")
            return render(request, 'index.html')
        else:
            messages.error(request, "Incorrect email or password")
            return render(request, 'login.html')
        form = AuthenticationForm()
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    messages.success(request, "you are logged out")
    return render(request, 'index.html')




# contact
def contact(request):
   
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        hearaboutus = request.POST.get('hear-about-us')
        desc = request.POST.get('desc')
        
      
            # Create and save Contact instance
        contact = Contact(name=name, email=email, hearaboutus=hearaboutus, desc=desc)
        contact.save()
            # Optionally, you can return a success message or redirect to another page
        messages.success(request, "Your message has been sent successfully")
        return render(request,'index.html')
       

    return render(request, 'contact.html')

def faq(request):
    return render(request,'faq.html')
def testimonial(request):
    return render(request,'testimonial.html')