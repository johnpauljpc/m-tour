from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "core/index.html")

@login_required(login_url='login')
def register(request):
    # if request.user.is_anonymous:
    #     messages.info(request, "before you get started, please login or signup")
    #     return redirect('login')
    
    return render(request, 'core/register.html')
def contactUs(request):
    return render(request, 'core/contact-us.html')