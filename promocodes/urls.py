
from django.urls import path
from .views import CreatePromocode,InfoTableList
app_name = 'promocodes'

urlpatterns = [
    path('create-promocode/', CreatePromocode.as_view(), name='create'),

    path('promocode-infotable/', InfoTableList.as_view(), name='infotable')

]

