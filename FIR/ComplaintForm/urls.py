""" App URLS"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.complaintform),
    path('formsubmitted/', views.formsubmitted),
]

