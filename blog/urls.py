from django.urls import path, include
from .views import blog,Blogpost,st,BlogClass,search

urlpatterns = [
    path('blog', BlogClass.as_view(), name='blog'),
    path('post/<int:pk>', Blogpost.as_view(), name='post'),
    path('search',search,name='search'),

]