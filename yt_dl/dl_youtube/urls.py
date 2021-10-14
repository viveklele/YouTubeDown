from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download_video/', views.download_video, name='download'),
]