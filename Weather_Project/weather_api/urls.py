from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_weather_info, name='get_weather'),
]