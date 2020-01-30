from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('aboutacademics/', views.aboutacademics, name='aboutacademics'),
    path('highschool/', views.highschool, name='highschool'),
    path('highersecondaryschool/', views.highersecondaryschool,
         name='highersecondaryschool'),
    path('schooltiming/', views.schooltiming, name='schooltiming'),
    path('schoolanthem/', views.schoolanthem, name='schoolanthem'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('media/', views.syllabus, name='syllabus'),
]
