from django.shortcuts import render
from .models import ForceBehind

# Create your views here.
def forcebehind(request):    
    forcebehind = ForceBehind.objects.all()
    template = 'forcebehind/forcebehind.html'
    context = {
        'forcebehind': forcebehind
    }
    return render(request, template, context)