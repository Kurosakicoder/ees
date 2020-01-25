from django.db import models

# Create your models here.
class Admissions(models.Model):
    admission_lower = models.TextField(default="")
    admission_hs = models.TextField(default="")
    fees_payment = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Admissions'
        verbose_name_plural = 'Admissions'  
