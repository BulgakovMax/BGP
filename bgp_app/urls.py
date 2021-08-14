"""Defines URL patterns for bgp_app."""

from django.urls import path

from . import views

app_name = 'bgp_app'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
]
