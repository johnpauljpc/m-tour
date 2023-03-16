from django.urls import path
from .views import signupView, LoginView, LogoutView

urlpatterns = [
    path('signup/', signupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]