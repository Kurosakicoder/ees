from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('aboutacademics/' , views.aboutacademics , name='aboutacademics'),
    path('highschool/' , views.highschool , name='highschool'),
    path('highersecondaryschool/' , views.highersecondaryschool , name='highersecondaryschool'),
    path('schooltiming/' , views.schooltiming , name='schooltiming'),
    path('schoolanthem/' , views.schoolanthem , name='schoolanthem'),
    path('syllabus/' , views.syllabus , name='syllabus'),
    path('media/' , views.syllabus , name='syllabus'),
    # path('', views.allCategories, name='allCategories'),
	# path('<slug:c_slug>/', views.allCategories, name='achievements_category'),
	# path('<slug:c_slug>/<slug:achievements_slug>/', views.AchieveDetails, name='AchieveDetails'),
    # path('' , views.circular , name='circular'),
    # path('' , views.about , name='about'),
    # path('message/' , views.message , name='message'),

]