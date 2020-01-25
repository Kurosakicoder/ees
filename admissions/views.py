from django.shortcuts import render
from .models import Admissions

# Create your views here.
def admissions(request):    
    admissions = Admissions.objects.last()
    template = 'admissions/admissions.html'
    context = {
        'admissions': admissions
    }
    return render(request, template, context)
 