from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from customauth.forms import CustomLoginForm, CustomerSignupForm, BusinessSignupForm
from django.contrib.auth import login
from django.contrib.auth import get_user_model, logout

#Auth Views

UserModel = get_user_model()

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


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    model = UserModel
    print(model)
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return super().delete(request, *args, **kwargs)

    def get_template_names(self):
        user = self.request.user
        print(user)
        if hasattr(user, 'businessuser'):
            return ["business/settings.html"]
        return ["customer/profile/settings.html"]