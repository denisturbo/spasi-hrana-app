
from django.urls import path
from .views import CreateListing,DeleteListing, InfoTableList, EditListing

app_name = "listings"

urlpatterns = [
    path('create-listing/', CreateListing.as_view(), name='create'),
    path('delete-listing/<int:pk>/', DeleteListing.as_view(), name='delete'),
    path('edit-listing/<int:pk>', EditListing.as_view(), name='edit'),
    path('infotable/', InfoTableList.as_view(), name='infotable')

]

