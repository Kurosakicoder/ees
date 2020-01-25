from django.contrib import admin
from .models import Category, Gallery
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','slug']
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['event_name']
    prepopulated_fields = {'slug':('event_name',)}
    list_per_page = 20
admin.site.register(Gallery, GalleryAdmin)  