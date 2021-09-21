from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lga/", views.total, name='total'),
    path("create/", views.create, name='create')
]