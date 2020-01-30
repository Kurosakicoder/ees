from django.urls import path
from . import views

app_name = 'forcebehind'

urlpatterns = [
    path('', views.forcebehind, name='forcebehind'),
]
