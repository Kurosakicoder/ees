from django.db import models

# Create your models here.
class StudentCouncil(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    post =  models.CharField(max_length=150,default="")
    student_name = models.CharField(max_length=150,default="")

    def __str__(self):
	    return '{}'.format(self.post)

    class Meta:
        verbose_name = 'StudentCouncil'
        verbose_name_plural = 'StudentCouncil' 