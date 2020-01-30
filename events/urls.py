from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('schoolassembly/', views.schoolassembly, name='schoolassembly'),
    path('trips/', views.trips, name='trips'),
    path('upcomingevents/', views.upcomingevents, name='upcomingevents'),
]
