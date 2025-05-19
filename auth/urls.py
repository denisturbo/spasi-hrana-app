
from django.urls import path
from .views import signin, signup,forgot_password



urlpatterns = [
    path('signin/', signin, name='signin'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('signup/', signup, name='signup')
]

