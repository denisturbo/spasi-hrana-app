
from django.urls import path
from .views import CreatePromocode, InfoTableList, DeletePromocode

app_name = 'promocodes'

urlpatterns = [
    path('create-promocode/', CreatePromocode.as_view(), name='create'),
    path('delete-promocode/<int:pk>/', DeletePromocode.as_view(), name='delete'),
    path('promocode-infotable/', InfoTableList.as_view(), name='infotable')

]

