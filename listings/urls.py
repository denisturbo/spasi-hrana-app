
from django.urls import path
from .views import create, InfoTableList

app_name = "listings"

urlpatterns = [
    path('create-listing/', create, name='create'),
    path('infotable/', InfoTableList.as_view(), name='infotable')

]

