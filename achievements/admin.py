from django.contrib import admin
from .models import Category, Achievements
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_year','slug']
    prepopulated_fields = {'slug':('category_year',)}
admin.site.register(Category, CategoryAdmin)

class AchievementsAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'student_class', 'student_position']
    prepopulated_fields = {'slug':('student_name',)}
    list_per_page = 20
admin.site.register(Achievements, AchievementsAdmin)  