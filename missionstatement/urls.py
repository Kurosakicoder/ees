from django.urls import path
from . import views

app_name = 'missionstatement'

urlpatterns = [
    path('', views.mission, name='mission'),
]
