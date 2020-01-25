from django.shortcuts import render
from .models import MissionStatement

# Create your views here.
def mission(request):    
    mission = MissionStatement.objects.all()
    template = 'mission/mission.html'
    context = {
        'mission': mission
    }
    return render(request, template, context)