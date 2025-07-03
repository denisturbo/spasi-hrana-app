
from django.urls import path
from .views import CreateListing,delete_list, InfoTableList

app_name = "listings"

urlpatterns = [
    path('create-listing/', CreateListing.as_view(), name='create'),
    path('delete-listing/<int:pk>/', delete_list, name='delete'),
    path('infotable/', InfoTableList.as_view(), name='infotable')

]

