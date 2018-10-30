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
from app.src import UserManager
from app.src import ApkFileManager
from app.src import ApplicationManager
from app.src import PluginManager
from app.src import FileManager

urlpatterns = [
    path('home/index/', views.index),
    path('home/testPost/', views.testPost),
    path('home/getFile/', views.getFile),
    path('home/testForward/', views.testForward),
    path('home/getJokeList/', views.getJokeList),
    path('home/upLoadFiles/', views.upLoadFiles),

    # User
    path('user/login/', UserManager.user_login),
    path('user/registered/', UserManager.user_registered),
    path('user/delete/', UserManager.user_delete),
    # ApkFileManager
    path('apk/upload/apk/', ApkFileManager.upload_apk),
    path('apk/update/apk/', ApkFileManager.update_apk),
    path('apk/get/apk/list/', ApkFileManager.get_apk_list),
    path('apk/get/apk/', ApkFileManager.get_apk),
    path('apk/delete/apk/', ApkFileManager.delete_apk),
    path('apk/download/apk/', ApkFileManager.download_apk),
    # PluginManager
    path('apk/register/plugin/', PluginManager.register_plugin),
    path('apk/update/plugin/', PluginManager.update_plugin),
    path('apk/delete/plugin/', PluginManager.delete_plugin),
    path('apk/get/plugin/list/', PluginManager.get_plugin_list),
    path('apk/get/plugin/', PluginManager.get_plugin),
    # ApplicationManager
    path('apk/register/app/', ApplicationManager.register_app),
    path('apk/update/app/', ApplicationManager.update_app),
    path('apk/delete/app/', ApplicationManager.delete_app),
    path('apk/get/app/list/', ApplicationManager.get_app_list),
    path('apk/get/app/', ApplicationManager.get_app),

    # FileManager
    path('upLoadFile/', FileManager.up_load_file),
    path('getFile/', FileManager.get_file),

]



