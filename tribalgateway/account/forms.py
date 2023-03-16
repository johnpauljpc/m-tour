from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class userCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'nationality','password1', 'password2',  'passport']