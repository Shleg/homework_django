"""
URL configuration for homework_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from home_app.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path("hw1/", include('hw1_app.urls')),
    path("hw2/", include('hw2_app.urls')),
    path("hw3/", include('hw3_app.urls')),
    path("hw4/", include('hw4_app.urls'))
]
