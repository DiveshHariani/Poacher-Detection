from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='index'),
    # path('process', views.upload)
]
