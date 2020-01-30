from django.urls import path
from . import views

app_name = 'circular'

urlpatterns = [
    path('', views.circular, name='circular'),
    path('<slug:c_slug>/', views.circular, name='circular_category'),
]
