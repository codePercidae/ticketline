from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path("tickets/", include(""))
    path("", views.index, name="index")
]