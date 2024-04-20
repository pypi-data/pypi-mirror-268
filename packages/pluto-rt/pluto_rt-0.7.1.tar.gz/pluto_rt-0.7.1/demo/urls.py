from django.urls import include, path

from . import views

urlpatterns = [
    path("rt_messages/", include("pluto_rt.urls")),
    path("list/", views.demo_list, name="demo_list"),
    path("messages/", views.demo_messages, name="demo_messages"),
    path("progress/", views.demo_progress, name="demo_progress"),
    path("", views.demo_index),
]
