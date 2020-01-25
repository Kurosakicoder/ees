from django.shortcuts import render
from .models import StudentCouncil
# Create your views here.
def studentcouncil(request):    
    studentcouncil = StudentCouncil.objects.all()
    template = 'studentcouncil/studentcouncil.html'
    context = {
        'studentcouncil': studentcouncil
    }
    return render(request, template, context)
