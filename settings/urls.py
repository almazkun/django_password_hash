"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.shortcuts import render
from hashhash.views import create_user, create_user_form
from api.views import ModelSView, SerializerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: render(request, "home.html"), name="home"),
    path("create_user/", create_user, name="create_user"),
    path("create_user_form/", create_user_form, name="create_user_form"),
    path("model_s", ModelSView.as_view(), name="model_s"),
    path("serializer", SerializerView.as_view(), name="serializer"),
]
