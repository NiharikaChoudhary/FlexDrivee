
from django.contrib import admin
from django.urls import path
from home import views
from .views import logout_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='home'),
    path('subscription', views.subscription, name='subscription'),
    # path('subscription/details/<int:car_id>/', views.subscription_details_view, name='subscription_details'),
    path('subscription/details/<int:car_id>/', views.subscription_details_view, name='subscription_details'),
    
    path('subscription/details/<int:car_id>/confirm/', views.confirm_subscription, name='confirm_subscription'),
    path('contact', views.contact, name='contact'),
    path('blogs', views.blogs, name='/blogs'),
    path('about', views.about, name='/about'), 
    path('book', views.book, name='book'),
 
    path('Car', views.Car, name='Car'),
    path('profile', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    # path('logout', views.logout, name='logout'),
    path('logout/', logout_view, name='logout'),
   
    # login signup logout
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.logoutuser, name='logout'),


    path('faq', views.faq, name='faq'),
    path('testimonial', views.testimonial, name='testimonial'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)