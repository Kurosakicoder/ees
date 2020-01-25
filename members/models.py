from django.db import models

# Create your models here.
class Members(models.Model):
    image = models.ImageField(upload_to='members/')
    name = models.CharField(max_length=250)
    post = models.CharField(max_length=250) 

    def __str__(self):
	    return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'  
