from django.db import models

# Create your models here.
class ForceBehind(models.Model):
    image = models.ImageField(upload_to='forcebehind/')
    name = models.CharField(max_length=250)
    post = models.CharField(max_length=250) 
    paragraph = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.name)

    class Meta:
        verbose_name = 'ForceBehind'
        verbose_name_plural = 'ForceBehind'  
