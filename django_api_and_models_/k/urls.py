"""k URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
import django
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from user import views as user_views
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, views as auth_views

import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    
    
    path('',user_views.home),
    path('register/',user_views.register,name='register'),
    path('home/',user_views.home, name='home'),
    path('login/', user_views.login,name='login'),
    path('logout/', user_views.logout,name='logout'),
    path('users/', user_views.users),
    path('users/<pk>/', user_views.users_detail,name='detail'),
    path('profile/', user_views.view_profile, name='profile'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path('change_password/', user_views.change_password, name='change_password'),
    path('add_company/',user_views.company,name='company'),
    path('iata/', user_views.get_iata, name='iata'),  
    path('hotels/',user_views.hotel_bycity,name='hotels'),
    
]

handler404 = 'user.views.error_404_view'