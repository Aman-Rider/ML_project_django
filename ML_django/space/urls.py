from django.urls import path
from .views import *
app_name = 'space'
urlpatterns = [
    path('', home, name = 'home')
]