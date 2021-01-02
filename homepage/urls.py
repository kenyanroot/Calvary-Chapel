from django.urls import path

from .views import index,youth,location,about,calvaryLearningCenter

urlpatterns = [
    path('',index,name='index'),
    path('index',index,name='index'),
    path('about',about,name='about'),
    path('location', location, name='location'),
    path('calvaryLearningCenter', calvaryLearningCenter, name='clc'),
    path('youth', youth, name='youth'),


]
