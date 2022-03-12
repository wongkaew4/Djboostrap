"""DjBootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from bootstrap import views
#from django.conf.urls import include

urlpatterns = [
    #path('', include('bootstrap.urls')),
    path('admin/', admin.site.urls),
    path('',views.bootstrap_index),
    path('page1',views.page1),
    path('page2',views.page2),
    path('addForm',views.addData)
]
