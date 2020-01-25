from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Category(models.Model):
    category_year = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.category_year)

    def get_url(self):
	    return reverse('achievements:achievements_category', args=[self.slug])	    

    class Meta:
        ordering = ('category_year',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 

class Achievements(models.Model):
    event_date = models.CharField(max_length=250)
    student_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    student_class = models.CharField(max_length=250)
    student_position = models.CharField(max_length=250)
    event = models.TextField(default="") 

    def __str__(self):
        return '{}'.format(self.student_name)

    # def get_url(self):
	# 	return reverse('achievements:AchieveDetails', args=[self.category.slug, self.slug])    

    class Meta:
        ordering = ('student_name',)
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

       
