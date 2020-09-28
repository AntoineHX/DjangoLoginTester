from django.urls import path
from loginApp import views

urlpatterns = [
    path("", views.home, name="home"),
]