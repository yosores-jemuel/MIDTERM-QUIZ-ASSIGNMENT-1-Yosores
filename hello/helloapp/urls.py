from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("greet", views.greet_post, name="greet"),
]
