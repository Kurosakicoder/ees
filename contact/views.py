from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):    
    contact = Contact.objects.last()
    template = 'contact/contact.html'
    context = {
        'contact': contact
    }
    return render(request, template, context)