from django.urls import path
from .views import *
app_name = 'user'
urlpatterns = [
    path('signup', signup, name = 'signup'),
    path('signin', signin, name = 'signin'),
     path('logout', logoutuser, name = 'logoutuser'),
]