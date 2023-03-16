from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def register(request):
    if request.user.is_anonymous:
        return redirect('signup')
    
    return render(request, 'core/register.html')
def contactUs(request):
    return render(request, 'core/contact-us.html')