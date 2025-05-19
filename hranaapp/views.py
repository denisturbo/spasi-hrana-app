from django.shortcuts import render

#Hrana app views 

def index(request):
    return render(request, 'landing/main.html')

def faq(request):
    return render(request, 'faq/faq.html')


def baba(request):
    return render(request, 'errors/404.html')