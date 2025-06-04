
from django.urls import path
from .views import create


urlpatterns = [
    # path('', business_landing, name='business_landing'),
    path('create-listing/', create, name='listingcreation'),

]

