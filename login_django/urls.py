from django.urls import path
from login_django.views import *

urlpatterns = [
    path('', loginPage, name='loginPage'),
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('reset-password/', resetPassword, name='resetPassword'),
]
