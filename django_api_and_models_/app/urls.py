from django import urls
from django.urls import path
from app import views as app_views
urlpatterns = [
    path('app/',app_views.app,name='app'),
   ]