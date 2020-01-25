from django.contrib import admin
from .models import SchoolAssembly, Trips, UpcomingEvents
# Register your models here.
admin.site.register(SchoolAssembly)
admin.site.register(Trips)
admin.site.register(UpcomingEvents)