from django.urls import path
from . import views

app_name = "Projects"

urlpatterns = [
    path("",                    views.Index,                    name="Index"),
    path("<int:pk>",            views.Detail,                   name="Detail"),
    path("FilterByTechnology",  views.FilterByTechnology,       name="FilterByTechnology"),
]
