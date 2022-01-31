from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('second/', views.second),
    path('third/', views.third),
    path('login/', views.login),

]
