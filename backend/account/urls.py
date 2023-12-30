from django.urls import path
from .views import *

urlpatterns = [
    path("", user_login),
    path("login", user_login),
    path("register", user_register),
    path("logout", user_logout),
    path("account", update_account),
]
