from django.urls import include,path
from django import contrib
from .views import home

urlpatterns = [
    path('',home,name='home')
]
