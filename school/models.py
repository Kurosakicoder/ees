from django.db import models

# Create your models here.
class About(models.Model):
    image = models.ImageField(upload_to='school/')
    header_school = models.TextField(default="")
    about_school = models.TextField(default="")
    first_para = models.TextField(default="")
    second_para = models.TextField(default="")  
    testimony_name_one = models.CharField(max_length=50,default="")
    testimony_details_one = models.TextField(default="") 
    testimony_name_two = models.CharField(max_length=50,default="")
    testimony_details_two = models.TextField(default="") 
    testimony_name_three = models.CharField(max_length=50,default="")
    testimony_details_three = models.TextField(default="") 

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

class Message(models.Model):
    image = models.ImageField(upload_to='school/message/')
    name =  models.CharField(max_length=50,default="")
    paragraph = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

class Principal(models.Model):
    image = models.ImageField(upload_to='school/principal/')
    name =  models.CharField(max_length=50,default="")
    paragraph = models.TextField(default="")  

    def __str__(self):
	    return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Principal'
        verbose_name_plural = 'Principal'     

class VicePrincipal(models.Model):
    image = models.ImageField(upload_to='school/vice-principal/')
    name =  models.CharField(max_length=50,default="")
    paragraph = models.TextField(default="")  

    def __str__(self):
	    return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Vice-Principal'
        verbose_name_plural = 'Vice-Principal' 

class Headmistress(models.Model):
    image = models.ImageField(upload_to='school/headmistress/')
    name =  models.CharField(max_length=50,default="")
    paragraph = models.TextField(default="")  

    def __str__(self):
	    return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Headmistress'
        verbose_name_plural = 'Headmistress'         

     

      