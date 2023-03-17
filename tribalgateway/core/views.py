from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import check_if_authenticated

# Create your views here.
def index(request):
    try:
        request.GET['get-started']
        messages.success(request, f"Congratulations <b>{request.user}</b>, Your application was successful")
        return redirect('/')
    except:
       pass
    return render(request, "core/index.html")

@check_if_authenticated
def register(request):
    
    context = {
        
    }
    # if request.user.is_anonymous:
    #     messages.info(request, "before you get started, please login or signup")
    #     return redirect('login')
    
    return render(request, 'core/register.html', context)
def contactUs(request):
    return render(request, 'core/contact-us.html')