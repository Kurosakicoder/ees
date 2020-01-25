from django.contrib import admin

# Register your models here.

from .models import Circular, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_year','slug']
    prepopulated_fields = {'slug':('category_year',)}
admin.site.register(Category, CategoryAdmin)

class CircularAdmin(admin.ModelAdmin):
    list_display = ['circular_notice']
    prepopulated_fields = {'slug':('circular_notice',)}
    list_per_page = 20
admin.site.register(Circular, CircularAdmin) 
