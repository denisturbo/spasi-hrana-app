from django.shortcuts import render

#Auth Views 

def signin(request): 
    return render(request, 'auth/signin.html')


def forgot_password(request):
    return render(request, 'auth/forgot_password.html')

def signup(request):
    return render(request, 'auth/signup.html')