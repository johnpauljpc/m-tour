from django.urls import path

from .views import index, register

urlpatterns = [
    path('', index, name='index'),
    path('get-started/', register, name='register')
]