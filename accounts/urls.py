from django import views
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path("",views.index),
    path("login",views.login),
    path("signup",views.signup),
    path("index",views.index),
]