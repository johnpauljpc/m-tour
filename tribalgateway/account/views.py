from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, decorators

# Create your views here.
from .forms import userCreationForm

class signupView(View):
    def get(self, request):
        form = userCreationForm()
        context = {'form':form}
        return render(request, 'account/signup.html', context)
    def post(self, request, *args, **kwargs):
        form = userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created")
            return redirect('index')
        return render(request, 'account/signup.html')
    


class loginView(View):
    def get(self, request):

        return render(request, 'account/login.html')
    def post(self, request, *args, **kwargs):
        # form = userCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, "account created")
        #     return redirect('index')
        return render(request, 'account/login.html')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password1']

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                
                login(request, user)
                messages.success(request, 'welcome  ' + user.username + ' You are now logged in')
                return redirect('/')

            messages.error(request, 'Your credentials are invalid, try again')
            return render(request, 'authentication/login.html')


class LogoutView(View):
    def get(self, request):
        messages.info(request, "You have been logged out")
        return redirect('/')