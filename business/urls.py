
from django.urls import path
from .views import create


urlpatterns = [
    path('create-listing/', create, name='listingcreation'),

]

