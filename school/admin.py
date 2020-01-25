from django.contrib import admin

# Register your models here.
from .models import About, Message, Principal, VicePrincipal, Headmistress

admin.site.register(About)
admin.site.register(Message)
admin.site.register(Principal)
admin.site.register(VicePrincipal)
admin.site.register(Headmistress)

