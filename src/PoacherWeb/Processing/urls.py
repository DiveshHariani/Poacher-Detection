from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='index'),
    path('result',views.result,name='result'),
    # path('process', views.upload)
]
