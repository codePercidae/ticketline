from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/", views.auth, name="auth"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("buy/<int:event_id>", views.buy, name="buy"),
    path("buy/add_to_cart/<int:event_id>", views.add_to_cart, name="add_to_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("transaction/<int:totalsum>", views.transaction, name="transaction")
]