from django.db import models

# Create your models here.
class Home(models.Model):
    important_notice = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home' 