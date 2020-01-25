from django.shortcuts import render
from .models import Infrastructure

# Create your views here.
def infrastructure(request):    
    infrastructure = Infrastructure.objects.all()
    template = 'infrastructure/infrastructure.html'
    context = {
        'infrastructure': infrastructure
    }
    return render(request, template, context)