from django.urls import path
from . import views

app_name = 'circular'

urlpatterns = [
    path('' , views.circular , name='circular'),
    path('<slug:c_slug>/', views.circular, name='circular_category'),
    # path('' , views.about , name='about'),
    # path('message/' , views.message , name='message'),
    # path('principal/' , views.principal , name='principal'),
    # path('vice_principal/' , views.vice_principal , name='vice_principal'),
    # path('headmistress/' , views.headmistress , name='headmistress'),
]