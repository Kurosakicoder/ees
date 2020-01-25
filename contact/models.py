from django.db import models

# Create your models here.
class Contact(models.Model):
    address = models.CharField(max_length=500)
    phone_numbers = models.CharField(max_length=250)
    mailids = models.EmailField()

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'  
