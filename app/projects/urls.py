from django.urls import path
from . import views

urlpatterns = [
    path("",            views.ProjectsIndex,     name="ProjectsIndex"),
    path("<int:pk>/",   views.ProjectsDetail,    name="ProjectsDetail"),
]
