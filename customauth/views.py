from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from customauth.forms import CustomLoginForm, CustomerSignupForm, BusinessSignupForm
from django.contrib.auth import login

#Auth Views

def customer_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerSignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('/')
        else:
            form = CustomerSignupForm()
        return render(request, 'auth/signup.html', {'form': form})
    else:
        return redirect('/')


def business_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = BusinessSignupForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('/')
        else:
            form = BusinessSignupForm()
        return render(request, 'auth/signup_business.html', {'form': form})
    else:
        return redirect('/')
               
class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    
class Login(LoginView):
    template_name = "auth/signin.html"
    form_class = CustomLoginForm


    