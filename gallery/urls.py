from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.allCategories, name='allCategories'),
    path('<slug:c_slug>/', views.allCategories, name='gallery_category'),
]
