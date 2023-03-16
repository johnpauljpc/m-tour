from django.urls import path

from .views import index, register, contactUs

urlpatterns = [
    path('', index, name='index'),
    path('get-started/', register, name='register'),
    path('contact-us/', contactUs, name="contact-us"),
]