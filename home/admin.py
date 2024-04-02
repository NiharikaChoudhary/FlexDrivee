from django.contrib import admin
from home.models import Contact
from home.models import Signup
from home.models import myuser
from home.models import Book
from home.models import Car
from home.models import mySubscription
# Register your models here.
admin.site.register(Contact)
admin.site.register(myuser)
admin.site.register(Signup)
admin.site.register(Book)
admin.site.register(Car)
admin.site.register(mySubscription)

