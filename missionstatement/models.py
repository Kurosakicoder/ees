from django.db import models

# Create your models here.
class MissionStatement(models.Model):
    paragraph = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'MisssionStatement'
        verbose_name_plural = 'MisssionStatement'  
