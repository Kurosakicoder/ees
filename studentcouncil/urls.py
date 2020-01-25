from django.urls import path
from . import views

app_name = 'studentcouncil'

urlpatterns = [
    path('studentcouncil/' , views.studentcouncil , name='studentcouncil'),
    # path('trips/' , views.trips , name='trips'),
    # path('upcomingevents/' , views.upcomingevents , name='upcomingevents'),
]
