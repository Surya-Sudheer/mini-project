from django.urls import include,path
from django import contrib
from .views import home,womenSignUp,ashaSignUp,ashalogin,whome,ashahome,wGuideline,wremainder,wprofile,ashaWomenInWard,ashaprofile,ashaupdate,ashaGuidlinesView
from .views import wupdate,start,month1,month2,month3,month4,month5,month6,month7,month8,month9
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
    path('ashaprofile/',ashaprofile,name='ashaprofile'),
    path('ashaupdate/',ashaupdate,name='ashaupdate'),
    path('ashaGuidlinesView/',ashaGuidlinesView,name='ashaGuidlinesView'),
    path('start/',start,name='start'),
    path('month1/',month1,name='month1'),
    path('month2/',month2,name='month2'),
    path('month3/',month3,name='month3'),
    path('month4/',month4,name='month4'),
    path('month5/',month5,name='month5'),
    path('month6/',month6,name='month6'),
    path('month7/',month7,name='month7'),
    path('month8/',month8,name='month8'),
    path('month9/',month9,name='month9'),
   
]
