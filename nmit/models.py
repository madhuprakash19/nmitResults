from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=70,blank=True,null=True)
    usn = models.CharField(max_length=20,blank=True,null=True)
    branch = models.CharField(max_length=50,blank=True,null=True)
    sem = models.IntegerField(blank=True,null=True,default=5)

    def __str__(self):
        return str(self.name)+" "+str(self.usn)

class subjects(models.Model):
    code = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    credits = models.IntegerField(blank=True,null=True,default=4)

    def __str__(self):
        return str(self.name)

class gpa(models.Model):
    sname = models.ForeignKey(student,on_delete = models.CASCADE,blank=True,null=True)
    sgpa =  models.CharField(max_length=5,blank=True,null=True)
    cgpa =  models.CharField(max_length=5,blank=True,null=True)
    branch = models.CharField(max_length=50,blank=True,null=True)
    sem = models.IntegerField(blank=True,null=True,default=5)

    def __str__(self):
        return str(self.sname.name)

class marks(models.Model):
    sname = models.ForeignKey(student,on_delete = models.CASCADE,blank=True,null=True)
    subname = models.ForeignKey(subjects,on_delete = models.CASCADE,blank=True,null=True)
    creditsEarned =  models.IntegerField(blank=True,null=True,default=4)
    cie =  models.IntegerField(blank=True,null=True)
    see = models.IntegerField(blank=True,null=True)
    total = models.IntegerField(blank=True,null=True)
    grade = models.CharField(max_length=5,blank=True,null=True)

    def __str__(self):
        return str(self.sname.name)
