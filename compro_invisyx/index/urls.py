from django.urls import path
from .views import *

app_name = 'index'

urlpatterns = [
    path('', index, name="index"),
    path('contact-us/', contactus, name="contactus"),
    path('our-services', our_services, name="our_services"),
]