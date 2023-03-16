from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def register(request):
    if not(request.user.is_superuser):
        return redirect('/')
    
    return render(request, 'core/register.html')