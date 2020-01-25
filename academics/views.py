from django.shortcuts import render
from .models import AboutAcademics, HighSchool, HigherSecondarySchool, SchoolAnthem, SchoolTiming, Syllabus
# Create your views here.
def aboutacademics(request):
    aboutacademics = AboutAcademics.objects.last()
    template = 'academics/aboutacademics.html'
    context = {
        'aboutacademics': aboutacademics
    }
    return render(request, template, context)

def highschool(request):
    highschool = HighSchool.objects.last()
    template = 'academics/highschool.html'
    context = {
        'highschool': highschool
    }
    return render(request, template, context)

def highersecondaryschool(request):
    highersecondaryschool = HigherSecondarySchool.objects.last()
    template = 'academics/higher.html'
    context = {
        'highersecondaryschool': highersecondaryschool
    }
    return render(request, template, context)

def schooltiming(request):
    schooltiming = SchoolTiming.objects.last()
    template = 'academics/schooltiming.html'
    context = {
        'schooltiming': schooltiming
    }
    return render(request, template, context)

def schoolanthem(request):
    schoolanthem = SchoolAnthem.objects.last()
    template = 'academics/schoolanthem.html'
    context = {
        'schoolanthem': schoolanthem
    }
    return render(request, template, context)  

def syllabus(request):
    syllabus = Syllabus.objects.all()
    template = 'academics/syllabus.html'
    context = {
        'syllabus': syllabus
    }
    return render(request, template, context)    

def syllabus(request):
    syllabus = Syllabus.objects.all()
   
    template = 'academics/syllabus.html'
    context = {
        'syllabus': syllabus
    }
    return render(request, template, context)     