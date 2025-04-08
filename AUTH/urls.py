from django.urls import path
from .views import *

urlpatterns = [
    path('', auth_home, name='auth_home' ),
    path('signup', email_signuup, name='email_signup' ),
    path('login', email_login, name='email_login' ),
]



