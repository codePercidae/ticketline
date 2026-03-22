from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/", views.auth, name="auth"),
    path("login/", views.login, name="login")
    
]