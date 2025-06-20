
from django.urls import path
from .views import create,InfoTableList

app_name = 'promocodes'

urlpatterns = [
    path('create-promocode/', create, name='create'),
    path('promocode-infotable/', InfoTableList.as_view(), name='infotable')

]

