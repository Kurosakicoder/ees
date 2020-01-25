from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_year = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250,default="")

    def __str__(self):
        return '{}'.format(self.category_year)

    def get_url(self):
	    return reverse('circular:circular_category', args=[self.slug])	    

    class Meta:
        ordering = ('category_year',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'   

class Circular(models.Model):
    date = models.DateField()
    
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    circular_notice = models.CharField(max_length=150,default="")
    slug = models.SlugField(max_length=250,default="")
    circular_details_two = models.TextField(default="") 

    def __str__(self):
        return str(self.date)
        

    class Meta:
        ordering = ('circular_notice',)
        verbose_name = 'Circular'
        verbose_name_plural = 'Circulars'

   
