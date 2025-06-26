
from django.urls import path
from .views import CreateListing, InfoTableList

app_name = "listings"

urlpatterns = [
    path('create-listing/', CreateListing.as_view(), name='create'),
    path('infotable/', InfoTableList.as_view(), name='infotable')

]

