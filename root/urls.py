"""Entekhab_Vahed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from root import views

urlpatterns = [
    path('' , views.index , name='index'),
    url(r'^register/$' , views.signup , name='register'),
    url(r'^login/$' , views.signin , name='login'),
    url(r'^logout/$' , views.logout_ , name='logout'),
    url(r'^contactus/$' , views.contactus , name='contactus'),
    url(r'^profile/$' , views.profile , name='profile'),
    url(r'^editprofile/$' , views.editprofile , name='editprofile'),
    url(r'^panel/$' , views.panel , name='panel'),
    url(r'^new_course/$' , views.new_course , name='new_course'),

]
