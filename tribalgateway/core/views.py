from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def register(request):
    if request.user.is_anonymous:
        messages.info(request, "before you get started, please login or signup")
        return redirect('login')
    
    return render(request, 'core/register.html')
def contactUs(request):
    return render(request, 'core/contact-us.html')