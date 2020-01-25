from django.shortcuts import render
from .models import About, Message, Principal, VicePrincipal, Headmistress

# Create your views here.
def about(request):
    about = About.objects.last()
    template = 'school/about.html'
    context = {
        'about': about
    }
    return render(request, template, context)

def message(request):    
    message = Message.objects.all()
    template = 'school/messages.html'
    context = {
        'message': message
    }
    return render(request, template, context)

def principal(request):
    principal = Principal.objects.last()
    template = 'school/principal.html'
    context = {
        'principal': principal
    }
    return render(request, template, context)

def vice_principal(request):
    vice_principal = VicePrincipal.objects.last()
    template = 'school/vice-principal.html'
    context = {
        'vice_principal': vice_principal
    }
    return render(request, template, context) 

def headmistress(request):
    headmistress = Headmistress.objects.last()
    template = 'school/headmistress.html'
    context = {
        'headmistress': headmistress
    }
    return render(request, template, context)       
