from django.db import models

# Create your models here.
class NCC(models.Model):
    image = models.ImageField(upload_to='ncc/')
    date = models.DateField()
    headerline =  models.CharField(max_length=500,default="")

    def __str__(self):
	    return '{}'.format(self.headerline)

    class Meta:
        verbose_name = 'NCC'
        verbose_name_plural = 'NCC'
