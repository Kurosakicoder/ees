from django.shortcuts import render
from .models import NCC

# Create your views here.
def ncc(request):    
    ncc = NCC.objects.all()
    template = 'ncc/ncc.html'
    context = {
        'ncc': ncc
    }
    return render(request, template, context)