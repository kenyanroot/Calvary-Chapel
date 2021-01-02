from django.contrib import admin
from django.urls import path, include
from .views import signup,login_function,loginpage,signuppage,signup_view,get_name
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login_function, name='login'),
    # path('register', get_name, name='register'),
    path('signin', loginpage, name='signin'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),


]
