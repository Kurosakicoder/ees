from django.urls import path
from . import views

app_name = 'achievements'

urlpatterns = [
    path('', views.allCategories, name='allCategories'),
	path('<slug:c_slug>/', views.allCategories, name='achievements_category'),
	# path('<slug:c_slug>/<slug:achievements_slug>/', views.AchieveDetails, name='AchieveDetails'),
    # path('' , views.circular , name='circular'),
    # path('' , views.about , name='about'),
    # path('message/' , views.message , name='message'),

]