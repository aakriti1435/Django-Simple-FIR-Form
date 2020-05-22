""" App URLS"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.opencomplaintform, name="opencform"),
    path('submitform', views.submitform, name="submitform"),
    #path('', views.complaintform, name="complaint_form"),
    #path('validate')
    #path('formsubmitted/', views.formsubmitted),


    #path('', views.openLoginPage, name="login_page"),
    #path('validate_login', views.validateUser, name="validate_login"),
    #path('validate_otp', views.validateOTP, name="validate_otp")

]
