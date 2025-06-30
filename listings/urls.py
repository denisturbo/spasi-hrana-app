
from django.urls import path
from .views import CreateListing,DeleteListing, InfoTableList

app_name = "listings"

urlpatterns = [
    path('create-listing/', CreateListing.as_view(), name='create'),
    path('delete-listing/<int:pk>/', DeleteListing.as_view(), name='delete'),
    path('infotable/', InfoTableList.as_view(), name='infotable')

]

