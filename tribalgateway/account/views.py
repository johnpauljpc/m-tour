from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from .forms import userCreationForm

class signupView(View):
    def get(request):
        form = userCreationForm()
        context = {'form':form}
        return render(request, 'account/signup.html', context)
    def post(self, request, *args, **kwargs):
        return render(request, 'account/signup.html')
