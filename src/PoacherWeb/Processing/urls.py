from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='index'),
    path('result',views.result,name='result'),
    path('videoUpload', views.videoUpload, name='video_upload'),
    path('videoProcess/', views.videoProcess, name='video_process')
]
