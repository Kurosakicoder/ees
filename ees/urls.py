"""ees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLcon
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls' , namespace='home')),
    path('about/', include('school.urls', namespace='aboutus')),
    path('circular/', include('circular.urls', namespace='circular')),
    path('events/', include('events.urls', namespace='events')),
    path('achievements/', include('achievements.urls', namespace='achievements')),
    path('studentcouncil/', include('studentcouncil.urls', namespace='studentcouncil')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('missionstatement/', include('missionstatement.urls', namespace='missionstatement')),
    path('forcebehind/', include('forcebehind.urls', namespace='forcebehind')),
    path('members/', include('members.urls', namespace='members')),
    path('infrastructure/', include('infrastructure.urls', namespace='infrastructure')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('admissions/', include('admissions.urls', namespace='admissions')),
    path('ncc/', include('ncc.urls', namespace='ncc')),
    path('academics/', include('academics.urls', namespace='academics')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "EEHS SCHOOL ADMIN"
admin.site.site_title = "EEHS SCHOOL ADMIN"
admin.site.site_index_title = "Welcome To EEHS School Admin Panel"