from django.urls import include,path
from django import contrib
from .views import home,womenSignUp,ashaSignUp,ashalogin,whome,ashahome,wGuideline,wremainder,wprofile,ashaWomenInWard
from .views import wupdate
urlpatterns = [
    path('',home,name='home'),
    path('womenSignUp/',womenSignUp,name='womenSignUp'),
    path('ashaSignUp/',ashaSignUp,name='ashaSignUp'),
    path('ashalogin/',ashalogin,name='ashalogin'),
    path('whome/',whome,name='whome'),
    path('ashahome/',ashahome,name='ashahome'),
    path('wGuideline/',wGuideline,name='wGuideline'),
    path('wremainder/',wremainder,name='wremainder'),
    path('wprofile/',wprofile,name='wprofile'),
    path('wupdate/',wupdate,name='wupdate'),
    path('ashaWomenInWard/',ashaWomenInWard,name='ashaWomenInWard'),
   
]
