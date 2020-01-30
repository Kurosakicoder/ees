from django.urls import path
from . import views

app_name = 'ncc'

urlpatterns = [
    path('ncc/', views.ncc, name='ncc'),
]
