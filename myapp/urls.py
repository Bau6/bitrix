from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_video, name='generate_video'),
]

