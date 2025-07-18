
from django.urls import path
from .views import CreatePromocode, InfoTableList, DeletePromocode, PromocodeEdit

app_name = 'promocodes'

urlpatterns = [
    path('create-promocode/', CreatePromocode.as_view(), name='create'),
    path('delete-promocode/<int:pk>/', DeletePromocode.as_view(), name='delete'),
    path('edit-promocode/<int:pk>/', PromocodeEdit.as_view(), name='edit'),
    path('promocode-infotable/', InfoTableList.as_view(), name='infotable')

]

