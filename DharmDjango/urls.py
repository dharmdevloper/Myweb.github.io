"""
Definition of urls for DharmDjango.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views, models
from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = "Dharma Wines Admin"
admin.site.site_title = "Dharma Wines Portal"
admin.site.index_title = "Welcome to Dharm Wines Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name='app'),
    path('index/',views.index,name='index' ),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
