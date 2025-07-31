
from django.urls import path
from .views import CreateListing,DeleteListing, InfoTableList, EditListing, ListingDetailView, ListingView, \
    AvailableListingsAPI

app_name = "listings"

urlpatterns = [
    path('create-listing/', CreateListing.as_view(), name='create'),
    path('delete-listing/<int:pk>/', DeleteListing.as_view(), name='delete'),
    path('edit-listing/<int:pk>', EditListing.as_view(), name='edit'),
    path('infotable/', InfoTableList.as_view(), name='infotable'),
    path('listing/<int:pk>/', ListingDetailView.as_view(), name='listingDetail'),
    path('listings/', ListingView.as_view(), name='listingList'),
    path('api/', AvailableListingsAPI.as_view({'get': 'list'}), name="api")

]

