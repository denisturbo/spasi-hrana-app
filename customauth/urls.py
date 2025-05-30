
from django.urls import path
from .views import Login,forgot_password, Logout, business_signup, customer_signup


urlpatterns = [
    path('signin/', Login.as_view(), name='signin'),
    path('logout/', Logout.as_view(), name='logout'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('signup/business/', business_signup, name='business-signup'),
    path('signup/', customer_signup, name='signup')

]

