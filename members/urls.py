from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('' , views.members , name='members'),
    # path('trips/' , views.trips , name='trips'),
    # path('upcomingevents/' , views.upcomingevents , name='upcomingevents'),
    # path('message/' , views.message , name='message'),
    # path('principal/' , views.principal , name='principal'),
    # path('vice_principal/' , views.vice_principal , name='vice_principal'),
    # path('headmistress/' , views.headmistress , name='headmistress'),
]
