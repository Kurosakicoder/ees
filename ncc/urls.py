from django.urls import path
from . import views

app_name = 'ncc'

urlpatterns = [
    path('ncc/' , views.ncc , name='ncc'),
    # path('message/' , views.message , name='message'),
    # path('principal/' , views.principal , name='principal'),
    # path('vice_principal/' , views.vice_principal , name='vice_principal'),
    # path('headmistress/' , views.headmistress , name='headmistress'),
]
