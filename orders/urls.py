from django.urls import path
from .views import CreateOrder, OrdersTableList,CompleteOrder

app_name = "orders"

urlpatterns = [
    path('create/<int:pk>/', CreateOrder.as_view(), name='create'),
    path('table/', OrdersTableList.as_view(), name='table'),
    path('complete/<int:pk>/', CompleteOrder.as_view(), name='complete')
]
