
from django.urls import path
from .views import Login, Logout, business_signup, customer_signup


urlpatterns = [
    path('signin/', Login.as_view(), name='signin'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/business/', business_signup, name='business-signup'),
    path('signup/', customer_signup, name='signup')

]

