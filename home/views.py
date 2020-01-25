from django.shortcuts import render
from school.models import Headmistress
from members.models import Members
from infrastructure.models import Infrastructure
from contact.models import Contact
from school.models import About
from events.models import UpcomingEvents
from .models import Home
# Create your views here.
def home(request):
    notice = Home.objects.last()
    headmistress = Headmistress.objects.last()
    members = Members.objects.all()
    infrastructure = Infrastructure.objects.all()
    contact = Contact.objects.last()
    about = About.objects.last()
    upcomingevents = UpcomingEvents.objects.all()
    template = 'home/home.html'
    context = {
        'notice': notice,
        'headmistress_home': headmistress,
        'members_home': members,
        'infrastructure_home': infrastructure,
        'contact_home': contact,
        'about_home': about,
        'upcomingevents_home': upcomingevents 
    }

    return render(request, template, context)