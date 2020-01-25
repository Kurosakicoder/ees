from django.shortcuts import render
from .models import SchoolAssembly, Trips, UpcomingEvents
# Create your views here.

def schoolassembly(request):    
    schoolassembly = SchoolAssembly.objects.all()
    template = 'events/schoolassembly.html'
    context = {
        'schoolassembly': schoolassembly
    }
    return render(request, template, context)

def trips(request):    
    trips = Trips.objects.all()
    template = 'events/trips.html'
    context = {
        'trips': trips
    }
    return render(request, template, context)

def upcomingevents(request):    
    upcomingevents = UpcomingEvents.objects.all()
    template = 'events/upcomingevents.html'
    context = {
        'upcomingevents': upcomingevents
    }
    return render(request, template, context)    
