from django.db import models

# Create your models here.
class Infrastructure(models.Model):
    image = models.ImageField(upload_to='infrastructure/')
    name = models.CharField(max_length=250)
    paragraph = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Infrastructure'
        verbose_name_plural = 'Infrastructure'  
