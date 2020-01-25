from django.db import models
from datetime import date
# Create your models here.
class SchoolAssembly(models.Model):
    date = models.DateField()
    class_students =  models.CharField(max_length=50,default="")
    assembly_notice = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.class_students)

    class Meta:
        verbose_name = 'SchoolAssembly'
        verbose_name_plural = 'SchoolAssembly'

class Trips(models.Model):
    image = models.ImageField(upload_to='events/')
    date = models.DateField()
    headerline=  models.CharField(max_length=150,default="")
    first_para = models.TextField(default="")
    second_para = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.headerline)

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'

class UpcomingEvents(models.Model):
    date = models.DateField()
    headerline =  models.CharField(max_length=50,default="")
    program_notice = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.headerline)

    class Meta:
        verbose_name = 'UpcomingEvent'
        verbose_name_plural = 'UpcomingEvents'        
