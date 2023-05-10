from django.urls import include,path
from django import contrib
from .views import home,womenSignUp,ashaSignUp,ashalogin,whome,ashahome

urlpatterns = [
    path('',home,name='home'),
    path('womenSignUp/',womenSignUp,name='womenSignUp'),
    path('ashaSignUp/',ashaSignUp,name='ashaSignUp'),
    path('ashalogin/',ashalogin,name='ashalogin'),
    path('whome/',whome,name='whome'),
    path('ashahome/',ashahome,name='ashahome'),
]
