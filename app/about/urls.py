from django.urls import path
from . import views

urlpatterns = [
    path("",                views.AboutIndex,    name="AboutIndex"),
    path("profile/",        views.Profile,       name="Profile")
]
