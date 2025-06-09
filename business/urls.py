
from django.urls import path
from .views import create, InfoTableList


urlpatterns = [
    # path('', business_landing, name='business_landing'),
    path('create-listing/', create, name='listingcreation'),
    path('infotable/', InfoTableList.as_view(), name='infotable')

]

