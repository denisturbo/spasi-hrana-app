
from django.urls import path
from .views import signin, signup,forgot_password,logout_view


urlpatterns = [
    path('signin/', signin, name='signin'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout')
]

