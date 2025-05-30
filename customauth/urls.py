
from django.urls import path
from .views import Login, signup,forgot_password, Logout


urlpatterns = [
    path('signin/', Login.as_view(), name='signin'),
    path('logout/', Logout.as_view(), name='logout'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('signup/', signup, name='signup'),
]

