from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.newPage, name="new"),
    path("random", views.random, name="random"),
    path("<str:entry>", views.page, name="page"),
    path("<str:entry>/edit", views.edit, name="edit")
]
