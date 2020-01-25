from django.db import models

# Create your models here.
class AboutAcademics(models.Model):
    school_terms = models.TextField(default="")
    school_pdf_calender = models.FileField(upload_to='schoolacademiccalenderpdf/')
    awards_scholarships = models.TextField(default="")
    disciplinary_rules = models.TextField(default="")
    examination_promotion = models.TextField(default="")
    leave_of_absence = models.TextField(default="")
    certificate = models.TextField(default="")
    notes_parents_guardians = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'AboutAcademics'
        verbose_name_plural = 'AboutAcademics'  

class HighSchool(models.Model):
    curriculum_school = models.TextField(default="")
    coscholastic_activities = models.TextField(default="")
    cocurricular_activities = models.TextField(default="")
    work_experience = models.TextField(default="")
    school_uniform = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'HighSchool'
        verbose_name_plural = 'HighSchool' 

class HigherSecondarySchool(models.Model):
    curriculum_hs = models.TextField(default="") 
    courses_study = models.TextField(default="")
    school_uniform = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'HigherSecondarySchool'
        verbose_name_plural = 'HigherSecondarySchool' 

class SchoolTiming(models.Model):
    school_timing = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'SchoolTiming'
        verbose_name_plural = 'SchoolTiming'     

class SchoolAnthem(models.Model):
    school_anthem = models.TextField(default="")

    def __str__(self):
	    return '{}'.format(self.id)

    class Meta:
        verbose_name = 'SchoolAnthem'
        verbose_name_plural = 'SchoolAnthem'     

class Syllabus(models.Model):
    syllabus_header = models.TextField(default="")
    syllabus_pdf = models.FileField(upload_to='syllabuspdf/')

    def __str__(self):
	    return '{}'.format(self.syllabus_header)

    class Meta:
        verbose_name = 'Syllabus'
        verbose_name_plural = 'Syllabus'               

