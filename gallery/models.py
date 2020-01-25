from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.category_name)

    def get_url(self):
	    return reverse('gallery:gallery_category', args=[self.slug])	    

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 

class Gallery(models.Model):
    event_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='gallery/')
    event_date = models.CharField(max_length=250)
    event_venue = models.CharField(max_length=250)
    event_details = models.TextField(default="")  
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    
    

    def __str__(self):
        return '{}'.format(self.event_name)

    # def get_url(self):
	# 	return reverse('achievements:AchieveDetails', args=[self.category.slug, self.slug])    

    class Meta:
        ordering = ('event_name',)
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

       
