"""Daimhim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from app.src import views
from app.src import User
from app.src import ApkFileManager as afm

urlpatterns = [
    path('home/index/', views.index),
    path('home/testPost/', views.testPost),
    path('home/getFile/', views.getFile),
    path('home/testForward/', views.testForward),
    path('home/getJokeList/', views.getJokeList),
    path('home/upLoadFiles/', views.upLoadFiles),
    path('user/userLogin', User.userLogin),
    path('user/userRegistered', User.userRegistered),
    path('apk/upload/', afm.upload),
    path('apk/getApkList/', afm.get_apk_list),
]
