from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomLoginForm
#Auth Views 


def forgot_password(request):
    return render(request, 'auth/forgot_password.html')

def signup(request):
    return render(request, 'auth/signup.html')





class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'auth/logout.html'
    next_page = '/'
    
class Login(LoginView):
    template_name = "auth/signin.html"
    form_class = CustomLoginForm