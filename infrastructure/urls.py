from django.urls import path
from . import views

app_name = 'infrastructure'

urlpatterns = [
    path('', views.infrastructure, name='infrastructure'),
]
