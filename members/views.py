from django.shortcuts import render
from .models import Members

# Create your views here.
def members(request):    
    members = Members.objects.all()
    template = 'members/members.html'
    context = {
        'members': members
    }
    return render(request, template, context)